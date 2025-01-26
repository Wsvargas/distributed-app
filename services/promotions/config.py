import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/promotions"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
