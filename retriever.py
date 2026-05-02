import os

# ✅ Load all corpus files
def load_corpus(folder_path):
    docs = {}

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            category = file.replace(".txt", "")
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                docs[category] = f.read()

    return docs


# ✅ Smart retrieval (best matching section)
def retrieve(docs, category, query):
    text = docs.get(category, "")

    if category.upper() not in ('VISA', 'CLAUDE', 'HACKERRANK'):
        return "Please select a valid category"

    # Split into sections
    sections = text.split("\n\n")

    query_words = query.lower().split()

    best_section = ""
    best_score = 0

    for sec in sections:
        sec_lower = sec.lower()
        score = sum(word in sec_lower for word in query_words)

        if score > best_score:
            best_score = score
            best_section = sec

    return best_section if best_section else text