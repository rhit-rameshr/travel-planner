# app/tools/hotel_search.py

def search_hotels(
    destination: str,
    check_in: str,
    check_out: str,
):
    """
    Mock hotel search.
    Later this will call a real API.
    """

    return [
        {
            "type": "Hotel",
            "name": "Shinjuku Grand Hotel",
            "location": destination,
            "price": 1200,
            "rating": 4.5,
        },
        {
            "type": "Airbnb",
            "name": "Modern City Apartment",
            "location": destination,
            "price": 950,
            "rating": 4.8,
        },
        {
            "type": "Hotel",
            "name": "Budget Inn",
            "location": destination,
            "price": 700,
            "rating": 4.1,
        },
    ]