from app.graph.state import TravelState


def planner_node(state: TravelState):
    print("Planner node")

    state["itinerary"] = """
    Day 1: Arrive Tokyo
    Day 2: Tokyo Skytree
    """

    return state