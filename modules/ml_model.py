from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train_sentiment_model(df):
    df = df.copy()

    df["label"] = df["sentiment"].replace({
        "Positive": 1,
        "Neutral": 0,
        "Negative": 0
    })

    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(df["feedback"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return model, vectorizer, accuracy, report


def ml_predict(text, model, vectorizer):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    return "Positive" if pred == 1 else "Negative"
