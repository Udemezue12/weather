import os

import dj_database_url
from .common import *
from decouple import config

SECRET_KEY = os.environ['SECRET_KEY']

DATABASE_URL = os.getenv('DATABASE_URL')

PORT = int(os.environ.get('PORT', 8080))

db_from_env = dj_database_url.config(default=DATABASE_URL)

DEBUG = False

ALLOWED_HOSTS = ["https://weather-n8j3.onrender.com", "https://weather-checker-app-550b9b073733.herokuapp.com/"]


DATABASES = {
    'default': db_from_env,
    'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
}
