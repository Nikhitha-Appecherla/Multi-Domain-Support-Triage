def should_escalate(query):
    query = query.lower()

    # ONLY TRUE FRAUD / SECURITY RISKS
    risky_keywords = [
        "unauthorized",
        "fraud",
        "stolen",
        "scam",
        "chargeback",
        "hacked",
        "breach",
        "otp",
        "cvv",
        "pin leak"
    ]

    for word in risky_keywords:
        if word in query:
            return True

    return False