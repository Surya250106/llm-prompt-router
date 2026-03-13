"""
Application Entry Point

Initializes the FastAPI application and registers API routes.
This file is used by the ASGI server (uvicorn) to run the service.
"""

from fastapi import FastAPI
from app.api.chat_routes import router as chat_router


def create_app() -> FastAPI:
    """
    Application factory for creating the FastAPI app.
    """

    app = FastAPI(
        title="LLM Prompt Router",
        description="Intent-based LLM prompt routing service",
        version="1.0.0"
    )

    # Register API routes
    app.include_router(chat_router, prefix="/api", tags=["Chat"])

    return app


# FastAPI application instance
app = create_app()