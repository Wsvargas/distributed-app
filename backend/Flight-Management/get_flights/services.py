from models import Flight

def get_all_flights_service():
    """
    Service to get all flights
    """
    flights = Flight.query.all()
    return [flight.to_dict() for flight in flights], 200
