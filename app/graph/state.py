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
    description: str


class Preferences(TypedDict):
    interests: List[str]
    weather: Optional[str]
    travel_style: Optional[str]


class TravelState(TypedDict, total=False):
    user_query: str

    departure_airport: Optional[str]

    start_date: Optional[str]
    end_date: Optional[str]

    budget: Optional[float]

    preferences: Preferences

    destinations: List[dict]

    flights: List[dict]
    accommodations: List[dict]
    activities: List[dict]

    itinerary: Optional[dict]

    requirements_complete: bool
    missing_fields: List[str]