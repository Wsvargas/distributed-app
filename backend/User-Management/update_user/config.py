<<<<<<< HEAD
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@db:5432/users_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@db:5432/users_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> origin/WILLIAN
