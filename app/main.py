from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, File, UploadFile

from app.csv_reader import analyze_csv
from app.models import ReportResponse

app = FastAPI()


@app.post("/analyze", response_model=ReportResponse)
async def analyze_file(
    file: UploadFile = File(...),
):

    with NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:

        temp_file.write(await file.read())

        csv_path = temp_file.name

    try:

        rows, columns = analyze_csv(csv_path)

        return ReportResponse(rows=rows, columns=columns)

    finally:

        Path(csv_path).unlink(missing_ok=True)
