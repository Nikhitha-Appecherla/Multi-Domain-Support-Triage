import re
from rapidfuzz import fuzz

SUPPORTED_DOMAINS = {

    "HackerRank": [
        "hackerrank", "login", "submission", "assessment",
        "runtime error", "wrong answer", "testcase",
        "interview", "coding test", "compiler"
    ],

    "Claude": [
        "claude", "api", "anthropic", "quota",
        "workspace", "token", "rate limit", "billing"
    ],

    "Visa": [
        "visa", "payment", "transaction", "card",
        "otp", "refund", "chargeback", "fraud"
    ]
}
def clean_text(text):
    return re.sub(r'\s+', ' ', text.lower()).strip()
def is_garbage(text):

    text = text.strip()

    if len(text) < 3:
        return True

    if re.match(r'^[^a-zA-Z]+$', text):
        return True

    return False
def detect_company(issue):

    if is_garbage(issue):
        return None

    issue = clean_text(issue)

    best_company = None
    best_score = 0

    for company, keywords in SUPPORTED_DOMAINS.items():

        score = 0

        for keyword in keywords:

            # strong match
            if keyword in issue:
                score += 5

            # fuzzy match (phrase-level, NOT word-level)
            if fuzz.partial_ratio(keyword, issue) > 85:
                score += 2

        # normalize bias
        score = score / len(keywords)

        if score > best_score:
            best_score = score
            best_company = company

    # threshold tuning
    if best_score >= 0.15:
        return best_company

    return None