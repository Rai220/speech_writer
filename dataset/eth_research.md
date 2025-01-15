[Перейти к основному содержанию](#main-content)

Последнее обновление страницы:12 августа 2024 г.

# Направления проводимых исследований Ethereum

Одно из ключевых преимуществ Ethereum — активное сообщество исследователей и разработчиков, которые постоянно совершенствуют сеть. Множество квалифицированных энтузиастов по всему миру готовы взяться за решение проблем Ethereum, но не всегда легко понять, в чем именно заключаются эти проблемы. На этой странице описаны основные направления проводимых исследований, и она служит примерным руководством по передовым возможностям Ethereum.

## [how ethereum research works permalink](\#how-ethereum-research-works) Как работают исследования Ethereum

Исследования в Ethereum открыты, прозрачны и воплощают принципы [децентрализованной науки (DeSci)(opens in a new tab)](https://hackernoon.com/desci-decentralized-science-as-our-chance-to-recover-the-real-science). Подход заключается в предоставлении инструментов и результатов исследований в как можно более открытом и интерактивном виде, например посредством исполнимых блокнотов. Исследования в Ethereum продвигаются быстро, новые данные публикуются и обсуждаются открыто на форумах, таких как [ethresear.ch(opens in a new tab)](https://ethresear.ch/), а не публикуются в традиционных медиа после прохождения нескольких этапов рецензирования.

## [general research resources permalink](\#general-research-resources) Основные ресурсы по исследованиям

Независимо от конкретной темы, огромное количество информации по исследованиям в Ethereum можно найти на форуме [ethresear.ch(opens in a new tab)](https://ethresear.ch) и в [Discord-канале Eth R&D(opens in a new tab)](https://discord.gg/qGpsxSA). Это основные места, где исследователи Ethereum обсуждают новейшие идеи и возможности разработки.

В этом отчете, опубликованном [DelphiDigital(opens in a new tab)](https://members.delphidigital.io/reports/the-hitchhikers-guide-to-ethereum) в мае 2022 года, представлен хороший обзор дорожной карты Ethereum.

## [sources of funding permalink](\#sources-of-funding) Источники финансирования

Вы можете участвовать в исследованиях Ethereum и получать за это деньги! Например, [фонд Ethereum](/ru/foundation/) недавно провел [раунд финансирования "Академические гранты"(opens in a new tab)](https://esp.ethereum.foundation/academic-grants). Информацию о действующих и будущих возможностях финансирования можно найти на [странице грантов Ethereum](/ru/community/grants/).

## [protocol research permalink](\#protocol-research) Исследования протокола

Исследования протокола касаются базового уровня Ethereum — набора правил, определяющих подключение узлов, их взаимодействие, обмен данными Ethereum и их хранение, а также достижение консенсуса касательно состояния блокчейна. Исследования протокола разделены на высшем уровне на две категории: консенсус и исполнение.

### [consensus permalink](\#consensus) Консенсус

Исследования консенсуса касаются [механизма доказательства доли владения](/ru/developers/docs/consensus-mechanisms/pos/) в Ethereum. Примеры тем исследований консенсуса:

- обнаружение и исправление уязвимостей;
- количественная оценка криптоэкономической безопасности;
- повышение безопасности или производительности форм реализации клиентов;
- и разработка легких клиентов.

Проводимые исследования касаются не только будущего, но и фундаментальной переработки протокола, например финализации в одном слоте, которая позволит значительно улучшить Ethereum. Кроме того, эффективность, безопасность и мониторинг взаимодействия между консенсус-клиентами — тоже важные темы для исследования.

#### [background reading permalink](\#background-reading) Дополнительные материалы

- [Введение в доказательство доли владения](/ru/developers/docs/consensus-mechanisms/pos/)
- [Документ Casper-FFG(opens in a new tab)](https://arxiv.org/abs/1710.09437)
- [Поясняющая статья Casper-FFG(opens in a new tab)](https://arxiv.org/abs/1710.09437)
- [Документ Gasper(opens in a new tab)](https://arxiv.org/abs/2003.03052)

#### [recent research permalink](\#recent-research) Недавние исследования

- [Консенсус Ethresear.ch(opens in a new tab)](https://ethresear.ch/c/consensus/29)
- [Дилемма доступности/финализации(opens in a new tab)](https://arxiv.org/abs/2009.04987)
- [Финализация в одном слоте(opens in a new tab)](https://ethresear.ch/t/a-model-for-cumulative-committee-based-finality/10259)
- [Разделение тех, кто предлагает, и тех, кто создает(opens in a new tab)](https://notes.ethereum.org/@vbuterin/pbs_censorship_resistance)

### [execution permalink](\#execution) Исполнение

Уровень исполнения связан с выполнением транзакций, работой [виртуальной машины Ethereum (EVM)](/ru/developers/docs/evm/) и созданием полезных нагрузок для передачи на уровень консенсуса. Исследования проводятся в различных направлениях, включая следующие:

- разработка поддержки легких клиентов;
- исследование лимитов газа;
- и добавление новых структур данных (например, деревьев Веркла).

#### [background reading 1 permalink](\#background-reading-1) Дополнительные материалы

- [Введение в EVM](/ru/developers/docs/evm/)
- [Уровень исполнения Ethresear.ch(opens in a new tab)](https://ethresear.ch/c/execution-layer-research/37)

#### [recent research 1 permalink](\#recent-research-1) Недавние исследования

- [Оптимизация баз данных(opens in a new tab)](https://github.com/ledgerwatch/erigon/blob/devel/docs/programmers_guide/db_faq.md)
- [Окончание действия данных о состоянии(opens in a new tab)](https://notes.ethereum.org/@vbuterin/state_expiry_eip)
- [Пути к окончанию действия данных о состоянии(opens in a new tab)](https://hackmd.io/@vbuterin/state_expiry_paths)
- [Предложение по деревьям Веркла и окончанию действия данных о состоянии(opens in a new tab)](https://notes.ethereum.org/@vbuterin/verkle_and_state_expiry_proposal)
- [Управление историей(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-4444)
- [Деревья Веркла(opens in a new tab)](https://vitalik.eth.limo/general/2021/06/18/verkle.html)
- [Проверка доступности данных(opens in a new tab)](https://github.com/ethereum/research/wiki/A-note-on-data-availability-and-erasure-coding)

## [client development permalink](\#client-development) Разработка клиентов

Клиенты Ethereum — это реализации протокола Ethereum. В процессе разработки в клиенты внедряется результаты исследований протокола. Обновляются спецификации и создаются конкретные реализации.

Узел Ethereum должен поддерживать работу двух элементов программного обеспечения:

1. Консенсус-клиент, который следит за вершиной блокчейна, обменивается блоками и обрабатывает логику консенсуса.
2. Клиент исполнения, который поддерживает виртуальную машину Ethereum, выполняет транзакции и смарт-контракты.

Дополнительную информацию об узлах и клиентах, а также список всех текущих реализаций клиентов см. на [странице об узлах и клиентах](/ru/developers/docs/nodes-and-clients/). Историю всех обновлений Ethereum можно найти на [странице истории](/ru/history/).

### [execution clients permalink](\#execution-clients) Клиенты исполнения:

- [Спецификация клиента исполнения(opens in a new tab)](https://github.com/ethereum/execution-specs)
- [Спецификация API исполнения(opens in a new tab)](https://github.com/ethereum/execution-apis)

### [consensus clients permalink](\#consensus-clients) Клиенты консенсуса:

- [Спецификация клиента консенсуса(opens in a new tab)](https://github.com/ethereum/consensus-specs)
- [Спецификация Beacon API(opens in a new tab)](https://ethereum.github.io/beacon-APIs/#/Beacon/getStateRoot)

## [scaling and performance permalink](\#scaling-and-performance) Масштабирование и производительность

Масштабирование Ethereum — это важное направление работы исследователей Ethereum. Текущие подходы включают перенос транзакций в свертки и их удешевление с помощью blob-объектов данных. Вводная информация о масштабировании Ethereum доступна на [этой странице](/ru/developers/docs/scaling/).

### [layer 2 permalink](\#layer-2) Уровень 2

Существует несколько протоколов уровня 2, которые масштабируют Ethereum, используя разные техники группировки транзакций и обеспечения их безопасности на уровне 1 Ethereum. Это быстро развивающаяся тема с огромным потенциалом для исследований и разработок.

#### [background reading 2 permalink](\#background-reading-2) Дополнительные материалы

- [Введение в решения второго уровня](/ru/layer-2/)
- [Polynya: свертки, доступность данных и модулярные цепочки(opens in a new tab)](https://polynya.medium.com/rollups-data-availability-layers-modular-blockchains-introductory-meta-post-5a1e7a60119d)

#### [recent research 2 permalink](\#recent-research-2) Недавние исследования

- [Справедливый порядок секвенсоров в Arbitrum(opens in a new tab)](https://eprint.iacr.org/2021/1465)
- [Уровень 2 от ethresear.ch(opens in a new tab)](https://ethresear.ch/c/layer-2/32)
- [Дорожная карта с упором на свертки(opens in a new tab)](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)
- [L2Beat(opens in a new tab)](https://l2beat.com/)

### [bridges permalink](\#bridges) Мосты

Такое решение уровня 2, как безопасные и эффективные мосты, требует дополнительных исследований и разработок. Сюда входят мосты между разными решениями уровня 2, а также между уровнем 1 и уровнем 2. Это особенно важное направление исследований, потому что мосты часто становятся мишенью хакеров.

#### [background reading 3 permalink](\#background-reading-3) Дополнительные материалы

- [Введение в блокчейн-мосты](/ru/bridges/)
- [Виталик о мостах(opens in a new tab)](https://old.reddit.com/r/ethereum/comments/rwojtk/ama_we_are_the_efs_research_team_pt_7_07_january/hrngyk8/)
- [Статья о блокчейн-мостах(opens in a new tab)](https://medium.com/1kxnetwork/blockchain-bridges-5db6afac44f8)
- [Ценность, содержащаяся в мостах(opens in a new tab)](https://dune.com/eliasimos/Bridge-Away-(from-Ethereum))

#### [recent research 3 permalink](\#recent-research-3) Недавние исследования

- [Проверка мостов(opens in a new tab)](https://stonecoldpat.github.io/images/validatingbridges.pdf)

### [sharding permalink](\#sharding) Шардинг

Шардинг блокчейна Ethereum долгое время был частью дорожной карты разработки. Но сейчас на первый план выходят новые решения в масштабировании, такие как данкшардинг.

Предшественник полного данкшардинга, известный как протоданкшардинг, был реализован в обновлении сети Cancun-Deneb (Dencun).

[Подробнее об обновлении Dencun](/ru/roadmap/dencun/)

#### [background reading 4 permalink](\#background-reading-4) Дополнительные материалы

- [Заметки о протоданкшардинге(opens in a new tab)](https://notes.ethereum.org/@vbuterin/proto_danksharding_faq)
- [Видео о безбанковом данкшардинге(opens in a new tab)](https://www.youtube.com/watch?v=N5p0TB77flM)
- [Сборник по исследованию шардинга Ethereum(opens in a new tab)](https://notes.ethereum.org/@serenity/H1PGqDhpm?type=view)
- [Данкшардинг (Polynya)(opens in a new tab)](https://polynya.medium.com/danksharding-36dc0c8067fe)

#### [recent research 4 permalink](\#recent-research-4) Недавние исследования

- [EIP-4844: Протоданкшардинг(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-4844)
- [Виталик о шардинге и проверке доступности данных(opens in a new tab)](https://hackmd.io/@vbuterin/sharding_proposal)

### [hardware permalink](\#hardware) Оборудование

Возможность [запуска узлов](/ru/developers/docs/nodes-and-clients/run-a-node/) на слабом оборудовании критически важна для сохранения децентрализации Ethereum. Поэтому активно ведутся исследования, касающиеся снижения требований к оборудованию для запуска узлов.

#### [background reading 5 permalink](\#background-reading-5) Дополнительные материалы

- [Ethereum на ARM-архитектуре(opens in a new tab)](https://ethereum-on-arm-documentation.readthedocs.io/en/latest/)

#### [recent research 5 permalink](\#recent-research-5) Недавние исследования

- [ecdsa на FPGA(opens in a new tab)](https://ethresear.ch/t/does-ecdsa-on-fpga-solve-the-scaling-problem/6738)

## [security permalink](\#security) Безопасность

Безопасность — это обширная тема, которая включает предотвращение спама/мошенничества, безопасность кошельков, оборудования и криптоэкономическую безопасность, поиск ошибок, тестирование приложений и клиентского ПО, управление ключами. Расширение знаний в этих областях поможет стимулировать массовое внедрение.

### [cryptography  zkp permalink](\#cryptography--zkp) Криптография и ZKP

Доказательства с нулевым разглашением (ZKP) и криптография критически важны для обеспечения конфиденциальности и безопасности Ethereum и его приложений. Нулевое разглашение — относительно новое, но быстро развивающееся направление с массой возможностей для исследований и разработок. К ним относятся разработка более эффективной реализации [алгоритма хэширования Keccak(opens in a new tab)](https://hackmd.io/sK7v0lr8Txi1bgION1rRpw?view#Overview), поиск лучших по сравнению с существующими полиномиальных обязательств или же снижение стоимости генерации публичных ключей ECDSA и схем верификации подписей.

#### [background reading 6 permalink](\#background-reading-6) Дополнительные материалы

- [Блог 0xparc(opens in a new tab)](https://0xparc.org/blog)
- [zkp.science(opens in a new tab)](https://zkp.science/)
- [Подкаст о доказательствах с нулевым разглашением(opens in a new tab)](https://zeroknowledge.fm/)

#### [recent research 6 permalink](\#recent-research-6) Недавние исследования

- [Недавние успехи в криптографии эллиптических кривых(opens in a new tab)](https://ethresear.ch/t/the-ec-fft-algorithm-without-elliptic-curve-and-isogenies/11346)
- [Ethresear.ch ZK(opens in a new tab)](https://ethresear.ch/c/zk-s-nt-arks/13)

### [wallets permalink](\#wallets) Кошельки

Кошельки Ethereum могут быть расширениями для браузера, приложениями для компьютеров или мобильных устройств и даже смарт-контрактами в Ethereum. Активно ведутся исследования кошельков с возможностью социального восстановления, которые снижают риски, связанные с управлением ключами одним пользователем. С разработкой кошельков связано исследование альтернативных форм абстрагирования аккаунтов, что является важным направлением перспективных исследований.

#### [background reading 7 permalink](\#background-reading-7) Дополнительные материалы

- [Введение в кошельки](/ru/wallets/)
- [Введение в безопасность кошельков](/ru/security/)
- [ethresear.ch — Безопасность(opens in a new tab)](https://ethresear.ch/tag/security)
- [EIP-2938 Абстрагирование аккаунта(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-2938)
- [EIP-4337 Абстрагирование аккаунта(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-4337)

#### [recent research 7 permalink](\#recent-research-7) Недавние исследования

- [Смартконтрактные кошельки с валидацией(opens in a new tab)](https://ethereum-magicians.org/t/validation-focused-smart-contract-wallets/6603)
- [Будущее аккаунтов(opens in a new tab)](https://ethereum-magicians.org/t/validation-focused-smart-contract-wallets/6603)
- [EIP-3074 Операционные коды AUTH и AUTHCALL(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-3074)
- [Публикация кода по адресу EOA(opens in a new tab)](https://eips.ethereum.org/EIPS/eip-5003)

## [community education and outreach permalink](\#community-education-and-outreach) Сообщество, образование и охват

Знакомство новых пользователей с Ethereum требует новых образовательных ресурсов и способов охвата. Сюда могут входить публикации в блогах и статьи, книги, подкасты, мемы, образовательные ресурсы, мероприятия и все остальное, что помогает строить сообщества, приветствовать новичков и рассказывать людям об Ethereum.

### [uxui permalink](\#uxui) UX/UI

Чтобы сделать Ethereum доступнее для большего круга людей, экосистема нуждается в улучшении пользовательского опыта (UX) и интерфейса (UI). Это требует от дизайнеров и экспертов в области разработки продуктов пересмотреть текущий дизайн кошельков и приложений.

#### [background reading 8 permalink](\#background-reading-8) Дополнительные материалы

- [Ethresear.ch UX и UI(opens in a new tab)](https://ethresear.ch/c/ui-ux/24)

#### [recent research 8 permalink](\#recent-research-8) Недавние исследования

- [Дискорд-канал Web3 Design(opens in a new tab)](https://discord.gg/FsCFPMTSm9)
- [Принципы дизайна Web3(opens in a new tab)](https://www.web3designprinciples.com/)
- [Обсуждение UX от Ethereum Magicians(opens in a new tab)](https://ethereum-magicians.org/t/og-council-ux-follow-up/9032/3)

### [economics permalink](\#economics) Экономика

Экономические исследования Ethereum часто затрагивают два направления: валидация безопасности механизмов, отвечающих за экономическое поощрение ("микроэкономика") и анализ потоков ценности между протоколами, приложениями и пользователями ("макроэкономика"). Существуют сложные криптоэкономические факторы, касающиеся базовой валюты Ethereum (эфира) и токенов, построенных на его основе (например, NFT и ERC20).

#### [background reading 9 permalink](\#background-reading-9) Дополнительные материалы

- [Robust Incentives Group(opens in a new tab)](https://ethereum.github.io/rig/)
- [Секция ETHconomics на Devconnect(opens in a new tab)](https://www.youtube.com/playlist?list=PLTLjFJ0OQOj5PHRvA2snoOKt2udVsyXEm)

#### [recent research 9 permalink](\#recent-research-9) Недавние исследования

- [Эмпирический анализ EIP1559(opens in a new tab)](https://arxiv.org/abs/2201.05574)
- [Баланс объема предложения в обороте(opens in a new tab)](https://ethresear.ch/t/circulating-supply-equilibrium-for-ethereum-and-minimum-viable-issuance-during-the-proof-of-stake-era/10954)
- [Количественная оценка MEV: насколько темен лес(opens in a new tab)](https://arxiv.org/abs/2101.05511)

### [blockspace fee markets permalink](\#blockspace-fee-markets) Рынки блочного пространства и комиссий

Рынки блочного пространства регулируют включение транзакций конечных пользователей, непосредственно в Ethereum (уровень 1) или в мостовых сетях, например в свертках (уровень 2). В Ethereum транзакции отправляются на рынок комиссий, развернутый в протоколе EIP-1559, что защищает цепочку от спама и чрезмерного роста стоимости транзакций. На обоих уровнях транзакции могут порождать внешние эффекты, известные как максимальная извлекаемая ценность (MEV). Это привело к созданию новых рыночных структур для отслеживания таких эффектов и управления ими.

#### [background reading 10 permalink](\#background-reading-10) Дополнительные материалы

- [Дизайн механизма начисления комиссий за транзакции в блокчейне Ethereum: экономический анализ EIP-1559 (Тим Рафгарден, 2020 г.)(opens in a new tab)](https://timroughgarden.org/papers/eip1559.pdf)
- [Моделирование EIP-1559 (Robust Incentives Group)(opens in a new tab)](https://ethereum.github.io/abm1559)
- [Основы экономики свертков(opens in a new tab)](https://barnabe.substack.com/p/understanding-rollup-economics-from?utm_source=url)
- [Flash Boys 2.0: фронтраннинг, перестановка транзакций и нестабильность консенсуса на децентрализованных биржах(opens in a new tab)](https://arxiv.org/abs/1904.05234)

#### [recent research 10 permalink](\#recent-research-10) Недавние исследования

- [Видеопрезентация многомерного протокола EIP-1559(opens in a new tab)](https://youtu.be/QbR4MTgnCko)
- [Кроссдоменная MEV(opens in a new tab)](http://arxiv.org/abs/2112.01472)
- [Аукционы MEV(opens in a new tab)](https://ethresear.ch/t/mev-auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-extractable-value/6788)

### [proof of stake incentives permalink](\#proof-of-stake-incentives) Поощрения при использовании доказательства доли владения

Валидаторы используют нативный актив сети Ethereum (эфир) как залог на случай нечестного поведения. Криптоэкономика этого процесса определяет безопасность в сети. Опытные валидаторы могут попробовать злоупотребить особенностями на уровне поощрений для проведения атак.

#### [background reading 11 permalink](\#background-reading-11) Дополнительные материалы

- [Мастер-класс по экономике и экономической модели Ethereum(opens in a new tab)](https://github.com/CADLabs/ethereum-economic-model)
- [Моделирование поощрений при использовании PoS (Robust Incentives Group)(opens in a new tab)](https://ethereum.github.io/beaconrunner/)

#### [recent research 11 permalink](\#recent-research-11) Недавние исследования

- [Повышение стойкости к цензурированию транзакций за счет разделения тех, кто предлагает, и тех, кто создает (PSB)(opens in a new tab)](https://notes.ethereum.org/s3JToeApTx6CKLJt8AbhFQ)
- [Три атаки на Ethereum с доказательством доли владения(opens in a new tab)](https://arxiv.org/abs/2110.10086)

### [liquid staking and derivatives permalink](\#liquid-staking-and-derivatives) Ликвидный стейкинг и деривативы

Ликвидный стейкинг позволяет пользователям с балансом менее 32 ETH получать доход от стейкинга, обменивая эфир на токен, представляющий размещенный в стейкинге эфир. Этот токен также можно использовать в DeFi. Однако поощрения и динамика рынка, связанные с ликвидным стейкингом, все еще изучаются, как и их влияние на безопасность Ethereum (например, риски централизации).

#### [background reading 12 permalink](\#background-reading-12) Дополнительные материалы

- [Ликвидный стейкинг — Ethresear.ch(opens in a new tab)](https://ethresear.ch/search?q=liquid%20staking)
- [Lido: путь к стейкингу Ethereum, не требующему доверия(opens in a new tab)](https://blog.lido.fi/the-road-to-trustless-ethereum-staking/)
- [Rocket Pool: знакомство с протоколом стейкинга(opens in a new tab)](https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-1-8be4859e5fbd)

#### [recent research 12 permalink](\#recent-research-12) Недавние исследования

- [Как вывести средства из Lido(opens in a new tab)](https://ethresear.ch/t/handling-withdrawals-in-lidos-eth-liquid-staking-protocol/8873)
- [Реквизиты для вывода(opens in a new tab)](https://ethresear.ch/t/withdrawal-credential-rotation-from-bls-to-eth1/8722)
- [Риски деривативов ликвидного стейкинга(opens in a new tab)](https://notes.ethereum.org/@djrtwo/risks-of-lsd)

## [testing permalink](\#testing) Тестирование

### [formal verification permalink](\#formal-verification) Формальная верификация

Формальная верификация — это написание кода, проверяющего спецификации консенсуса Ethereum. Существует исполняемая версия спецификации, написанная на Python, которая требует обслуживания и разработки. Дальнейшие исследования помогут улучшить реализацию спецификации на языке Python и добавить инструменты, которые смогут более надежно проверять правильность и выявлять проблемы.

#### [background reading 13 permalink](\#background-reading-13) Дополнительные материалы

- [Введение в формальную верификацию(opens in a new tab)](https://ptolemy.berkeley.edu/projects/embedded/research/vis/doc/VisUser/vis_user/node4.html)
- [Формальная верификация (Intel)(opens in a new tab)](https://www.cl.cam.ac.uk/~jrh13/papers/mark10.pdf)

#### [recent research 13 permalink](\#recent-research-13) Недавние исследования

- [Формальная верификация контракта депозита(opens in a new tab)](https://github.com/runtimeverification/deposit-contract-verification)
- [Формальная верификация спецификации Beacon Chain(opens in a new tab)](https://github.com/runtimeverification/deposit-contract-verification)

## [data science and analytics permalink](\#data-science-and-analytics) Наука о данных и аналитика

Нужно больше инструментов для анализа и панелей, которые предоставят подробную информацию об активности и состоянии сети Ethereum.

### [background reading 14 permalink](\#background-reading-14) Дополнительные материалы

- [Dune Analytics(opens in a new tab)](https://dune.com/browse/dashboards)
- [Панель разнообразия клиентов(opens in a new tab)](https://clientdiversity.org/)

#### [recent research 14 permalink](\#recent-research-14) Недавние исследования

- [Анализ данных от Robust Incentives Group(opens in a new tab)](https://ethereum.github.io/rig/)

## [apps and tooling permalink](\#apps-and-tooling) Приложения и инструменты

Уровень приложений поддерживает разнообразную экосистему с программами, которые обрабатывают транзакции на основном уровне Ethereum. Команды разработчиков постоянно ищут новые способы создания компонуемых, не требующих разрешений и устойчивых к цензурированию версий важных приложений Web2 или совершенно новых концептов, нативных для Web3, используя Ethereum. В то же время разрабатываются новые инструменты. Они позволят строить децентрализованные приложения на Ethereum без лишних сложностей.

### [defi permalink](\#defi) DeFi

Децентрализованные финансы (DeFi) — это один из основных классов приложений, созданных на основе Ethereum. Целью DeFi является создание компонуемых "денежных лего", которые позволят пользователям хранить, передавать, давать взаймы, одалживать и инвестировать криптоактивы, используя смарт-контракты. DeFi — направление, которое быстро развивается и постоянно совершенствуется. Исследования в области безопасности, эффективности и доступности протоколов требуются постоянно.

#### [background reading 15 permalink](\#background-reading-15) Дополнительные материалы

- [DeFi](/ru/defi/)
- [Coinbase: Что такое DeFi?(opens in a new tab)](https://www.coinbase.com/learn/crypto-basics/what-is-defi)

#### [recent research 15 permalink](\#recent-research-15) Недавние исследования

- [Децентрализованные финансы, централизованное владение?(opens in a new tab)](https://arxiv.org/pdf/2012.09306.pdf)
- [Optimism: путь к транзакциям со стоимостью меньше доллара(opens in a new tab)](https://medium.com/ethereum-optimism/the-road-to-sub-dollar-transactions-part-2-compression-edition-6bb2890e3e92)

### [daos permalink](\#daos) DAO

Важнейший сценарий применения Ethereum — это возможность организовываться децентрализованным образом через DAO. Сейчас проводится много исследований, которые касаются разработки и использования DAO в Ethereum, чтобы применять усовершенствованные формы управления, в качестве инструмента для координации с минимумом доверия. Это значительно расширит возможности людей в сравнении с традиционными структурами корпораций и организаций.

#### [background reading 16 permalink](\#background-reading-16) Дополнительные материалы

- [Знакомство с DAO](/ru/dao/)
- [Dao Collective(opens in a new tab)](https://daocollective.xyz/)

#### [recent research 16 permalink](\#recent-research-16) Недавние исследования

- [Составление схемы экосистемы DAO(opens in a new tab)](https://www.researchgate.net/publication/358694594_Mapping_out_the_DAO_Ecosystem_and_Assessing_DAO_Autonomy)

### [developer tools permalink](\#developer-tools) Инструменты для разработчиков

Инструменты для разработчиков Ethereum стремительно улучшаются. В этой области предстоит провести много исследований и разработок.

#### [background reading 17 permalink](\#background-reading-17) Дополнительная литература

- [Инструменты для разных языков программирования](/ru/developers/docs/programming-languages/)
- [Фреймворки для разработчиков](/ru/developers/docs/frameworks/)
- [Список инструментов для разработчика консенсуса(opens in a new tab)](https://github.com/ConsenSys/ethereum-developer-tools-list)
- [Стандарты токенов](/ru/developers/docs/standards/tokens/)
- [CryptoDevHub: инструменты EVM(opens in a new tab)](https://cryptodevhub.io/wiki/ethereum-virtual-machine-tools)

#### [recent research 17 permalink](\#recent-research-17) Недавние исследования

- [Канал, посвященный инструментам консенсуса Eth R&D, в Discord(opens in a new tab)](https://discordapp.com/channels/595666850260713488/746343380900118528)

### [oracles permalink](\#oracles) Оракулы

Оракулы импортируют данные из офчейна в блокчейн децентрализованным и не требующим разрешений способом. Получение этих данных ончейн позволяет децентрализованным приложениям взаимодействовать с такими явлениями реального мира, как колебания цен реальных активов, события в офчейн-приложениях и даже перемены погоды.

#### [background reading 18 permalink](\#background-reading-18) Дополнительные материалы

- [Знакомство с оракулами](/ru/developers/docs/oracles/)

#### [recent research 18 permalink](\#recent-research-18) Недавние исследования

- [Обзор блокчейн-оракулов(opens in a new tab)](https://arxiv.org/pdf/2004.07140.pdf)
- [Документация Chainlink(opens in a new tab)](https://chain.link/whitepaper)

### [app security permalink](\#app-security) Безопасность приложений

Взломы в Ethereum обычно используют уязвимости в отдельных приложениях, а не в самом протоколе. Хакеры и разработчики приложений ведут гонку вооружений, разрабатывая новые средства атаки и защиты. Это означает, что всегда необходимо вести исследования и разработки для защиты приложений от взломов.

#### [background reading 19 permalink](\#background-reading-19) Дополнительные материалы

- [Отчет об эксплойте Wormhole(opens in a new tab)](https://blog.chainalysis.com/reports/wormhole-hack-february-2022/)
- [Анализ причин взломов контрактов Ethereum(opens in a new tab)](https://forum.openzeppelin.com/t/list-of-ethereum-smart-contracts-post-mortems/1191)
- [Новости Rekt(opens in a new tab)](https://twitter.com/RektHQ?s=20%5C&t=3otjYQdM9Bqk8k3n1a1Adg)

#### [recent research 19 permalink](\#recent-research-19) Недавние исследования

- [Приложения — ethresear.ch(opens in a new tab)](https://ethresear.ch/c/applications/18)

### [technology stack permalink](\#technology-stack) Технологический стек

Децентрализация всего технологического стека Ethereum — это важное направление исследований. Сейчас децентрализованные приложения в Ethereum частично централизованы, потому что зависят от централизованных инструментов или инфраструктуры.

#### [background reading 20 permalink](\#background-reading-20) Дополнительные материалы

- [Стек Ethereum](/ru/developers/docs/ethereum-stack/)
- [Coinbase: введение в стек Web3(opens in a new tab)](https://blog.coinbase.com/a-simple-guide-to-the-web3-stack-785240e557f0)
- [Знакомство со смарт-контрактами](/ru/developers/docs/smart-contracts/)
- [Введение в децентрализованное хранение](/ru/developers/docs/storage/)

#### [recent research 20 permalink](\#recent-research-20) Недавние исследования

- [Компонуемость смарт-контрактов](/ru/developers/docs/smart-contracts/composability/)