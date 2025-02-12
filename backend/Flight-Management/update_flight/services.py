from models import db_postgres, Flight
from datetime import datetime

def update_flight_service(flight_id, data):
    """
    Service to update a flight by ID
    """
    flight = Flight.query.get(flight_id)
    if not flight:
        return {"error": "Flight not found"}, 404

    try:
        flight.origin = data.get("origin", flight.origin)
        flight.destination = data.get("destination", flight.destination)
        flight.departure_time = datetime.strptime(data["departure_time"], '%Y-%m-%dT%H:%M:%S') if "departure_time" in data else flight.departure_time
        flight.arrival_time = datetime.strptime(data["arrival_time"], '%Y-%m-%dT%H:%M:%S') if "arrival_time" in data else flight.arrival_time
        flight.price = data.get("price", flight.price)
        flight.status = data.get("status", flight.status)
        flight.available_seats = data.get("available_seats", flight.available_seats)

        db_postgres.session.commit()
        return {"message": "Flight updated successfully"}, 200
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
