import os
import pymysql
import dj_database_url
from decouple import config 
from dotenv import load_dotenv
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper
from .common import *


pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()

load_dotenv()


SECRET_KEY = config('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['weather-j269.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://weather-j269.onrender.com']





DATABASES = {
    'default': dj_database_url.config(default='sqlite:///:memory:')
}

if os.getenv('DB_URL'):
    db_from_env = dj_database_url.config(default=os.getenv('DB_URL'))
    DATABASES['default'].update(db_from_env)
else:
    DATABASES['default']['ENGINE'] = os.getenv('DB_ENGINE', DATABASES['default']['ENGINE'])
    DATABASES['default']['NAME'] = os.getenv('DB_NAME', DATABASES['default']['NAME'])
    DATABASES['default']['USER'] = os.getenv('DB_USER', DATABASES['default']['USER'])
    DATABASES['default']['PASSWORD'] = os.getenv('DB_PASSWORD', DATABASES['default']['PASSWORD'])
    DATABASES['default']['HOST'] = os.getenv('DB_HOST', DATABASES['default']['HOST'])
    DATABASES['default']['PORT'] = os.getenv('DB_PORT', DATABASES['default']['PORT'])



# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE'),
#         'NAME': config('DB_NAME'),
#         'HOST': config('DB_HOST'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'USER': config('DB_USER'),
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },

#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }

# CELERY_BROKER_URL = 'redis://localhost:6379/1'

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/2',
#         'TIMEOUT': 10 * 60,
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# EMAIL_PORT = config('EMAIL_PORT', default='', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')

