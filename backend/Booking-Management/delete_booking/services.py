from models import db_postgres, Booking

def delete_booking_service(booking_id):
    """
    Service to delete a booking by ID
    """
    booking = Booking.query.get(booking_id)
    if not booking:
        return {"error": "Booking not found"}, 404

    try:
        db_postgres.session.delete(booking)
        db_postgres.session.commit()
        return {"message": "Booking deleted successfully"}, 200
    except Exception as e:
        db_postgres.session.rollback()
        return {"error": str(e)}, 500
