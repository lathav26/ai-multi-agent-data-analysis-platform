import pandas as pd

def analyze_data(df):

    analysis = {}

    analysis["Total Rows"] = df.shape[0]
    analysis["Total Columns"] = df.shape[1]

    numeric_cols = df.select_dtypes(include=["number"]).columns

    if len(numeric_cols) > 0:
        analysis["Average Values"] = df[numeric_cols].mean().to_dict()

    return analysis