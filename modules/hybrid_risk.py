def rating_risk_score(rating):
    rating = float(rating)
    if rating <= 2:
        return 1.0
    elif rating == 3:
        return 0.6
    elif rating >= 4:
        return 0.2
    return 0.5


def sentiment_risk_score(sentiment):
    if sentiment == "Negative":
        return 1.0
    elif sentiment == "Neutral":
        return 0.5
    return 0.1


def issue_severity_score(issue):
    issue = str(issue).lower()

    high = ["damaged", "wrong", "broken", "lost", "service", "complaint"]
    medium = ["delay", "timing", "late"]

    if any(w in issue for w in high):
        return 1.0
    elif any(w in issue for w in medium):
        return 0.6
    return 0.2


def recommendation_score(value):
    if str(value).lower() == "no":
        return 1.0
    return 0.2


def compute_hybrid_score(row):
    score = (
        0.4 * rating_risk_score(row["rating"])
        + 0.3 * sentiment_risk_score(row["sentiment"])
        + 0.2 * issue_severity_score(row["issue_category"])
        + 0.1 * recommendation_score(row.get("would_recommend", "Yes"))
    )
    return round(score, 2)


def bucket_hybrid_risk(score):
    if score >= 0.70:
        return "High Risk"
    elif score >= 0.40:
        return "Medium Risk"
    return "Low Risk"
