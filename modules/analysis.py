import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import re
from collections import Counter

# Downloads
nltk.download("vader_lexicon")
nltk.download("stopwords")

sia = SentimentIntensityAnalyzer()
STOP = set(stopwords.words("english"))

def vader_sentiment_label(text):
    """
    Returns Positive / Neutral / Negative using VADER.
    """
    if not isinstance(text, str):
        text = str(text)

    score = sia.polarity_scores(text)
    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


def top_words(series, n=20):
    """
    Extracts the top frequent meaningful words.
    """
    text = " ".join(series.dropna().astype(str).tolist()).lower()
    words = re.findall(r"\b[a-z]{2,}\b", text)
    filtered = [w for w in words if w not in STOP]
    return Counter(filtered).most_common(n)
