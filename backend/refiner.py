from utils import is_irrelevant_input


def refine_prompt(text=None, images=None, documents=None):
    source_types = []
    confidence = 0.4

    result = {
        "meta": {
            "source_types": [],
            "confidence_score": 0.0,
            "missing_fields": [],
            "rejected": False,
            "rejection_reason": None
        },
        "intent": {
            "summary": "",
            "domain": "",
            "target_users": ""
        },
        "functional_requirements": [],
        "technical_constraints": [],
        "non_functional_requirements": [],
        "expected_outputs": [],
        "assumptions": [],
        "open_questions": []
    }

    # ---------------- REJECTION ----------------
    if text and is_irrelevant_input(text):
        result["meta"]["rejected"] = True
        result["meta"]["rejection_reason"] = "Input is not a task or product description"
        result["meta"]["confidence_score"] = 0.0
        return result

    # ---------------- SOURCE TYPES ----------------
    if text:
        source_types.append("text")
        confidence += 0.2

    if images:
        source_types.append("image")
        confidence += 0.2

    if documents:
        source_types.append("document")
        confidence += 0.2

    if not source_types:
        result["meta"]["missing_fields"].append("No valid input provided")
        result["meta"]["confidence_score"] = 0.1
        return result

    result["meta"]["source_types"] = source_types

    combined_text = text or ""

    # ---------------- IMAGE INFERENCE ----------------
    if images:
        for img in images:
            if img.caption:
                combined_text += " " + img.caption
            else:
                combined_text += " image related to product design"

    # ---------------- DOCUMENT INFERENCE ----------------
    if documents:
        for doc in documents:
            if doc.extracted_text:
                combined_text += " " + doc.extracted_text
            else:
                combined_text += " document containing technical specifications"

    lower_text = combined_text.lower()

    # ---------------- INTENT ----------------
    result["intent"]["summary"] = combined_text[:200]

    if "app" in lower_text or "website" in lower_text:
        result["intent"]["domain"] = "software"
    else:
        result["meta"]["missing_fields"].append("domain")

    if "student" in lower_text:
        result["intent"]["target_users"] = "students"
    else:
        result["assumptions"].append("Target users are general users")

    # ---------------- FUNCTIONAL ----------------
    if "upload" in lower_text:
        result["functional_requirements"].append("Users can upload files")

    if "login" in lower_text:
        result["functional_requirements"].append("User authentication")

    if "dashboard" in lower_text:
        result["functional_requirements"].append("User dashboard")

    # ---------------- TECHNICAL ----------------
    if "react" in lower_text:
        result["technical_constraints"].append("Frontend must use React")

    if "fastapi" in lower_text or "python" in lower_text:
        result["technical_constraints"].append("Backend must use FastAPI (Python)")

    # ---------------- NON FUNCTIONAL ----------------
    if "secure" in lower_text:
        result["non_functional_requirements"].append("Security best practices")

    if "fast" in lower_text or "scalable" in lower_text:
        result["non_functional_requirements"].append("System should be scalable")

    # ---------------- OUTPUTS ----------------
    result["expected_outputs"].append("Standardized refined prompt (JSON)")
    result["expected_outputs"].append("Clear list of functional and technical requirements")

    # ---------------- CONFIDENCE ----------------
    confidence += min(len(result["functional_requirements"]) * 0.05, 0.2)
    result["meta"]["confidence_score"] = round(min(confidence, 1.0), 2)

    # ---------------- OPEN QUESTIONS ----------------
    if not result["functional_requirements"]:
        result["open_questions"].append("What core features are required?")

    return result
