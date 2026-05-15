# Vision Language Model (VLM) Agent System Architecture

# High-Level Workflow

```text
User Uploads Image + Question
                │
                ▼
        Streamlit Frontend
                │
                ▼
          FastAPI Backend
                │
                ▼
          Image Processing
                │
                ▼
      Vision Language Model
    (Hugging Face Inference API)
                │
                ▼
         Reasoning Agent
                │
                ▼
        Summarization Agent
                │
                ▼
          MLflow Logging
                │
                ▼
         Final Response
                │
                ▼
         Streamlit Display
```

---

# Component Overview

## Streamlit Frontend

Responsible for:
- Image uploads
- User question input
- Displaying AI-generated responses

---

## FastAPI Backend

Responsible for:
- API orchestration
- File handling
- Agent execution pipeline
- Response management

---

## Vision Language Model (VLM)

Model Used:
- Qwen2.5-VL-72B-Instruct

Responsibilities:
- Image understanding
- Multimodal reasoning
- Visual-text contextual analysis

Inference:
- Hugging Face Inference API

---

## Reasoning Agent

Responsible for:
- Context reasoning
- Intermediate response refinement
- Agent orchestration logic

---

## Summarizer Agent

Responsible for:
- Compressing responses
- Improving readability
- Generating concise outputs

---

## Image Tool

Responsible for:
- Image loading
- Metadata extraction
- Basic preprocessing

---

## Logging Tool

Responsible for:
- MLflow parameter logging
- Response logging
- Experiment tracking

---

# MLflow Observability

Tracked Information:
- Uploaded image names
- User questions
- Generated responses
- Execution runs

Benefits:
- Experiment tracking
- Pipeline observability
- Monitoring and debugging

---

# Advantages of Architecture

- Modular design
- Cloud-native inference
- Lightweight execution
- No local GPU dependency
- Scalable agent workflows
- Production-style AI engineering structure

---

# Future Scalability

The architecture can be extended with:

- LangGraph workflows
- Multi-agent systems
- Vector databases
- RAG pipelines
- Memory systems
- Real-time streaming
- Autonomous agent orchestration

---

# Deployment Possibilities

- Hugging Face Spaces
- Render
- Railway
- AWS
- Azure
- GCP
- Docker + Kubernetes

---

# System Characteristics

| Property | Value |
|---|---|
| Architecture Style | Modular AI System |
| Inference Type | Cloud-based |
| Model Category | Vision Language Model |
| Frontend | Streamlit |
| Backend | FastAPI |
| Observability | MLflow |
| GPU Requirement | None |
| Deployment Ready | Yes |
