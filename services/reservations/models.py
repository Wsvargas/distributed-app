from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    seats_reserved = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="confirmed")
