# app/agents/requirements.py

import json

from google import genai

from app.graph.state import TravelState


from dotenv import load_dotenv
import os

load_dotenv()

from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_requirements(state: TravelState) -> TravelState:
    """
    Extract structured travel requirements from the user's query.
    """

    user_query = state["user_query"]

    prompt = f"""
You are a travel planning assistant.

Extract travel requirements from the user query.

Return ONLY valid JSON.

Schema:

{{
    "destination": null,
    "start_date": null,
    "end_date": null,
    "duration_days": null,
    "budget": null,
    "travelers": 1,
    "preferences": []
}}

Rules:
- destination should be a city or country if specified.
- budget should be a number.
- travelers should be an integer.
- preferences should be a list of interests.
- Use null for missing values.
- Do not include markdown.
- Return JSON only.

User Query:
{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    requirements = json.loads(response.text)

    state["requirements"] = requirements

    return state