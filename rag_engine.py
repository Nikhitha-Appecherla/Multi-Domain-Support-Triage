class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.texts = []
        self.meta = []   # 👈 store company

    def add(self, text, company):
        emb = self.model.encode([text]).astype("float32")
        self.index.add(emb)
        self.texts.append(text)
        self.meta.append(company)

    def search(self, query, company, k=3):
        if len(self.texts) == 0:
            return []

        emb = self.model.encode([query]).astype("float32")
        D, I = self.index.search(emb, k)

        results = []

        for i, d in zip(I[0], D[0]):
            if i < len(self.texts):
                # 🔥 STRICT FILTER BY COMPANY
                if self.meta[i] == company and d < 1.2:
                    results.append(self.texts[i])

        return results