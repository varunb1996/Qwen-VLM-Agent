import mlflow


def log_question(question):

    mlflow.log_param(
        "question",
        question
    )


def log_response(response):

    mlflow.log_text(
        response,
        "response.txt"
    )


def log_image(image_name):

    mlflow.log_param(
        "image_name",
        image_name
    )