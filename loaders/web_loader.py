from langchain_community.document_loaders import WebBaseLoader


def load_urls(urls):
    documents = []

    for url in urls:
        loader = WebBaseLoader(url)
        docs = loader.load()
        documents.extend(docs)

    return documents 