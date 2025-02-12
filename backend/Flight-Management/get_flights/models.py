from flask_sqlalchemy import SQLAlchemy

db_postgres = SQLAlchemy()

class Flight(db_postgres.Model):
    """
    Flight Model
    ---
    id: Auto-increment primary key
    origin: Flight origin location
    destination: Flight destination location
    departure_time: Date and time of departure
    arrival_time: Date and time of arrival
    price: Price of the flight
    status: Status of the flight (active, cancelled, etc.)
    total_seats: Total seats available on the flight
    available_seats: Seats currently available for booking
    """
    __tablename__ = "flights"

    id = db_postgres.Column(db_postgres.Integer, primary_key=True)
    origin = db_postgres.Column(db_postgres.String(100), nullable=False)
    destination = db_postgres.Column(db_postgres.String(100), nullable=False)
    departure_time = db_postgres.Column(db_postgres.DateTime, nullable=False)
    arrival_time = db_postgres.Column(db_postgres.DateTime, nullable=False)
    price = db_postgres.Column(db_postgres.Numeric(10, 2), nullable=False)
    status = db_postgres.Column(db_postgres.String(50), nullable=False, default="active")
    total_seats = db_postgres.Column(db_postgres.Integer, nullable=False)
    available_seats = db_postgres.Column(db_postgres.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time.strftime('%Y-%m-%dT%H:%M:%S'),
            "arrival_time": self.arrival_time.strftime('%Y-%m-%dT%H:%M:%S'),
            "price": str(self.price),
            "status": self.status,
            "total_seats": self.total_seats,
            "available_seats": self.available_seats
        }
