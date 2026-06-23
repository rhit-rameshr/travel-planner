from app.graph.state import TravelState


def destination_node(state: TravelState):
    print("Destination node")

    state["destinations"] = [
        {
            "country": "Japan",
            "city": "Tokyo",
            "score": 95
        }
    ]

    return state