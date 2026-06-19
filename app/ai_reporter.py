import os

from app.gemini_provider import generate_report as gemini_report

from app.ollama_provider import generate_report as ollama_report


def generate_report(dataset_summary: str) -> dict:

    provider = os.getenv("AI_PROVIDER", "gemini")

    if provider == "gemini":
        return gemini_report(dataset_summary)

    if provider == "ollama":
        return ollama_report(dataset_summary)

    raise ValueError(f"Unknown provider: {provider}")
