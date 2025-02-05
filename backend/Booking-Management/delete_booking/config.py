import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:D1str1bu1D4.@booking-management-db.c7u4ume2skf9.us-east-1.rds.amazonaws.com:5432/booking_management'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False