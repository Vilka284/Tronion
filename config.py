from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = False
    SECRET_KEY = environ.get("SECRET_KEY")


class DatabaseConfig(object):
    DATABASE_HOST = environ.get("DATABASE_HOST")
    DATABASE_USERNAME = environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
    DATABASE_NAME = environ.get("DATABASE_NAME")
    DATABASE_PORT = environ.get("DATABASE_PORT")

