
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma3:1b"


def analyze_plan(user_plan):
    """Analyze a user's plan using the local Gemma model."""

    prompt = f"""
    You are PlanGuard AI, an intelligent plan analysis assistant.

    Analyze the following plan:
    {user_plan}

    Provide your analysis under these headings:

    1. Plan Summary
    2. Potential Risks
    3. Missing Tasks
    4. Time and Resource Limitations
    5. Priority Tasks
    6. Practical Solutions

    Be clear, realistic, and specific.
    If information is missing, state your assumptions.
    Do not present uncertain predictions as guaranteed facts.
    """

    request_data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    request = Request(
        OLLAMA_URL,
        data=json.dumps(request_data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=300) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["message"]["content"]

    except HTTPError as error:
        return f"Ollama returned an HTTP error: {error.code}"

    except URLError:
        return (
            "Could not connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except (KeyError, ValueError):
        return "The AI returned an unexpected response."
