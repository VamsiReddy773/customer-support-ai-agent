import os

from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

documents = []

docs_folder = "docs"

for filename in os.listdir(docs_folder):
    if filename.endswith(".md"):
        filepath = os.path.join(docs_folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        documents.append(
            Document(
                page_content=text,
                metadata={"source": filename}
            )
        )

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)

def get_retriever():
    return retriever