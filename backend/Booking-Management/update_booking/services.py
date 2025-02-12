from models import db_postgres, Booking
from datetime import datetime

def update_booking_service(booking_id, data):
    """
    Service to update a booking
    """
    booking = Booking.query.get(booking_id)
    if not booking:
        return {"error": "Booking not found"}, 404

    try:
        if "user_id" in data:
            booking.user_id = data["user_id"]
        if "flight_id" in data:
            booking.flight_id = data["flight_id"]
        if "booking_date" in data:
            booking.booking_date = datetime.strptime(data["booking_date"], "%Y-%m-%dT%H:%M:%S")
        if "status" in data:
            booking.status = data["status"]

        db_postgres.session.commit()
        return {"message": "Booking updated successfully"}, 200
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
