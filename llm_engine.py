from dotenv import load_dotenv
import os
from google import genai
from google.api_core.exceptions import ResourceExhausted



# =========================
# GEMINI CLIENT
# =========================
load_dotenv()
client = genai.Client(
    # api_key = os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-2.5-flash"

# =========================
# SUBJECT GENERATION
# =========================

def generate_subject(issue: str):

    try:
        prompt = f"""
Generate ONE short support subject.

Rules:
- Max 6 words
- No numbering
- No explanation

Issue:
{issue}
"""

        res = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return res.text.strip().split("\n")[0]

    except Exception as e:
        print("SUBJECT ERROR:", e)
        return "Subject unavailable"

# =========================
# RESPONSE GENERATION
# =========================

def generate_response(issue: str, context: str = ""):

    try:
        prompt = f"""
You are a strict support TRIAGE agent.

Issue:
{issue}

Context:
{context}

RULES:
- NEVER ask questions
- NEVER request more information
- NEVER be conversational
- ONLY give 2–3 action steps
"""

        res = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return "\n".join(res.text.strip().split("\n")[:3])

    except ResourceExhausted:
        print("GEMINI ERROR: QUOTA EXCEEDED")
        return "Quota exceeded. Using fallback response."

    except Exception as e:
        print("GEMINI ERROR:", e)
        return "Service temporarily unavailable."