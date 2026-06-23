# Defines shared state that every LangGraph node (flights, stays, activities, planner) can read and update.

# app/graph/state.py

from typing import TypedDict, List, Optional


class Destination(TypedDict):
    country: str
    city: str
    score: float


class Flight(TypedDict):
    airline: str
    price: float
    duration_hours: float
    layover_duration: float
    origin: str
    destination: str


class Accommodation(TypedDict):
    type: str
    name: str
    location: str
    price: float
    rating: float


class Activity(TypedDict):
    name: str
    cost: float
    duration_hours: float
    location: str
    available_dates: List[str]
    

class Preferences(TypedDict):
    interests: List[str]
    weather: str
    travel_style: str


class TravelState(TypedDict):
    # Original request
    user_query: str

    # Extracted requirements
    departure_airport: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    budget: Optional[float]

    preferences: Preferences

    # Destination stage
    destination_candidates: List[Destination]
    selected_destination: Optional[Destination]

    flight_options: List[Flight]
    accommodation_options: List[Accommodation]
    activity_options: List[Activity]
    transportation_cost: float

    # Final selections
    selected_flight: Optional[Flight]
    selected_accommodation: Optional[Accommodation]
    selected_activities: List[Activity]

    # Cost tracking
    flight_cost: float
    accommodation_cost: float
    activity_cost: float

    total_cost: float
    remaining_budget: float

    # Final output
    daily_itinerary: List[dict]
    itinerary: str