"""
Prompt Manager

Responsible for loading and providing expert system prompts
used by the router.
"""

import json
from pathlib import Path
from app.constants.intents import VALID_INTENTS

# Resolve prompts.json path
PROMPTS_FILE = Path(__file__).resolve().parent.parent / "prompts" / "prompts.json"


class PromptManager:
    """
    Handles loading and retrieving expert prompts.
    """

    def __init__(self):
        self.prompts = self._load_prompts()

    def _load_prompts(self):
        """
        Load prompts from JSON file.
        """

        try:
            with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
                prompts = json.load(f)

            # Validate prompts
            for intent in VALID_INTENTS:
                if intent == "unclear":
                    continue
                if intent not in prompts:
                    raise ValueError(f"Missing prompt for intent: {intent}")

            return prompts

        except Exception as e:
            raise RuntimeError(f"Failed to load prompts: {str(e)}")

    def get_prompt(self, intent: str) -> str:
        """
        Retrieve system prompt for a given intent.
        """

        return self.prompts.get(intent)


# Singleton instance
prompt_manager = PromptManager()