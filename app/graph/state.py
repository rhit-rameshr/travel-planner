# Defines shared state that every LangGraph node (flights, stays, activities, planner) can read and update.

# app/graph/state.py

from typing import TypedDict, List, Optional


class Activity(TypedDict):
    name: str
    cost: float
    duration_hours: float


class Flight(TypedDict):
    airline: str
    departure: str
    arrival: str
    price: float
    duration_hours: float
    layover_duration: float


class Stay(TypedDict):
    name: str
    type: str  # Hotel or Airbnb
    nightly_rate: float
    total_price: float
    location: str


class TravelState(TypedDict):
    # Original user request
    user_query: str

    # Extracted requirements
    departure_airport: str | None
    start_date: str | None
    end_date: str | None
    budget: float | None

    preferences: dict

    # Destination recommendation stage
    destination_candidates: list
    selected_destination: dict | None

    # Travel planning stage
    flight_options: list
    hotel_options: list
    activity_options: list

    # Final chosen itinerary
    selected_flight: dict | None
    selected_hotel: dict | None
    selected_activities: list

    total_cost: float
    itinerary: str