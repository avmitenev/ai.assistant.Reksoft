import streamlit as st

st.title("Справка")

st.markdown(
"""
Это приложение представляет собой экспресс-прототип чат-бота-консультанта для клиентов, заинтересованных в получении дополнительной информации о Reksoft. Разработанное в течение трех дней, оно служит частичной и ограниченной демонстрацией возможностей больших языковых моделей (LLM), обогащенных контекстными знаниями о продуктах и услугах организации.

База знаний приложения была сформирована с использованием следующих источников:
* https://www.reksoft.ru
* https://www.reksoft.ru/reksoft-consulting
* https://www.reksoft.ru/services
* https://www.reksoft.ru/solutions
* https://www.reksoft.ru/industries

Чтобы обогатить базу знаний приложения, вы можете загрузить свои собственные файлы в следующих форматах:
* .txt
* .json
* .pdf

Пожалуйста, обратите внимание, что загружать можно только общедоступную информацию, поскольку это приложение также является общедоступным.
Чтобы загрузить свои документы, перейдите на вкладку "Загрузить данные", расположенную в левой колонке. Перетащите файл в блок загрузки данных или выберите его в проводнике, нажав кнопку "Browse files". Как только файл будет загружен, подтвердите его добавление в общую базу документов, нажав кнопку "Подтвердить".

В дополнение к базе знаний, бот также использует историю чата во время разговоров. Это позволяет боту задавать уточняющие вопросы, не требуя от пользователя повторения всего контекста. Стоит отметить, что по той же причине важно очистить историю чата, чтобы восстановить контекст при смене тем. Вы можете сделать это, нажав кнопку "Сбросить историю" в конце чата.
"""
)
