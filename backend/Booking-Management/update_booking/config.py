<<<<<<< HEAD
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@db_postgres:5432/booking_management'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@db_postgres:5432/booking_management'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> origin/WILLIAN
