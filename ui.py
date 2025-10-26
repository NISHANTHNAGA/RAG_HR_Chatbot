import streamlit as st
import requests

st.set_page_config(page_title="RAG HR Chatbot", layout="centered")
st.title("HR Policy RAG Chatbot")

API_URL = "http://localhost:5000/query"

user_input = st.text_input("Ask a question about the HR Policy:")
if user_input:
    with st.spinner("Fetching answer..."):
        response = requests.post(API_URL, json={"question": user_input})
        if response.status_code == 200:
            data = response.json()
            st.success(data["answer"])
        else:
            st.error("Error: Could not connect to backend API.")
