import os

from google import genai

from google.genai.errors import ServerError

from app.json_utils import extract_json

from app.prompt_builder import build_prompt

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_report(dataset_summary: str) -> dict:

    try:

        prompt = build_prompt(dataset_summary)

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )

        if not response.text:
            raise ValueError("Empty Gemini response")

        return extract_json(response.text)

    except ServerError:

        raise ValueError("Gemini service temporarily unavailable. Please try again.")
