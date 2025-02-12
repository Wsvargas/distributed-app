from models import db_postgres, Booking
from datetime import datetime

def create_booking_service(data):
    """
    Handles booking creation logic
    """
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status', 'pending')  # Default to 'pending' if not provided

    if not user_id or not flight_id or not booking_date:
        return {"error": "User ID, flight ID, and booking date are required"}, 400

    try:
        booking_date = datetime.strptime(booking_date, '%Y-%m-%dT%H:%M:%S')

        new_booking = Booking(
            user_id=user_id,
            flight_id=flight_id,
            booking_date=booking_date,
            status=status
        )

        db_postgres.session.add(new_booking)
        db_postgres.session.commit()
        return {"message": "Booking created successfully"}, 201
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
