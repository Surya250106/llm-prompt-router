"""
Intent Constants

Defines the set of valid intent labels used by the prompt router.
These labels must match what the classifier returns.
"""

# All supported intent labels
VALID_INTENTS = [
    "code",
    "data",
    "writing",
    "career",
    "unclear"
]

# Default fallback intent when classification fails
UNCLEAR_INTENT = "unclear"