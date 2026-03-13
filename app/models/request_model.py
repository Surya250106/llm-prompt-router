"""
Request model for chat endpoint.
Defines the structure of incoming user messages.
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Incoming API request schema.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User input message that needs intent classification and routing"
    )