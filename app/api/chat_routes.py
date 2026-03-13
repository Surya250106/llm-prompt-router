from fastapi import APIRouter, HTTPException
from app.models.request_model import ChatRequest
from app.models.response_model import ChatResponse
from app.services.classifier import classify_intent
from app.services.router import route_and_respond

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main chat endpoint.

    Steps:
    1. Classify user intent using LLM
    2. Route request to appropriate expert persona
    3. Return generated response with intent + confidence
    """

    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        # Step 1: Classify intent
        intent_data = classify_intent(user_message)

        # Step 2: Route and generate response
        final_response = route_and_respond(user_message, intent_data)

        # Step 3: Return structured response
        return ChatResponse(
            intent=intent_data["intent"],
            confidence=intent_data["confidence"],
            response=final_response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )