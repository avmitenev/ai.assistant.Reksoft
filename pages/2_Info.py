import streamlit as st

st.title("Info")

st.markdown(
"""
This application is an express prototype of a chatbot consultant for clients interested in learning more about Reksoft. Developed within a span of three days, it serves as a partial and limited demonstration of the capabilities of Large Language Models (LLMs) enriched with contextual knowledge about the financial organization's products and services.

The application's knowledge base was formed using the following sources:
* https://www.reksoft.ru
* https://www.reksoft.ru/reksoft-consulting
* https://www.reksoft.ru/services
* https://www.reksoft.ru/solutions
* https://www.reksoft.ru/industries

To further enrich the application's knowledge base, you can upload your own files in the following formats:
* .txt
* .json
* .pdf

Please note that only publicly available information can be uploaded, as this application is also publicly accessible.
To upload your documents, navigate to the 'Upload data' tab located in the left-hand column. Either drag and drop the file into the data upload block or select it through the file explorer by clicking the 'Browse files' button. Once the file is uploaded, confirm its addition to the shared document base by clicking the 'Submit' button.

In addition to the knowledge base, the bot also relies on the chat history during conversations. This enables the bot to ask clarifying questions without requiring the user to reiterate the entire context. It's worth noting that, for the same reason, it's essential to clear the chat history to reset the context when changing topics. You can do this by clicking the 'Reset history' button at the end of the chat.
"""
)