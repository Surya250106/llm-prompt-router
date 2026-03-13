# LLM-Powered Prompt Router for Intent Classification

## Overview

This project implements a production-style **LLM-powered prompt router**
that intelligently routes user queries to specialized AI personas based
on the detected intent.

Instead of relying on a single monolithic prompt, the system first
classifies the user's intent and then delegates the request to a focused
expert prompt designed for that task.

This architecture improves response quality, modularity, and scalability
for AI-powered applications.

------------------------------------------------------------------------

## System Architecture

The application follows a **two-step process: classify → route →
respond**.

    User Message
    ↓
    Intent Classifier (LLM Call #1)
    ↓
    Intent + Confidence
    ↓
    Prompt Router
    ├── Code Expert
    ├── Data Analyst
    ├── Writing Coach
    ├── Career Advisor
    └── Clarification (if unclear)
    ↓
    Response Generator (LLM Call #2)
    ↓
    Log Routing Decision
    ↓
    Return Response

------------------------------------------------------------------------

## Features

-   Intent classification using an LLM
-   Modular prompt routing architecture
-   Four specialized expert personas
-   Confidence-based routing
-   Clarification handling for unclear queries
-   JSON Lines request logging
-   Docker containerization
-   Automated test scripts
-   FastAPI-based REST API
-   Structured project architecture

------------------------------------------------------------------------

## Expert Personas

The system routes queries to four expert personas:

  -----------------------------------------------------------------------
  Intent                  Persona                 Description
  ----------------------- ----------------------- -----------------------
  `code`                  Code Expert             Provides programming
                                                  help, debugging, and
                                                  code examples

  `data`                  Data Analyst            Explains data insights,
                                                  statistics, and
                                                  visualizations

  `writing`               Writing Coach           Provides feedback on
                                                  writing clarity and
                                                  structure

  `career`                Career Advisor          Offers practical career
                                                  guidance and next steps
  -----------------------------------------------------------------------

If the classifier cannot confidently determine the intent, the system
asks the user for clarification.

------------------------------------------------------------------------

## Project Structure

    llm-prompt-router
    │
    ├── app/
    │   ├── api/
    │   │   └── chat_routes.py
    │   │
    │   ├── constants/
    │   │   └── intents.py
    │   │
    │   ├── core/
    │   │   ├── config.py
    │   │   └── openai_client.py
    │   │
    │   ├── models/
    │   │   ├── request_model.py
    │   │   └── response_model.py
    │   │
    │   ├── prompts/
    │   │   └── prompts.json
    │   │
    │   ├── services/
    │   │   ├── classifier.py
    │   │   ├── router.py
    │   │   └── prompt_manager.py
    │   │
    │   ├── utils/
    │   │   ├── json_parser.py
    │   │   └── logger.py
    │   │
    │   └── main.py
    │
    ├── docker/
    │   ├── Dockerfile
    │   └── docker-compose.yml
    │
    ├── logs/
    │   └── route_log.jsonl
    │
    ├── scripts/
    │   └── run_tests.py
    │
    ├── tests/
    │   ├── test_messages.txt
    │   └── test_router.py
    │
    ├── requirements.txt
    ├── .env.example
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## Installation

### 1. Clone the Repository

    git clone <repository-url>
    cd llm-prompt-router

------------------------------------------------------------------------

### 2. Create Virtual Environment

    python -m venv venv

Activate environment:

**Windows**

    venv\Scripts\activate

**Mac/Linux**

    source venv/bin/activate

------------------------------------------------------------------------

### 3. Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

### 4. Configure Environment Variables

Copy the environment template:

    cp .env.example .env

Add your OpenAI API key:

    OPENAI_API_KEY=your_api_key_here
    MODEL_NAME=gpt-4o-mini
    CONFIDENCE_THRESHOLD=0.7
    LOG_FILE_PATH=logs/route_log.jsonl

------------------------------------------------------------------------

## Running the Application

Start the FastAPI server:

    uvicorn app.main:app --reload

The API will be available at:

    http://localhost:8000

API documentation:

    http://localhost:8000/docs

------------------------------------------------------------------------

## API Usage

### Endpoint

    POST /api/chat

### Request Example

    {
    "message": "How do I sort a list in Python?"
    }

### Response Example

    {
    "intent": "code",
    "confidence": 0.92,
    "response": "Use the built-in sorted() function..."
    }

------------------------------------------------------------------------

## Logging

All routing decisions are logged to a JSON Lines file:

    logs/route_log.jsonl

Example log entry:

    {
    "timestamp": "2026-03-13T14:34:03",
    "intent": "code",
    "confidence": 0.92,
    "user_message": "sort python list",
    "final_response": "Use sorted()..."
    }

------------------------------------------------------------------------

## Running Tests

Run automated router tests:

    python scripts/run_tests.py

Run unit tests:

    pytest tests/

------------------------------------------------------------------------

## Docker Setup

### Build and Run Container

    docker compose -f docker/docker-compose.yml up --build

Access API:

    http://localhost:8000/docs

------------------------------------------------------------------------

## Example Test Inputs

    how do i sort a list of objects in python?
    explain this sql query for me
    This paragraph sounds awkward, can you help me fix it?
    I'm preparing for a job interview, any tips?
    what's the average of these numbers: 12, 45, 23, 67, 34
    Help me make this better
    hey
    Can you write me a poem about clouds?
    Rewrite this sentence to be more professional
    I'm not sure what to do with my career
    what is a pivot table
    fxi thsi bug pls: for i in range(10) print(i)
    How do I structure a cover letter?
    My boss says my writing is too verbose

------------------------------------------------------------------------

## Design Decisions

### Intent Classification

A lightweight LLM call classifies the user message into predefined
intents:

-   code
-   data
-   writing
-   career
-   unclear

### Prompt Routing

The router selects a specialized system prompt based on the classified
intent, ensuring more accurate responses than a single general prompt.

### Error Handling

The system gracefully handles:

-   malformed JSON responses
-   failed LLM calls
-   low confidence predictions

------------------------------------------------------------------------

## Technologies Used

-   Python
-   FastAPI
-   OpenAI API
-   Docker
-   Pytest
-   Pydantic

------------------------------------------------------------------------

## Future Improvements

-   Confidence-based rerouting
-   Multi-intent detection
-   UI dashboard for monitoring routing decisions
-   Metrics and observability integration
-   Rate limiting and caching

------------------------------------------------------------------------

## License

This project is intended for educational and demonstration purposes.
