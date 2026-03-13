"""
Mock Intent Classifier

This version does NOT call OpenAI.
It uses simple keyword rules to classify intent.

Used when OpenAI quota is unavailable.
"""

from app.constants.intents import UNCLEAR_INTENT


def classify_intent(message: str):

    msg = message.lower()

    # Code related
    if any(word in msg for word in ["python", "bug", "function", "code", "sql", "query"]):
        return {
            "intent": "code",
            "confidence": 0.9
        }

    # Data related
    if any(word in msg for word in ["average", "dataset", "data", "pivot", "statistics"]):
        return {
            "intent": "data",
            "confidence": 0.9
        }

    # Writing related
    if any(word in msg for word in ["paragraph", "writing", "sentence", "verbose", "professional"]):
        return {
            "intent": "writing",
            "confidence": 0.9
        }

    # Career related
    if any(word in msg for word in ["career", "interview", "resume", "job", "cover letter"]):
        return {
            "intent": "career",
            "confidence": 0.9
        }

    # Default fallback
    return {
        "intent": UNCLEAR_INTENT,
        "confidence": 0.5
    }
