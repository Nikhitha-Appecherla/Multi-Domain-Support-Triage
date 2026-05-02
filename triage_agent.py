from classifier import classify
from retriever import load_corpus, retrieve
from router import should_escalate

import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--corpus", required=True)
args = parser.parse_args()

# Load corpus
docs = load_corpus(args.corpus)

print("\n🚀 Support Triage Agent Started")

while True:
    query = input("\nEnter ticket (or type exit): ")

    if query.lower() == "exit":
        print("\n👋 Exiting Support Triage Agent")
        break

    # 🔹 Step 1: Classification
    category = classify(query)

    # 🔹 Step 2: Escalation decision
    escalated = should_escalate(query)

    # 🔹 Output Header
    print("\n========================================")
    print("        TICKET ANALYSIS RESULT")
    print("========================================")
    print("CATEGORY   :", category.capitalize())

    # 🔹 Confidence score
    q = query.lower()
    if category == "visa":
        confidence = 95
    elif "login" in q or "password" in q:
        confidence = 90
    elif category == "claude":
        confidence = 85
    else:
        confidence = 0

    print("CONFIDENCE :", str(confidence) + "%")

    # 🔴 ESCALATION CASE
    if escalated:
        print("ACTION     : ESCALATED")
        print("REASON     : Detected fraud/security-related keywords")
        print("========================================")
        print("⚠️ ROUTED TO HUMAN SUPPORT")
        print("Please contact your bank or card issuer immediately.")
        print("Do not share OTP, CVV, or PIN with anyone.")
        print("========================================")
        continue

    # 🟢 NORMAL RESPONSE
    info = retrieve(docs, category, query)

    print("ACTION     : ANSWERED")
    print("REASON     : Matched query to support corpus")
    print("========================================")
    print("RESPONSE:\n")
    print(info)
    print("========================================")