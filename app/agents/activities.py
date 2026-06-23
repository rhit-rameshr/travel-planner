from app.graph.state import TravelState


def activity_node(state: TravelState):
    print("Activity node")

    state["activities"] = [
        {
            "name": "Tokyo Skytree",
            "category": "sightseeing",
            "cost": 30,
            "duration_hours": 3,
            "location": "Tokyo",
            "available_dates": [],
            "description": "Observation tower"
        }
    ]

    return state