from flask_sqlalchemy import SQLAlchemy

db_postgres = SQLAlchemy()

class Booking(db_postgres.Model):
    """
    Booking Model
    ---
    id: Auto-increment primary key
    user_id: ID of the user making the booking
    flight_id: ID of the flight being booked
    booking_date: Date and time of booking
    status: Status of the booking (pending, confirmed, canceled)
    """
    id = db_postgres.Column(db_postgres.Integer, primary_key=True)
    user_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    flight_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    booking_date = db_postgres.Column(db_postgres.DateTime, nullable=False)
    status = db_postgres.Column(db_postgres.String(50), nullable=False, default='pending')

    def to_dict(self):
        """
        Convert model to dictionary for JSON response
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'flight_id': self.flight_id,
            'booking_date': self.booking_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'status': self.status
        }
