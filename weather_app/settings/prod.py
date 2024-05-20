import os
import logging
import dj_database_url
from weather_app.settings.common import *

# Setup logging to print debug information
logger = logging.getLogger('django')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Log environment variables
logger.debug(f'SECRET_KEY: {os.environ.get("SECRET_KEY")}')
logger.debug(f'PORT: {os.environ.get("PORT")}')
logger.debug(f'DATABASE_URL: {os.getenv("DATABASE_URL")}')

SECRET_KEY = os.environ['SECRET_KEY']
PORT = int(os.environ.get('PORT', 8080))

DATABASE_URL = os.getenv('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL)

DATABASES = {
    'default': db_from_env,
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
}

DEBUG = False

ALLOWED_HOSTS = ["weather-n8j3.onrender.com", "weather-checker-app-550b9b073733.herokuapp.com"]
