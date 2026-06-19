from pathlib import Path

import pandas as pd


def summarize_file(file_path: str) -> str:

    extension = Path(file_path).suffix.lower()

    if extension == ".csv":

        df = pd.read_csv(file_path)

    elif extension == ".xlsx":

        df = pd.read_excel(file_path)

    else:

        raise ValueError("Unsupported file type")

    summary = []

    summary.append(f"Rows: {len(df)}")

    summary.append(f"Columns: {', '.join(df.columns)}")

    summary.append(f"Data Types:\n{df.dtypes}")

    summary.append(f"Sample Data:\n{df.head().to_string()}")

    return "\n\n".join(summary)
