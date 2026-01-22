# Analytics Insight API

Analytics Insight is a FastAPI-based analytics and AI-powered insight generation service.  
It analyzes structured data using an LLM and returns actionable insights in JSON format.

---

## 🚀 Features

- FastAPI backend
- AI-powered data analysis using Groq LLM
- Simple `/analyze` endpoint
- JSON-based structured output
- Deployed on Render
- Dependency management with `uv`

---

## 🛠 Tech Stack

- **Python 3.13**
- **FastAPI**
- **LangChain**
- **Groq LLM**
- **uv**
- **SQLAlchemy**
- **MySQL**
- **Render (Deployment)**

---

## 📁 Project Structure

.
├── fastapi_v1.py # FastAPI application
├── database/
│ └── db_fetch.py # Data source
├── ai_utils/
│ └── analyzer_prompt.py
├── pyproject.toml
├── uv.lock
└── README.md


---

## ⚙️ Environment Variables

Create a `.env` file locally or set variables in Render:

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=your_database_url



## ▶️ Run Locally
pip install uv
uv sync
uv run uvicorn fastapi_v1:app --reload

Open:

http://127.0.0.1:8000/docs


##🔍 API Usage
Analyze Endpoint

POST /analyze

This endpoint accepts a single query parameter.

Query Parameter

question (string) – The analysis question

Example (cURL)
curl -X POST "http://127.0.0.1:8000/analyze?question=Analyze%20last%207%20days%20revenue"

Example (Python)
import requests

url = "http://127.0.0.1:8000/analyze"
params = {
    "question": "Analyze last 7 days revenue"
}

response = requests.post(url, params=params)
print(response.json())

##📖 API Documentation

FastAPI automatically generates interactive documentation:

/docs

##📌 Notes

The /analyze endpoint expects query parameters, not JSON body

Make sure environment variables are correctly set in production

## ❓ Why This Project?

This project was built to explore how Large Language Models (LLMs) can be combined with structured analytical data to generate meaningful, human-readable insights.

Traditional dashboards and charts are powerful, but they often require manual interpretation.  
The goal of **Analytics Insight API** is to bridge this gap by allowing users to ask natural language questions and receive structured, actionable insights directly from their data.

Key motivations behind this project:

- To experiment with **LLM-driven analytics** rather than plain text generation
- To design a **lightweight, API-first analytics service**
- To integrate **real structured data** with prompt-driven reasoning
- To build a production-ready FastAPI service deployable on cloud platforms
- To gain hands-on experience with **modern Python tooling** such as `uv`, LangChain, and Render

This project can serve as a foundation for:
- Analytics copilots
- BI assistant tools
- AI-powered dashboards
- Data-driven decision support systems

---

Built as a practical learning project with real-world deployment in mind.
