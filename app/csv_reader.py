import pandas as pd


def analyze_csv(file_path: str) -> tuple[int, list[str]]:

    df = pd.read_csv(file_path)

    return (len(df), list(df.columns))
