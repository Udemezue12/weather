import os
import logging
import dj_database_url
from weather_app.settings.common import *

logger = logging.getLogger('django')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug(f'PORT: {os.environ.get("PORT")}')
logger.debug(f'SECRET_KEY: {os.environ.get("SECRET_KEY")}')
logger.debug(f'DATABASE_URL: {os.getenv("DATABASE_URL")}')

PORT = int(os.environ.get('PORT', 8080))
SECRET_KEY = os.environ['SECRET_KEY']

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
CSRF_TRUSTED_ORIGINS = [
    'https://weather-checker-app-550b9b073733.herokuapp.com',
    'https://weather-n8j3.onrender.com'
]


