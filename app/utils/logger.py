"""
Routing Logger

Writes routing decisions to a JSON Lines log file.
Each request is logged as a single JSON object per line.
"""

import json
from datetime import datetime
from pathlib import Path
from app.core.config import settings


LOG_FILE = Path(settings.LOG_FILE_PATH)


def log_request(intent: str, confidence: float, user_message: str, final_response: str):
    """
    Append a routing log entry to the JSONL log file.

    Args:
        intent (str): Detected intent
        confidence (float): Confidence score
        user_message (str): Original user message
        final_response (str): Generated response
    """

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "intent": intent,
        "confidence": confidence,
        "user_message": user_message,
        "final_response": final_response
    }

    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

    except Exception:
        # Logging should never crash the application
        pass