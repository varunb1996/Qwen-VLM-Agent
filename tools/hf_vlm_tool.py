import base64
import os

from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

MODEL_NAME = "Qwen/Qwen2.5-VL-72B-Instruct"

def analyze_image(image_path, question):

    with open(image_path, "rb") as image_file:

        image_bytes = image_file.read()

        image_base64 = base64.b64encode(
            image_bytes
        ).decode("utf-8")

    prompt = f"""
    Answer this question about the image:

    {question}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content