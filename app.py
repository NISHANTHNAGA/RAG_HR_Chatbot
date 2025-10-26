from flask import Flask, request, jsonify
from chatbot import build_rag_chain

app = Flask(__name__)
qa_chain = build_rag_chain()

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    question = data.get("question", "")
    result = qa_chain({"query": question})
    return jsonify({
        "answer": result["result"],
        "sources": [doc.metadata.get("source", "N/A") for doc in result["source_documents"]]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
