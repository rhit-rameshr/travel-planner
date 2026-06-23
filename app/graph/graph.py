from langgraph.graph import StateGraph, END, START

from app.graph.state import TravelState

from app.agents.destination import destination_node
from app.agents.flights import flight_node
from app.agents.accommodations import accommodation_node
from app.agents.activities import activity_node
from app.agents.planner import planner_node
from app.agents.requirements import extract_requirements


builder = StateGraph(TravelState)

builder.add_node("destination", destination_node)
builder.add_node("flights", flight_node)
builder.add_node("accommodations", accommodation_node)
builder.add_node("activities", activity_node)
builder.add_node("planner", planner_node)
builder.add_node(
    "requirements",
    extract_requirements
)

builder.set_entry_point("requirements")

builder.add_edge(
    START,
    "requirements"
)

builder.add_edge("requirements", "destination")
builder.add_edge("destination", "flights")
builder.add_edge("flights", "accommodations")
builder.add_edge("accommodations", "activities")
builder.add_edge("activities", "planner")
builder.add_edge("planner", END)

graph = builder.compile()