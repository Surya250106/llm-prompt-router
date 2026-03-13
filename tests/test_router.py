"""
Router Test Script

This test script sends requests to the running API
and validates basic response structure.
"""

import requests

API_URL = "http://localhost:8000/api/chat"


def test_router_response():
    message = "how do i sort a list in python?"

    response = requests.post(
        API_URL,
        json={"message": message},
        timeout=30
    )

    assert response.status_code == 200

    data = response.json()

    assert "intent" in data
    assert "confidence" in data
    assert "response" in data


def test_unclear_intent():
    message = "hey"

    response = requests.post(
        API_URL,
        json={"message": message},
        timeout=30
    )

    data = response.json()

    assert data["intent"] in [
        "code",
        "data",
        "writing",
        "career",
        "unclear"
    ]