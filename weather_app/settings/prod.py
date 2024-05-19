import os
from .common import *
from decouple import config

SECRET_KEY = os.environ['SECRET_KEY']


DEBUG = False

ALLOWED_HOSTS = ["https://weather-n8j3.onrender.com"]

