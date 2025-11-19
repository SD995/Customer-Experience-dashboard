import streamlit as st
import pandas as pd

from modules.data_loader import load_default_data, load_uploaded_file
from modules.preprocess import preprocess_data
from modules.visualizations import (
    rating_distribution, issue_category_chart,
    rating_trend, sentiment_pie
)
from modules.analysis import top_words
from modules.ml_model import train_sentiment_model, ml_predict

st.set_page_config(page_title="Customer Experience Dashboard", layout="wide")
st.title("Customer Experience Dashboard — NexGen Logistics")

# ------------------------------------------------------------
# 1. Dataset Selection
# ------------------------------------------------------------
uploaded = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded:
    df = load_uploaded_file(uploaded)
    st.success("Using uploaded dataset.")
else:
    df = load_default_data()
    st.info("Using default dataset (customer_feedback.csv).")

# ------------------------------------------------------------
# 2. Preprocess Data
# ------------------------------------------------------------
df = preprocess_data(df)

# ------------------------------------------------------------
# 3. Train ML Model
# ------------------------------------------------------------
model, vectorizer, accuracy, report = train_sentiment_model(df)
df["ml_sentiment"] = df["feedback"].apply(lambda x: ml_predict(x, model, vectorizer))

# ------------------------------------------------------------
# 4. KPIs
# ------------------------------------------------------------
st.subheader("Key Metrics")
c1, c2, c3 = st.columns(3)
c1.metric("Average Rating", round(df["rating"].mean(), 2))
c2.metric("Total Feedback", len(df))
c3.metric("High Risk %", f"{round((df['hybrid_risk']=='High Risk').mean()*100,1)}%")

st.markdown("---")

# ------------------------------------------------------------
# 5. ML Performance
# ------------------------------------------------------------
st.subheader("ML Sentiment Model Performance")
colA, colB = st.columns([1, 2])
colA.metric("Accuracy", f"{accuracy*100:.2f}%")

with colB.expander("Classification Report"):
    st.text(report)

st.markdown("---")

# ------------------------------------------------------------
# 6. Visualizations
# ------------------------------------------------------------
col1, col2 = st.columns(2)
col1.plotly_chart(rating_distribution(df), use_container_width=True)
col2.plotly_chart(issue_category_chart(df), use_container_width=True)

col3, col4 = st.columns(2)
col3.plotly_chart(rating_trend(df), use_container_width=True)
col4.plotly_chart(sentiment_pie(df), use_container_width=True)

st.markdown("---")

# ------------------------------------------------------------
# 7. Hybrid Risk Table
# ------------------------------------------------------------
st.subheader("Hybrid Risk Scoring (Advanced)")
st.dataframe(df[["rating","sentiment","issue_category","hybrid_risk_score","hybrid_risk"]])

st.markdown("---")

# ------------------------------------------------------------
# 8. Top Words
# ------------------------------------------------------------
st.subheader("Top Words in Feedback")
top_n = st.slider("Number of words", 5, 50, 15)
words = top_words(df["feedback"], top_n)
st.write(pd.DataFrame(words, columns=["word","count"]))

st.markdown("---")

# ------------------------------------------------------------
# 9. Final Data Table
# ------------------------------------------------------------
st.subheader("Complete Feedback Data")
st.dataframe(df)
