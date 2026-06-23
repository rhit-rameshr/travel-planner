# app/graph/state.py

from typing import TypedDict, List, Optional, Dict
from pydantic import BaseModel



# Requirements Models

class Requirements(BaseModel):
    destination: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    duration_days: int | None = None
    budget: int | None = None
    travelers: int = 1
    preferences: list[str] = []

class Preferences(TypedDict, total=False):
    interests: List[str]
    weather: Optional[str]
    travel_style: Optional[str]


class TripRequirements(TypedDict, total=False):
    departure_airport: Optional[str]

    destination_country: Optional[str]
    destination_city: Optional[str]

    start_date: Optional[str]
    end_date: Optional[str]

    travelers: int

    total_budget: Optional[float]

    preferences: Preferences



# Search Result Models

class Destination(TypedDict):
    country: str
    city: str
    score: float


class Flight(TypedDict):
    airline: str
    flight_number: str

    origin: str
    destination: str

    departure_time: str
    arrival_time: str

    duration_hours: float
    layover_duration: float

    price: float

    booking_url: str


class Accommodation(TypedDict):
    type: str  # hotel, airbnb

    name: str
    location: str

    check_in: str
    check_out: str

    nightly_rate: float
    total_price: float

    rating: float

    booking_url: str


class Activity(TypedDict):
    name: str

    category: str

    cost: float
    duration_hours: float

    location: str

    available_dates: List[str]

    description: str



# Selection Models

class DailyPlan(TypedDict):
    date: str
    activities: List[str]



# Main LangGraph State


class TravelState(TypedDict, total=False):
    # User input
    user_query: str

    # Extracted requirements
    requirements: TripRequirements

    # Destination recommendations
    destinations: List[Destination]

    # Search results
    flights: List[Flight]
    accommodations: List[Accommodation]
    activities: List[Activity]

    # Search status tracking
    flights_found: bool
    accommodations_found: bool
    activities_found: bool

    # Selected options
    selected_flight: Flight
    selected_accommodation: Accommodation
    selected_activities: List[Activity]

    # Budget calculations
    flight_cost: float
    accommodation_cost: float
    activity_cost: float
    transportation_cost: float

    total_trip_cost: float
    remaining_budget: float

    # Final itinerary
    itinerary: dict
    daily_itinerary: List[DailyPlan]

    # Workflow tracking
    requirements_complete: bool
    missing_fields: List[str]

    # Error handling
    errors: List[str]