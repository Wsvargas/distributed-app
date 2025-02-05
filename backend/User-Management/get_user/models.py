from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(200), nullable=False) 
    date_of_birth = db.Column(db.Date, nullable=True)
    role = db.Column(db.String(50), nullable=False, default='user')
    is_active = db.Column(db.Boolean, default=True)