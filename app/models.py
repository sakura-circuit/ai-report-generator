from pydantic import BaseModel


class ReportResponse(BaseModel):
    summary: str
    insights: list[str]
    recommendations: list[str]
