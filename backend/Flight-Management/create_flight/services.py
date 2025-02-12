from models import db_postgres, Flight
from datetime import datetime

def create_flight_service(data):
    """
    Service to create a new flight
    """
    try:
        new_flight = Flight(
            origin=data["origin"],
            destination=data["destination"],
            departure_time=datetime.strptime(data["departure_time"], '%Y-%m-%dT%H:%M:%S'),
            arrival_time=datetime.strptime(data["arrival_time"], '%Y-%m-%dT%H:%M:%S'),
            price=data["price"],
            total_seats=data["total_seats"],
            available_seats=data["total_seats"]
        )

        db_postgres.session.add(new_flight)
        db_postgres.session.commit()
        return {"message": "Flight created successfully"}, 201
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
