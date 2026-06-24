def retrieve_context(query, vector_store, k=4):

    retrieved_docs = vector_store.similarity_search(
        query,
        k=k
    )

    context = ""

    for doc in retrieved_docs:
        context += f"Source: {doc.metadata.get('source', 'Unknown')}\n"
        context += f"Content: {doc.page_content}\n\n"

    return context, retrieved_docs