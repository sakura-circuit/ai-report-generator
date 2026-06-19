import json
import re


def extract_json(content: str) -> dict:

    match = re.search(r"\{.*\}", content, re.DOTALL)

    if not match:
        raise ValueError(f"No JSON found:\n{content}")

    return json.loads(match.group(0))
