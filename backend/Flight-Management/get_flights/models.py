from flask_sqlalchemy import SQLAlchemy

db_postgres = SQLAlchemy()

class Flight(db_postgres.Model):
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
