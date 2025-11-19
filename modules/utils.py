def risk_bucket(rating):
    """
    Categorizes rating into risk levels.
    """
    try:
        r = float(rating)
    except:
        return "Unknown"

    if r <= 2:
        return "High Risk"
    elif r == 3:
        return "Medium Risk"
    elif r >= 4:
        return "Low Risk"
    else:
        return "Unknown"
