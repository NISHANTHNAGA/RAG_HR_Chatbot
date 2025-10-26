import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "HR-Policy (1).pdf"
DB_FAISS_PATH = "faiss_index"




def create_vector_db():
    pdf_path = os.path.join(DATA_PATH)
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = FAISS.from_documents(splits, embeddings)
    db.save_local(DB_FAISS_PATH)
    print("✅ FAISS index created and saved at:", DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()
