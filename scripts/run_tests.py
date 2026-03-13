"""
Batch Test Script

Runs multiple test messages through the LLM Prompt Router API
and prints the detected intent, confidence, and response.

Useful for generating route logs and validating routing behavior.
"""

import requests

API_URL = "http://localhost:8000/api/chat"

TEST_MESSAGES = [
    "how do i sort a list of objects in python?",
    "explain this sql query for me",
    "This paragraph sounds awkward, can you help me fix it?",
    "I'm preparing for a job interview, any tips?",
    "what's the average of these numbers: 12, 45, 23, 67, 34",
    "Help me make this better.",
    "I need to write a function that takes a user id and returns their profile",
    "hey",
    "Can you write me a poem about clouds?",
    "Rewrite this sentence to be more professional.",
    "I'm not sure what to do with my career.",
    "what is a pivot table",
    "fxi thsi bug pls: for i in range(10) print(i)",
    "How do I structure a cover letter?",
    "My boss says my writing is too verbose."
]


def run_tests():
    print("Running router tests...\n")

    for i, message in enumerate(TEST_MESSAGES, start=1):
        try:
            response = requests.post(
                API_URL,
                json={"message": message},
                timeout=30
            )

            data = response.json()

            print(f"Test #{i}")
            print(f"Message: {message}")
            print(f"Intent: {data.get('intent')}")
            print(f"Confidence: {data.get('confidence')}")
            print(f"Response: {data.get('response')}")
            print("-" * 60)

        except Exception as e:
            print(f"Test #{i} failed: {str(e)}")


if __name__ == "__main__":
    run_tests()