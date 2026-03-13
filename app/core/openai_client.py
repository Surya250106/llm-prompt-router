from openai import OpenAI
from app.core.config import settings


def get_openai_client():
    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set")

    return OpenAI(api_key=settings.OPENAI_API_KEY)


client = get_openai_client()
