from pydantic import BaseModel


class ReportResponse(BaseModel):
    rows: int
    columns: list[str]
