from app.graph.state import TravelState


def flight_node(state: TravelState):
    print("Flight node")

    state["flights"] = [
        {
            "airline": "United",
            "flight_number": "UA837",
            "origin": "SFO",
            "destination": "NRT",
            "departure_time": "10:00",
            "arrival_time": "14:00",
            "duration_hours": 11,
            "layover_duration": 0,
            "price": 800,
            "booking_url": ""
        }
    ]

    return state