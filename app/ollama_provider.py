import os

from ollama import chat

from app.json_utils import extract_json

from app.prompt_builder import build_prompt

MODEL_NAME = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")


def generate_report(dataset_summary: str) -> dict:

    prompt = build_prompt(dataset_summary)

    response = chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])

    content = response["message"]["content"]

    return extract_json(content)
