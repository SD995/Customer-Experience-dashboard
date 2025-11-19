import pandas as pd

def load_default_data():
    """
    Loads NexGen's provided default dataset.
    """
    try:
        df = pd.read_csv("data/customer_feedback.csv")
        return df
    except:
        raise FileNotFoundError("Default dataset not found in /data folder.")


def load_uploaded_file(uploaded_file):
    """
    Load user-uploaded CSV file.
    """
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except:
        raise Exception("Invalid CSV file. Please upload a valid CSV.")
