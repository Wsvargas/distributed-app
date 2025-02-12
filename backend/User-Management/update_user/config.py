import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@user-management-db.ctomew44ejiz.us-east-1.rds.amazonaws.com:5432/users_management'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # tcopilot