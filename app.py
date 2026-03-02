import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Kraljic Matrix Dashboard", layout="wide")

st.title("📊 Procurement Strategy - Kraljic Matrix Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload Procurement Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Sidebar threshold sliders
    st.sidebar.header("Set Threshold Values")

    risk_threshold = st.sidebar.slider(
        "Supply Risk Threshold",
        float(df["Supply Risk"].min()),
        float(df["Supply Risk"].max()),
        float(df["Supply Risk"].mean())
    )

    impact_threshold = st.sidebar.slider(
        "Profit Impact Threshold",
        float(df["Profit Impact"].min()),
        float(df["Profit Impact"].max()),
        float(df["Profit Impact"].mean())
    )

    # Kraljic Classification
    def classify(row):
        if row["Supply Risk"] < risk_threshold and row["Profit Impact"] < impact_threshold:
            return "Non-Critical"
        elif row["Supply Risk"] < risk_threshold and row["Profit Impact"] >= impact_threshold:
            return "Leverage"
        elif row["Supply Risk"] >= risk_threshold and row["Profit Impact"] < impact_threshold:
            return "Bottleneck"
        else:
            return "Strategic"

    df["Category"] = df.apply(classify, axis=1)

    st.subheader("Category Distribution")
    st.write(df["Category"].value_counts())

    # Plot
    st.subheader("Kraljic Matrix Visualization")

    fig, ax = plt.subplots(figsize=(8,6))

    sns.scatterplot(
        data=df,
        x="Supply Risk",
        y="Profit Impact",
        hue="Category",
        palette="Set1",
        ax=ax
    )

    ax.axvline(risk_threshold, color="black", linestyle="--")
    ax.axhline(impact_threshold, color="black", linestyle="--")

    ax.set_title("Kraljic Matrix")

    st.pyplot(fig)

else:
    st.info("Please upload your CSV dataset to continue.")
