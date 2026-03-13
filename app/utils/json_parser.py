"""
Safe JSON Parser Utility
Handles malformed LLM JSON responses safely.
"""

import json
import re


def safe_json_parse(text: str) -> dict:
    """
    Extract and parse JSON from LLM output.

    Handles cases like:
    - markdown ```json blocks
    - extra explanations
    - whitespace
    """

    try:
        return json.loads(text)
    except Exception:
        pass

    try:
        # Extract JSON object using regex
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception:
        pass

    return {}