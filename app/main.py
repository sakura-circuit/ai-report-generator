from app import config

from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import FastAPI, File, UploadFile, HTTPException


from app.models import ReportResponse

from app.ai_reporter import generate_report

from app.file_reader import summarize_file

app = FastAPI()


@app.post("/analyze", response_model=ReportResponse)
async def analyze_file(
    file: UploadFile = File(...),
):

    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is missing")

    suffix = Path(file.filename).suffix

    with NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:

        temp_file.write(await file.read())

        csv_path = temp_file.name

    try:

        dataset_summary = summarize_file(csv_path)

        report = generate_report(dataset_summary)

        return ReportResponse(**report)

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    finally:

        Path(csv_path).unlink(missing_ok=True)
