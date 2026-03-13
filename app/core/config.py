import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    """
    Central configuration class.
    """

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4o-mini")

    CONFIDENCE_THRESHOLD: float = float(os.getenv("CONFIDENCE_THRESHOLD", "0.7"))

    LOG_FILE_PATH: str = os.getenv("LOG_FILE_PATH", "logs/route_log.jsonl")

    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    ALLOWED_INTENTS = [
        "code",
        "data",
        "writing",
        "career",
        "unclear"
    ]


settings = Settings()