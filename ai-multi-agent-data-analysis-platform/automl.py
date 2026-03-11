from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np


def run_automl(df):
    
    # Remove unwanted columns like Unnamed
    df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]

    # Select numeric columns
    numeric_df = df.select_dtypes(include=["number"]).copy()

    if numeric_df.empty:
        return "No numeric columns available for AutoML."

    

    # Replace infinite values
    numeric_df = numeric_df.replace([np.inf, -np.inf], np.nan)

    # Fill NaN values with column mean
    numeric_df = numeric_df.fillna(numeric_df.mean())

    # If dataset still too small
    if numeric_df.shape[0] < 2:
        return "Not enough rows to train a model."

    # Use last numeric column as target
    target = numeric_df.columns[-1]

    X = numeric_df.drop(columns=[target])
    y = numeric_df[target]

    # Final safety check
    X = X.fillna(0)
    y = y.fillna(0)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor()
    }

    results = {}

    for name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        score = r2_score(y_test, predictions)

        results[name] = round(score, 3)

    best_model = max(results, key=results.get)

    return {
        "Target Column": target,
        "Model Scores": results,
        "Best Model": best_model
    }