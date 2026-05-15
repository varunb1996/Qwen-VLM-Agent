# Vision Language Model (VLM) Agent System

## Overview

This project is a cloud-native Vision Language Model (VLM) Agent System built using FastAPI, Streamlit, Hugging Face Inference API, MLflow, and modular AI agents for multimodal reasoning over images and text.

The system allows users to upload images and ask natural language questions about them. The uploaded image is processed using a Vision Language Model, followed by reasoning and summarization agents to generate intelligent contextual responses.

The project follows a modular AI engineering architecture suitable for scalable multimodal AI workflows.

---

# Features

- Vision Language Model (VLM) integration
- Image upload and multimodal reasoning
- FastAPI backend orchestration
- Streamlit frontend UI
- Hugging Face cloud inference
- MLflow observability and logging
- Modular agent architecture
- Lightweight cloud-native workflow
- No local GPU inference required

---

# Tech Stack

## Backend
- FastAPI
- Python

## Frontend
- Streamlit

## AI/ML
- Hugging Face Inference API
- Qwen2-VL-7B-Instruct
- MLflow

## Utilities
- Pillow
- dotenv

---

# Project Structure

```text
vlm-agent-system/
│
├── agents/
│   ├── reasoning_agent.py
│   ├── summarizer_agent.py
│   └── vlm_agent.py
│
├── tools/
│   ├── image_tool.py
│   ├── logging_tool.py
│   └── openrouter_vlm_tool.py
│
├── utils/
│   └── config.py
│
├── uploads/
│   └── .gitkeep
│
├── mlruns/
│
├── app.py
├── api.py
├── requirements.txt
├── README.md
├── architecture.md
├── .env
└── .gitignore
```

---

# Execution Steps

## 1. Create Virtual Environment

```bash
python -m venv venv
```

---

## 2. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`

```env
HF_TOKEN=your_huggingface_token
```

---

## 5. Run FastAPI Backend

```bash
uvicorn api:app --reload
```

---

## 6. Run Streamlit Frontend

```bash
streamlit run app.py
```

---

## 7. Run MLflow UI

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

---

# Example Use Cases

- Image understanding
- Dashboard interpretation
- Architecture reasoning
- Diagram explanation
- Visual summarization
- Tactical image analysis
- OCR-style multimodal reasoning

---

# Future Improvements

- LangGraph workflows
- Multi-agent orchestration
- RAG-based multimodal retrieval
- Vector database integration
- Vision memory systems
- Real-time streaming inference
- Multimodal conversational agents

---

# Author

Varun Bukka
