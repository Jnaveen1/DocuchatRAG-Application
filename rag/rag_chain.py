from rag.retriever import retrieve_context
from rag.chat_model import get_llm


def ask_question(user_query, vector_store):

    context, source_docs = retrieve_context(
        user_query,
        vector_store,
        k=4
    )

    prompt = f"""
        You are a technical AI assistant.

        Answer the user's question using the provided context.

        Provide:
        1. A clear explanation
        2. Important points in bullet form
        3. Examples when available

        Context:
        {context}

        Question:
        {user_query}
        """

    model = get_llm()


    response = model.invoke(prompt)

    return {
        "answer": response.content,
        "source_documents": source_docs
    }