from app.core.openai_client import client
from app.core.config import settings
from app.constants.intents import UNCLEAR_INTENT
from app.services.prompt_manager import prompt_manager
from app.utils.logger import log_request


def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent", UNCLEAR_INTENT)
    confidence = intent_data.get("confidence", 0.0)

    if intent == UNCLEAR_INTENT:

        clarification = (
            "I'm not sure what type of help you're looking for. "
            "Are you asking about coding, data analysis, writing improvement, "
            "or career advice?"
        )

        log_request(intent, confidence, message, clarification)

        return clarification

    system_prompt = prompt_manager.get_prompt(intent)

    try:

        response = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
        )

        final_response = response.choices[0].message.content.strip()

        log_request(intent, confidence, message, final_response)

        return final_response

    except Exception as e:

        print("Router error:", str(e))

        fallback = "An error occurred while generating the response."

        log_request(intent, confidence, message, fallback)

        return fallback
