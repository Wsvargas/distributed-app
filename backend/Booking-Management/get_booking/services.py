from models import db_postgres, Booking

def get_all_bookings():
    """
    Service to get all bookings
    """
    bookings = Booking.query.all()
    return [b.to_dict() for b in bookings], 200
