from vector_store import VectorStore
from llm_engine import generate_response

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# =========================
# SEMANTIC ROUTER MODEL
# =========================

router_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# SEMANTIC COMPANY ROUTING
# =========================

company_examples = {

    "hackerrank": [

        # coding/interview
        "coding platform",
        "online coding test",
        "technical interview",
        "programming challenge",
        "coding assessment",
        "online assessment",
        "technical screening",
        "candidate evaluation",

        # compiler/submission
        "compiler error",
        "runtime error",
        "syntax issue",
        "submission failed",
        "code execution failed",
        "testcase failure",
        "program output mismatch",
        "time limit exceeded",
        "memory limit exceeded",

        # interview environment
        "camera issue",
        "microphone issue",
        "browser compatibility",
        "compatibility check",
        "fullscreen blocked",
        "proctoring issue",
        "interview disconnected",
        "webcam permission denied",

        # platform issues
        "editor not loading",
        "coding page stuck",
        "challenge not opening",
        "assessment loading issue",
        "score not updating",
        "leaderboard not refreshing"
    ],

    "claude": [

        # ai/chatbot
        "ai assistant",
        "chatbot",
        "language model",
        "conversation ai",
        "generative ai",
        "ai response problem",

        # api/platform
        "api timeout",
        "api failure",
        "invalid api key",
        "authentication failed",
        "quota exceeded",
        "rate limit exceeded",
        "workspace access denied",

        # subscriptions/team
        "subscription cancellation",
        "billing issue",
        "team access removed",
        "workspace removed",
        "seat removed by admin",
        "organization access issue",

        # performance
        "slow ai response",
        "assistant not responding",
        "server overloaded",
        "internal server error",
        "unable to generate output",

        # files/browser
        "file upload failed",
        "browser compatibility issue",
        "session expired",
        "conversation history missing"
    ],

    "visa": [

        # payments
        "payment failed",
        "money deducted",
        "transaction declined",
        "international transaction issue",
        "card payment failed",
        "payment processing issue",
        "refund pending",

        # application
        "visa application rejected",
        "application under review",
        "application delayed",
        "application incomplete",
        "document verification issue",

        # verification
        "passport verification",
        "biometric verification",
        "identity verification",
        "otp verification",
        "travel document issue",

        # appointments
        "embassy appointment",
        "slot unavailable",
        "interview rescheduled",
        "appointment booking failed",

        # account/login
        "visa account locked",
        "otp not received",
        "payment receipt missing",
        "status not updating"
    ]
}
# =========================
# VECTOR STORE
# =========================

store = VectorStore()

# =========================
# KNOWLEDGE BASE
# =========================

# ---------- HACKERRANK ----------

store.add(
    "cannot login to hackerrank",
    "Hackerrank login issue",
    "Reset your password and verify your email.",
    "hackerrank"
)

store.add(
    "hackerrank login failed",
    "Hackerrank login issue",
    "Reset your password and verify your email.",
    "hackerrank"
)

store.add(
    "hackerrank account locked",
    "Hackerrank account issue",
    "Wait for account unlock or reset your password.",
    "hackerrank"
)

store.add(
    "forgot hackerrank password",
    "Hackerrank password recovery",
    "Use the forgot password option to recover your account.",
    "hackerrank"
)

store.add(
    "hackerrank code not accepted",
    "Hackerrank code submission issue",
    "Check failed testcases and input formatting.",
    "hackerrank"
)

store.add(
    "hackerrank wrong answer",
    "Hackerrank wrong answer issue",
    "Verify edge cases and ensure your logic handles all inputs.",
    "hackerrank"
)

store.add(
    "hackerrank runtime error",
    "Hackerrank runtime error",
    "Check null values, array bounds, and invalid operations.",
    "hackerrank"
)

store.add(
    "hackerrank compilation error",
    "Hackerrank compilation issue",
    "Check syntax errors and verify selected language.",
    "hackerrank"
)

store.add(
    "hackerrank time limit exceeded",
    "Hackerrank performance issue",
    "Optimize your algorithm to reduce execution time.",
    "hackerrank"
)

store.add(
    "hackerrank interview audio not working",
    "Hackerrank audio issue",
    "Check microphone permissions and browser audio settings.",
    "hackerrank"
)

store.add(
    "hackerrank camera not working",
    "Hackerrank camera issue",
    "Allow camera permissions and refresh the page.",
    "hackerrank"
)

store.add(
    "hackerrank editor not loading",
    "Hackerrank editor issue",
    "Refresh the page and clear browser cache.",
    "hackerrank"
)

store.add(
    "hackerrank dark mode not working",
    "Hackerrank UI issue",
    "Clear browser cache or switch themes and retry.",
    "hackerrank"
)

# ---------- CLAUDE ----------

store.add(
    "claude is not responding",
    "Claude response issue",
    "Refresh the page and retry after some time.",
    "claude"
)

store.add(
    "lost access to claude team",
    "Claude team access issue",
    "Contact your admin to restore your Claude seat.",
    "claude"
)

store.add(
    "claude api timeout",
    "Claude API timeout issue",
    "Retry after some time and verify API availability.",
    "claude"
)

store.add(
    "claude api key invalid",
    "Claude API key issue",
    "Verify your API key and regenerate if needed.",
    "claude"
)

store.add(
    "claude quota exceeded",
    "Claude quota exceeded",
    "You exceeded your current usage limits.",
    "claude"
)

store.add(
    "claude account locked",
    "Claude account issue",
    "Wait for temporary unlock or contact support.",
    "claude"
)

store.add(
    "claude billing issue",
    "Claude billing issue",
    "Verify your payment method and subscription status.",
    "claude"
)

store.add(
    "claude slow response",
    "Claude performance issue",
    "High server load may delay responses temporarily.",
    "claude"
)

# ---------- VISA ----------

store.add(
    "visa application rejected",
    "Visa application rejection",
    "Please recheck your documents and financial proofs.",
    "visa"
)

store.add(
    "visa payment failed",
    "Visa payment issue",
    "Verify payment details and retry the transaction.",
    "visa"
)

store.add(
    "visa biometric verification pending",
    "Visa biometric issue",
    "Complete biometric verification at the assigned center.",
    "visa"
)
store.add(
    "unauthorized visa transaction",
    "Visa fraud transaction issue",
    "Immediately block the card and contact your bank support.",
    "visa"
)

store.add(
    "visa otp not received",
    "Visa OTP issue",
    "Check network connectivity and retry OTP verification.",
    "visa"
)

store.add(
    "visa appointment unavailable",
    "Visa appointment issue",
    "Appointment slots may open periodically. Retry later.",
    "visa"
)

store.add(
    "visa application delayed",
    "Visa processing delay",
    "Processing times may vary depending on application type.",
    "visa"
)

store.add(
    "visa documents missing",
    "Visa document issue",
    "Upload all mandatory documents before submission.",
    "visa"
)

# =========================
# SEMANTIC COMPANY DETECTION
# =========================

def detect_company(issue: str):

    issue_low = issue.lower()

    # direct keyword routing

    if "hackerrank" in issue_low:
        return "hackerrank"

    if "claude" in issue_low:
        return "claude"

    if "visa" in issue_low:
        return "visa"

    # semantic routing

    issue_emb = router_model.encode([issue])

    best_company = "unknown"
    best_score = 0

    for company, examples in company_examples.items():

        example_embs = router_model.encode(examples)

        similarities = cosine_similarity(
            issue_emb,
            example_embs
        )[0]

        score = np.max(similarities)

        if score > best_score:

            best_score = score
            best_company = company

    #print("Detected:", best_company, "| Score:", best_score)

    # threshold

    if best_score < 0.30:
        return "unknown"

    return best_company

# =========================
# MAIN PIPELINE
# =========================

def process(issue: str):

    # company detection

    company = detect_company(issue)

    # out of scope

    if company == "unknown":

        return {
            "company": "unknown",
            "subject": "Out of scope request",
            "reason": "Unsupported domain",
            "response": "OUT OF SCOPE"
        }

    # default subject

    subject = f"{company.capitalize()} support issue"

    # RAG retrieval

    rag_result = store.search(issue, company)

    # =========================
    # RAG + GEMINI
    # =========================

    if rag_result:

        subject = rag_result["subject"]

        reason = "Response generated using RAG + Gemini"

        context = rag_result["response"]

        prompt = f"""
        Support Knowledge:
        {context}

        User Issue:
        {issue}

        Generate a short helpful support response in 1-2 lines only.
        """

        print("CALLING GEMINI WITH RAG CONTEXT")

        response = generate_response(prompt)

       # print("LLM OUTPUT:", response)

        # Gemini failed

        if (
            response == "Service temporarily unavailable."
            or
            response == "Quota exceeded. Using fallback response."
        ):

            response = context

    # =========================
    # GEMINI FALLBACK
    # =========================

    else:

       # print("USING GEMINI FALLBACK")

        reason = "No similar issue found in knowledge base"

        response = generate_response(issue)

        #print("Gemini Response:", response)

        # Gemini failed

        if (
            response == "Service temporarily unavailable."
            or
            response == "Quota exceeded. Using fallback response."
        ):

            response = "No relevant support data found."

    # =========================
    # FINAL OUTPUT
    # =========================

    return {
        "company": company,
        "subject": subject,
        "reason": reason,
        "response": response
    }

# =========================
# CLI
# =========================

if __name__ == "__main__":

    print("\n🚀 Hybrid RAG Support System Ready")

    while True:

        issue = input("\nEnter issue (or type exit): ")

        if issue.lower() == "exit":
            break

        result = process(issue)

        print("\n================================\n")

        print(f"Company : {result['company']}")
        print(f"Subject : {result['subject']}")
        print(f"Reason  : {result['reason']}")
        print(f"Response: {result['response']}")

        print("\n================================\n")