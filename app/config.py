import os 
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')
secret_key = os.getenv('SECRET_KEY')

if not username or password == None or not database or not host  or not secret_key:
    raise ValueError("One or more environment variables are missing")


class AppConfigrations:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secret_key
    