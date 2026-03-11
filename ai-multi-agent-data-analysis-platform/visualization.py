import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):

    plots = []

    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols[:3]:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        plots.append(fig)

    return plots