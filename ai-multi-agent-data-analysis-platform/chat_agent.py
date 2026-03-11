import pandas as pd

def ask_question(df, question):

    question = question.lower()
    responses = []

    if "rows" in question:
        responses.append(f"The dataset has {df.shape[0]} rows.")

    if "columns" in question:
        responses.append(f"The dataset has {df.shape[1]} columns.")

    if "average" in question:
        numeric_cols = df.select_dtypes(include=["number"]).columns
        responses.append("Average values:\n" + df[numeric_cols].mean().to_string())

    if "summary" in question:
        responses.append("Summary:\n" + df.describe().to_string())

    if not responses:
        return "Sorry, I cannot answer that yet."

    return "\n\n".join(responses)