from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

# docs = loader.load()
docs = loader.lazy_load()

# print(len(docs))

# print(docs[80].page_content)
# print(docs[80].metadata)

for document in docs:
    # print(document.page_content)
    print(document.metadata)
    print("\n")