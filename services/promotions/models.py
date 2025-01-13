from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, default=True)
