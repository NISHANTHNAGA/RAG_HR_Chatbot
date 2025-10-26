from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from functools import lru_cache
import os
from dotenv import load_dotenv
load_dotenv()

DB_FAISS_PATH = "faiss_index"

@lru_cache(maxsize=50)
def query_cache(question):
    return question

def build_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="Answer the HR policy-related question using the context below.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )
    return chain

def chat():
    chain = build_rag_chain()
    print("HR Policy Chatbot ready! Type 'exit' to quit.")

    while True:
        q = input("\nYou: ")
        if q.lower() == "exit":
            break
        if query_cache(q):
            result = chain({"query": q})
            print("\n🤖 Answer:", result["result"])
            print("\n📄 Source:", [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]])

if __name__ == "__main__":
    chat()
