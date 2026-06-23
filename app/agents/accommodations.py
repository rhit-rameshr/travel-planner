# # app/agents/accommodations.py

# import json
# from google import genai

# from app.graph import state
# from app.graph.state import TravelState
# from app.tools.hotel_search import search_hotels


# client = genai.Client()


# def accommodation_score(
#     accommodation: dict,
#     rating_weight: float,
#     price_weight: float,
# ) -> float:
#     """
#     Calculate a weighted score for an accommodation.
#     Higher score = better option.
#     """

#     rating_score = accommodation["rating"] / 5.0
#     price_score = max(0, 1 - (accommodation["price"] / 2000))

#     return (
#         rating_weight * rating_score
#         + price_weight * price_score
#     )


# def choose_accommodation_with_gemini(
#     accommodations: list,
#     preferences: dict,
# ):
#     """
#     Ask Gemini to choose the best accommodation.
#     """

#     prompt = f"""
# You are an expert travel planner.

# User preferences:
# {json.dumps(preferences, indent=2)}

# Available accommodations:
# {json.dumps(accommodations, indent=2)}

# Choose the BEST accommodation.

# Consider:
# - Price
# - Rating
# - Travel style
# - Overall value

# Return ONLY valid JSON:

# {{
#     "selected_name": "hotel name",
#     "reason": "short explanation"
# }}
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt,
#     )

#     text = response.text.strip()

#     # Gemini sometimes wraps JSON in markdown
#     text = text.replace("```json", "").replace("```", "").strip()

#     result = json.loads(text)

#     selected = next(
#         a for a in accommodations
#         if a["name"] == result["selected_name"]
#     )

#     return selected, result["reason"]


# def find_accommodations(state: TravelState) -> TravelState:
#     """
#     Accommodation search agent.
#     """

#     destination = "Tokyo"

#     if state.get("selected_flight"):
#         destination = state["selected_flight"]["destination"]


#     accommodations = search_hotels(
#     destination=destination,
#     check_in=state["start_date"],
#     check_out=state["end_date"],
# )

#     rating_weight = 0.6
#     price_weight = 0.4

#     travel_style = (
#         state.get("preferences", {})
#         .get("travel_style", "balanced")
#         .lower()
#     )

#     if travel_style == "budget":
#         rating_weight = 0.3
#         price_weight = 0.7

#     elif travel_style == "luxury":
#         rating_weight = 0.8
#         price_weight = 0.2

#     ranked = sorted(
#         accommodations,
#         key=lambda a: accommodation_score(
#             a,
#             rating_weight,
#             price_weight,
#         ),
#         reverse=True,
#     )

#     # Send only top 3 candidates to Gemini
#     shortlisted = ranked[:3]

#     selected, reason = choose_accommodation_with_gemini(
#         shortlisted,
#         state.get("preferences", {}),
#     )

#     return {
#         **state,
#         "accommodations": accommodations,
#         "selected_accommodation": selected,
#         "accommodation_cost": selected["price"],
#         "accommodation_reason": reason,
#     }

from app.graph.state import TravelState


def accommodation_node(state: TravelState):
    print("Accommodation node")

    state["accommodations"] = [
        {
            "type": "hotel",
            "name": "Hilton Tokyo",
            "location": "Tokyo",
            "check_in": "2026-06-01",
            "check_out": "2026-06-08",
            "nightly_rate": 150,
            "total_price": 1050,
            "rating": 4.5,
            "booking_url": ""
        }
    ]

    return state