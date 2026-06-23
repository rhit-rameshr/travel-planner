import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.agents.accommodations import find_accommodations

from app.agents.accommodations import find_accommodations


def test_budget_travel_style():
    state = {
        "preferences": {
            "travel_style": "budget"
        }
    }

    result = find_accommodations(state)

    print("\nBudget Selection:")
    print(result["selected_accommodation"])

    assert "selected_accommodation" in result
    assert "accommodation_cost" in result


def test_luxury_travel_style():
    state = {
        "preferences": {
            "travel_style": "luxury"
        }
    }

    result = find_accommodations(state)

    print("\nLuxury Selection:")
    print(result["selected_accommodation"])

    assert "selected_accommodation" in result
    assert "accommodation_cost" in result


def test_balanced_travel_style():
    state = {
        "preferences": {
            "travel_style": "balanced"
        }
    }

    result = find_accommodations(state)

    print("\nBalanced Selection:")
    print(result["selected_accommodation"])

    assert "selected_accommodation" in result
    assert "accommodation_cost" in result


if __name__ == "__main__":
    test_budget_travel_style()
    test_luxury_travel_style()
    test_balanced_travel_style()

    print("\n✅ All accommodation tests passed")