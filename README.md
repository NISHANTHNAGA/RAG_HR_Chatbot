# RAG_HR_Chatbot
Overview
This project is an HR chatbot that uses a (RAG) pipeline to answer HR-related queries.

## Features
- Ask HR policy questions through an API endpoint.
- Supports PDF and text document ingestion.
- Provides answers.

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd <directory>
```
2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Install dependencies
4. Set Environmental vriables
```
API_KEY=<your_api_key>
```
## Usage Instructions

1. Run the ingestion_1.py
  ```
python ingestion_1.py
```
2. Run the chatbot.py
 ```
python chatbot.py
```
3. Run app.py 
```
python app.py
```
4. Run ui.py
```
streamlit run ui.py
```
