import os
from typing import List, Iterable, Any

from dotenv import load_dotenv
from langchain.memory import ChatMessageHistory
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables.history import RunnableWithMessageHistory

from basic_chain import get_model
from rag_chain import make_rag_chain
import logging

store = {}

import json

def create_memory_chain(llm, base_chain, contextualize_q_prompt):
    runnable = contextualize_q_prompt | llm | base_chain

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()

        return store[session_id]

    with_message_history = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="question",
        history_messages_key="chat_history",
    )
    return with_message_history

def clean_session_history(session_id):
    global store
    store[session_id] = ChatMessageHistory()


class SimpleTextRetriever(BaseRetriever):
    docs: List[Document]
    """Documents."""

    @classmethod
    def from_texts(
            cls,
            texts: Iterable[str],
            **kwargs: Any,
    ):
        docs = [Document(page_content=t) for t in texts]
        return cls(docs=docs, **kwargs)

    def _get_relevant_documents(
            self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return self.docs


def main():
    load_dotenv()
    model = get_model("ChatGPT")
    chat_memory = ChatMessageHistory()

    system_prompt = "You are a helpful AI assistant for busy professionals trying to improve their health."
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )

    text_path = "examples/standard_chartered_faq.txt"  # Updated path
    text = open(text_path, "r").read()
    retriever = SimpleTextRetriever.from_texts([text])
    rag_chain = make_rag_chain(model, retriever, rag_prompt=None)
    chain = create_memory_chain(model, rag_chain, chat_memory) | StrOutputParser()
    queries = [
        "What do I need to get from the grocery store besides milk?",
        "Which of these items can I find at a farmer's market?",
    ]

    for query in queries:
        print(f"\nQuestion: {query}")
        response = chain.invoke(
            {"question": query},
            config={"configurable": {"session_id": "foo"}}
        )
        print(f"Answer: {response}")


if __name__ == "__main__":
    # this is to quite parallel tokenizers warning.
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    main()