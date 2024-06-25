import os

DB_URL = "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(DB_USER = os.getenv("DB_USER"),DB_PASSWORD = os.getenv("DB_PASSWORD"),DB_HOST = os.getenv("DB_HOST"),DB_NAME = os.getenv("DB_NAME"))

class Config:
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False