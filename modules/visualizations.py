import plotly.express as px

def rating_distribution(df):
    return px.histogram(
        df, x="rating", nbins=5,
        title="Rating Distribution", color="rating"
    )

def issue_category_chart(df):
    issues = df["issue_category"].value_counts().reset_index()
    issues.columns = ["issue_category", "count"]
    return px.bar(
        issues, x="issue_category", y="count",
        title="Issue Categories", text="count"
    )

def rating_trend(df):
    df["date"] = df["feedback_date"].dt.date
    trend = df.groupby("date")["rating"].mean().reset_index()
    return px.line(
        trend, x="date", y="rating",
        title="Rating Trend Over Time", markers=True
    )

def sentiment_pie(df):
    sent = df["sentiment"].value_counts().reset_index()
    sent.columns = ["sentiment", "count"]
    return px.pie(
        sent, names="sentiment", values="count",
        title="Sentiment Breakdown"
    )
