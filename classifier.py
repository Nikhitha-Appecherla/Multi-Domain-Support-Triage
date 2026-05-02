def classify(query):
    query = query.lower()

    # 🔴 HIGH PRIORITY: VISA / FRAUD
    if any(word in query for word in [
        "visa", "card", "payment", "money", "stolen", "unauthorized", "fraud", "bank"
    ]):
        return "visa"

    # 🟡 CLAUDE
    if "claude" in query:
        return "claude"

    # 🟢 HACKERRANK
    if "hackerrank" in query or "login" in query or "assessment" in query:
        return "hackerrank"

    # DEFAULT SAFE FALLBACK
    return "Please check your input and try again"