import pandas as pd

def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing text values
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].fillna("Unknown")

    return df