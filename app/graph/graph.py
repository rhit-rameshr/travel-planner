from langgraph.graph import StateGraph, END

from app.graph.state import TravelState

from app.agents.destination import recommend_destinations
from app.agents.flights import search_flights
from app.agents.accommodations import search_accommodations
from app.agents.activities import search_activities
from app.agents.planner import (
    optimize_budget,
    generate_itinerary
)

builder = StateGraph(TravelState)

builder.add_node(
    "recommend_destinations",
    recommend_destinations
)

builder.add_node(
    "search_flights",
    search_flights
)

builder.add_node(
    "search_accommodations",
    search_accommodations
)

builder.add_node(
    "search_activities",
    search_activities
)

builder.add_node(
    "optimize_budget",
    optimize_budget
)

builder.add_node(
    "generate_itinerary",
    generate_itinerary
)