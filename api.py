from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import mlflow

from agents.vlm_agent import vlm_agent

from tools.logging_tool import (
    log_question,
    log_response,
    log_image
)

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# MLflow local tracking
mlflow.set_tracking_uri(
    "file:./mlruns"
)

mlflow.set_experiment(
    "VLM Agent System"
)

@app.post("/analyze")

async def analyze_image(
    file: UploadFile = File(...),
    question: str = Form(...)
):

    image_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(image_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    with mlflow.start_run():

        log_question(question)

        log_image(file.filename)

        response = vlm_agent(
            image_path,
            question
        )

        log_response(response)

    return {
        "question": question,
        "image": file.filename,
        "response": response
    }