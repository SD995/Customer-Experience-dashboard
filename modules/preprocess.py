import pandas as pd
from modules.utils import risk_bucket
from modules.analysis import vader_sentiment_label
from modules.hybrid_risk import compute_hybrid_score, bucket_hybrid_risk

def preprocess_data(df):
    df = df.copy()

    df.columns = [c.lower().strip() for c in df.columns]

    # Detect feedback column
    if "feedback" in df.columns:
        df["feedback"] = df["feedback"].astype(str)
    elif "feedback_text" in df.columns:
        df["feedback"] = df["feedback_text"].astype(str)
    elif "comment" in df.columns:
        df["feedback"] = df["comment"].astype(str)
    else:
        raise ValueError("CSV missing feedback or feedback_text column")

    if "rating" not in df.columns:
        raise ValueError("CSV missing rating column")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0)

    if "issue_category" not in df.columns:
        df["issue_category"] = "Unknown"

    if "feedback_date" in df.columns:
        df["feedback_date"] = pd.to_datetime(df["feedback_date"], errors="coerce")
    else:
        df["feedback_date"] = pd.NaT

    df["risk"] = df["rating"].apply(risk_bucket)
    df["sentiment"] = df["feedback"].apply(vader_sentiment_label)

    # Hybrid risk
    df["hybrid_risk_score"] = df.apply(compute_hybrid_score, axis=1)
    df["hybrid_risk"] = df["hybrid_risk_score"].apply(bucket_hybrid_risk)

    return df
