from models import Flight

def get_flight_service(flight_id):
    """
    Service to get a flight by ID
    """
    flight = Flight.query.get(flight_id)
    if not flight:
        return {"error": "Flight not found"}, 404

    return flight.to_dict(), 200
