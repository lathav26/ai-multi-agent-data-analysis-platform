import streamlit as st
import pandas as pd
from data_cleaning import clean_data
from analysis import analyze_data
from visualization import create_visualizations
from automl import run_automl
from chat_agent import ask_question

st.title("AI Multi-Agent Data Analysis Platform")

st.write("Upload a dataset to analyze")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:

    df = pd.read_csv(file, encoding="latin1")

    st.subheader("Original Dataset")
    st.dataframe(df.head())

    # Data Cleaning Agent
    if st.button("Run Data Cleaning Agent"):

        cleaned_df = clean_data(df)

        st.subheader("Cleaned Dataset")
        st.dataframe(cleaned_df.head())

        st.success("Data Cleaning Agent completed successfully")

    # Data Analysis Agent
    if st.button("Run Data Analysis Agent"):

        results = analyze_data(df)

        st.subheader("Data Analysis Results")

        for key, value in results.items():
            st.write(key, ":", value)

    # Visualization Agent
    if st.button("Run Visualization Agent"):

        plots = create_visualizations(df)

        st.subheader("Generated Visualizations")

        for fig in plots:
            st.pyplot(fig)

    # AutoML Agent
    if st.button("Run AutoML Agent"):

        automl_results = run_automl(df)

        st.subheader("AutoML Results")

        st.write(automl_results)

    # ---------------------------
    # AI Data Chat Agent
    # ---------------------------

    st.subheader("AI Data Chat Agent")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input("Ask a question about your dataset")

    if st.button("Ask AI Agent") and question:

        answer = ask_question(df, question)

        st.session_state.chat_history.append(("You", question))
        st.session_state.chat_history.append(("AI", answer))

    for sender, message in st.session_state.chat_history:
        st.write(f"**{sender}:** {message}")