def build_prompt(dataset_summary: str) -> str:

    return f"""
You are a business analyst.

Analyze the dataset summary.

Provide:

- Executive summary
- Key insights
- Recommendations

Return ONLY valid JSON.

Schema:

{{
    "summary": "",
    "insights": [],
    "recommendations": []
}}

Dataset Summary:

{dataset_summary}
"""
