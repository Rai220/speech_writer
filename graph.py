import time
from typing import Annotated, List, Literal, TypedDict

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_gigachat.chat_models.gigachat import GigaChat
from langchain_gigachat.embeddings import GigaChatEmbeddings
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.types import Command, interrupt
import requests

# LLM GigaChat
giga_low_topp = GigaChat(
    model="GigaChat-Max",
    verify_ssl_certs=False,
    profanity_check=False,
    base_url="https://gigachat.sberdevices.ru/v1",
    top_p=0,
    streaming=True,
    max_tokens=8000,
    timeout=600,
)

# Эмбеддер GigaChat
giga_embed = GigaChatEmbeddings(
    scope="GIGACHAT_API_PERS",
    verify_ssl_certs=False,
    model="EmbeddingsGigaR",
    base_url="https://gigachat.sberdevices.ru/v1",
)

files = [
    "ukaz_309.md",
    "burnaev.md",
    "president_direct_line_2024.md",
    "president_aij_2024.md",
]
all_content = {}

for file_path in files:
    url = f'https://raw.githubusercontent.com/Rai220/speech_writer/refs/heads/main/dataset/{file_path}'

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Не удалось скачать файл. Статус код: {response.status_code}")    
    
    # Открываем и читаем содержимое файла
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(f"Размер файла {file_path} - {len(content)} байт")
    all_content[file_path] = content

    docs = {
        "president_direct_line_2024.md": "Прямая линия Путина 2024",
        "president_aij_2024.md": "Конференция AI Journey 2024",
    }

for doc in docs:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200, chunk_overlap=350, length_function=len, keep_separator=True
    )
    chunks = splitter.split_text(all_content[doc])
    print(f"Количество чанков: {len(chunks)}")

    metadatas = [{"document": docs[doc]} for _ in range(len(chunks))]
    vectorstore = Chroma.from_texts(chunks, embedding=giga_embed, metadatas=metadatas)
    
print("Векторная БД заполнена")

class SpeechWriterState(MessagesState):
    speech_topic: str
    time_to_speak: str
    speech_plan: str
    speaker_bio: str
    result_speech: str
    critique: list[str]
    retriever_citations: str

def plan_speech(state: SpeechWriterState):
    TEMPLATE = """
Ты - агент-аналитик, который занимается помощью в составлении отличных речей для политиков.
Ты должен помочь спичрайтеру написать хорошую речь, поэтому ты должен составить техническое задание на написание речи
Тема выступления - {speech_topic}. Время выступления - {time_to_speak}.

Вот биография спикера для которого нужно написать речь:
<BIO>
{speaker_bio}
</BIO>

Вот документ на основании которого нужно написать речь:
<MAIN_DOCUMENT>
{content}
</MAIN_DOCUMENT>

Вот дополнительные документы, которые нужно учесть при составлении речи:
<ADDITIONAL_DOCUMENTS>
{additional_content}
</ADDITIONAL_DOCUMENTS>

Твой ответ должен быть в формате JSON:

**Формат вывода:**
```JSON
{{
  "speech_structure": "<структура речи по тематикам, релевантную заявленному формату мероприятия>",
  "tezis_structure: "<структуру тезисов в соответствии с приоритетами стратегических документов.>",
  "speech_tz: "<тз на написание речи>",
  "actual_citations: "<актуальные цитаты из исходных документов по теме выступления>"
}}```
    """
    print(f"📝 Speech planner начинает работу")
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", TEMPLATE),
        ]
    )

    pipe = chat_template | giga_low_topp | StrOutputParser()

    resp = pipe.invoke(
        {
            "speech_topic": state["speech_topic"],
            "time_to_speak": state["time_to_speak"],
            "content": all_content["ukaz_309.md"],
            "additional_content": all_content["burnaev.md"],
            "speaker_bio": state["speaker_bio"],
        }
    )

    # printmd(f"Составлен план документа:\n{resp}")

    return {"speech_plan": resp}


def write_speech(state: SpeechWriterState):
    TEMPLATE = """
Ты - агент-спичрайтер. Ты должен написать речь для политиков на основании данных тебе документов.
Тема выступления - {speech_topic}. Время выступления - {time_to_speak}.

Вот биография спикера для которого нужно написать речь:
<BIO>
{speaker_bio}
</BIO>

Вот документ на основании которого нужно написать речь:
<MAIN_DOCUMENT>
{content}
</MAIN_DOCUMENT>

Вот дополнительные документы, которые нужно учесть при составлении речи:
<ADDITIONAL_DOCUMENTS>
{additional_content}
</ADDITIONAL_DOCUMENTS>

План выступления и вспомогательные инструкции от твоего коллеги-планировщика:
<SPEECH_PLAN>
{speech_plan}
</SPEECH_PLAN>

Вот предыдущая версия речи, которую ты написал на прошлой итерации (если есть):
<SPEECH_TEXT>
{result_speech}
<SPEECH_TEXT>

Вот набор отрывков из выступлений Путина, которые нужно обязательно использовать при составлении речи:
<PUTIN_SPEECH>
{retriever_citations}
</PUTIN_SPEECH>
Обязательно процитируй В. В. Путина в своей речи (если отрывки предоставлены). Обязательно укажи явно, что это цитата В. В. Путина!!!

Вот конструктивная критика твоей предыдущей версии речи (если есть):
<CRITIQUE>
{critique}
</CRITIQUE>

Итоговая речь должна быть красиво оформлена в формате Markdown и представлять собой набор пунктов.
Если это речь для награждения - держи интригу, не называй победителя сразу.
Укажи время чтения в скобках под заголовком.
"""

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", TEMPLATE),
        ]
    )

    pipe = chat_template | giga_low_topp | StrOutputParser()

    critique = state.get("critique", [""])[-1]
    citations = f'{state.get("retriever_citations", "")}'
    print(f"👨‍💻 Writer начинает работу. Объем цитат: {len(citations)}")

    resp = pipe.invoke(
        {
            "speech_topic": state["speech_topic"],
            "time_to_speak": state["time_to_speak"],
            "content": all_content["ukaz_309.md"],
            "additional_content": all_content["burnaev.md"],
            "speech_plan": state["speech_plan"],
            "speaker_bio": state["speaker_bio"],
            "result_speech": state.get("result_speech", ""),
            "critique": critique,
            "retriever_citations": citations,
        }
    )

    return {"result_speech": resp}


def critique(
    state: SpeechWriterState,
) -> Command[Literal["👨‍💻 Writer", "🌐 Retriever", END]]:
    TEMPLATE = """
Ты - агент-выпускающий редактор, который занимается помощью в составлении отличных речей для политиков. Ты должен оценить речь и решить - готова ли она или её нужно доработать.
Ты должен помочь спичрайтеру написать хорошую речь, твоя задача качественно оценить написанную речь и дать конструктивную обратную свзяь, если она требуется.

Ты должен дать ограниченное количество критики. В какой-то момент нужно остановиться и завершить написание речи.
Тема выступления - {speech_topic}. Время выступления - {time_to_speak}.

Вот биография спикера для которого нужно написать речь:
<BIO>
{speaker_bio}
</BIO>

Вот документ на основании которого нужно написать речь:
<MAIN_DOCUMENT>
{content}
</MAIN_DOCUMENT>

Вот дополнительные документы, которые нужно учесть при составлении речи:
<ADDITIONAL_DOCUMENTS>
{additional_content}
</ADDITIONAL_DOCUMENTS>

Вот текущий текст речи, который тебе надо оценить:
<SPEECH_TEXT>
{result_speech}
<SPEECH_TEXT>

Вот критика, которую ты давал ранее на предыдущие версии речи (если есть). Не повторяйся, не пиши ту же самую критику заново.
<OLD_CRITIQUE>
{old_critique}
</OLD_CRITIQUE>
Если ты не можешь дать никакой принципиально новой критики - прими решение good.
Текст обязательно должен содержать цитаты Путина. Если это не так, то в качестве финального решения прими решение final_decision = retrieve

Твой ответ должен быть в формате JSON:

**Формат вывода:**
```JSON
{{
  "thoughts": <твои мысли по поводу написанной речи>,
  "critique": <конструктивная критика речи - что нужно поправить или доработать>,
  "is_new_critique": <есть ли в твоей критики что-то принципиально новое, если сравнивать со старой критикой (если она была) - True или False>,
  "final_decision: <итоговое решение, должно быть одно из следующих: - good (если нет новой критики и речь закончена), fix (если требуется переписать речь), retrieve (если требуется поиск дополнительных цитат)>
}}```
    """

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", TEMPLATE),
        ]
    )

    pipe = chat_template | giga_low_topp | JsonOutputParser()

    print(f"🧑‍⚖️ Critic начинает работу")

    resp = pipe.invoke(
        {
            "speech_topic": state["speech_topic"],
            "time_to_speak": state["time_to_speak"],
            "content": all_content["ukaz_309.md"],
            "additional_content": all_content["burnaev.md"],
            "speaker_bio": state["speaker_bio"],
            "result_speech": state.get("result_speech", ""),
            "old_critique": state.get("critique", []),
        }
    )

    final_decision = resp.get("final_decision", "good")
    critique = resp.get("critique", "")
    is_new_critique = resp.get("is_new_critique", "False")
    # printmd(f"Составлена критика документа:\n{resp}")
    print(
        f"Критик принял решение: {final_decision}, is_new_critique: {is_new_critique}"
    )

    old_critique = state.get("critique", [])
    old_critique.append(critique)
    update = {"critique": old_critique}

    goto = END
    if final_decision == "fix" and is_new_critique:
        goto = "👨‍💻 Writer"
    if final_decision == "retrieve":
        goto = "🌐 Retriever"

    return Command(update=update, goto=goto)


def retriever(state: SpeechWriterState):
    print(f"🌐 Retriever начинает работу")
    result = graph.get_state(config=config).values["result_speech"]
    docs = vectorstore.similarity_search(result[0:2048], k=4)  # Depends on embeddings
    return {"retriever_citations": f"{docs}"}


from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph

builder = StateGraph(SpeechWriterState)
builder.add_node("📝 Speech planner", plan_speech)
builder.add_node("👨‍💻 Writer", write_speech)
builder.add_node("🧑‍⚖️ Critic", critique)
builder.add_node("🌐 Retriever", retriever)

builder.add_edge(START, "📝 Speech planner")
builder.add_edge("📝 Speech planner", "👨‍💻 Writer")
builder.add_edge("👨‍💻 Writer", "🧑‍⚖️ Critic")
builder.add_edge("🌐 Retriever", "👨‍💻 Writer")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)


# Comment me to debug!
# speaker_bio = """Дмитрий Николаевич Чернышенко (род. 20 сентября 1968 года в Саратове) — российский государственный деятель и предприниматель. В 1993 году стал соучредителем одного из крупнейших в России коммуникационных холдингов Media Arts, которым управлял в течение 12 лет.
# С 2007 по 2014 год занимал должность президента Организационного комитета XXII Олимпийских зимних игр и XI Паралимпийских зимних игр 2014 года в Сочи, сыграв ключевую роль в их подготовке и проведении.
# В 2015 году возглавил АО «Газпром-Медиа Холдинг», где занимал пост генерального директора и председателя правления до 2020 года.
# С 21 января 2020 года назначен заместителем председателя правительства Российской Федерации, курируя вопросы цифровой экономики, инноваций, связи, СМИ, а также культуры, туризма и спорта.
# Чернышенко награжден орденом «За заслуги перед Отечеством» II степени, орденом Дружбы и орденом Почета.
# Он увлекается горными лыжами и боевыми искусствами."""

# inputs = {
#     "speech_topic": "Награждение Евгения Бурнаева на Научной премии Сбера (номинация «Цифровая Вселенная»)",
#     "time_to_speak": "5 минут",
#     "speaker_bio": speaker_bio,
# }

# config = {"configurable": {"thread_id": "1"}}
# start = time.time()
# for output in graph.stream(inputs, config=config, stream_mode="updates"):
#     current_agent = next(iter(output))
#     print(f"Отработал агент {current_agent}. Время: {int(time.time() - start)}с")
