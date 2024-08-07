import os
import dj_database_url
from decouple import config
from dotenv import load_dotenv
from .common import *


# pymysql.version_info = (1, 4, 13, "final", 0)
# pymysql.install_as_MySQLdb()

# load_dotenv()


DEBUG = True
ALLOWED_HOSTS = []


load_dotenv()


PASSWORD_RESET_TIMEOUT = 350


SECRET_KEY = os.getenv('SECRET_KEY')


# DATABASES = {
#     'default': dj_database_url.config(default='sqlite:///:memory:')
# }

# if os.getenv('DB_URL'):
#     db_from_env = dj_database_url.config(default=os.getenv('DB_URL'))
#     DATABASES['default'].update(db_from_env)
# else:
#     DATABASES['default']['ENGINE'] = os.getenv('DB_ENGINE', DATABASES['default']['ENGINE'])
#     DATABASES['default']['NAME'] = os.getenv('DB_NAME', DATABASES['default']['NAME'])
#     DATABASES['default']['USER'] = os.getenv('DB_USER', DATABASES['default']['USER'])
#     DATABASES['default']['PASSWORD'] = os.getenv('DB_PASSWORD', DATABASES['default']['PASSWORD'])
#     DATABASES['default']['HOST'] = os.getenv('DB_HOST', DATABASES['default']['HOST'])
#     DATABASES['default']['PORT'] = os.getenv('DB_PORT', DATABASES['default']['PORT'])


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '3306'),  # Default port for MySQL is 3306
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

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

# dev.py


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_FROM')
EMAIL_TIMEOUT = 120
