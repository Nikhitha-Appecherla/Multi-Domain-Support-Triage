import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = faiss.IndexFlatL2(384)

        self.data = []

    def add(self, issue, subject, response, company):

        emb = self.model.encode([issue]).astype("float32")

        self.index.add(emb)

        self.data.append({
            "issue": issue,
            "subject": subject,
            "response": response,
            "company": company
            })
    def search(self, query, company, k=1):

        if len(self.data) == 0:
            return None

        emb = self.model.encode([query]).astype("float32")

        D, I = self.index.search(emb, int(k))

        best_distance = D[0][0]
        best_index = I[0][0]

        # 🔥 similarity threshold
        if best_distance > 0.45:
            return None

        result = self.data[best_index]

        # 🔥 company filter
        if result["company"] != company:
            return None

        return result
