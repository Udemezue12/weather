import os
from .common import *
from decouple import config

SECRET_KEY = config['SECRET_KEY']


DEBUG = False

ALLOWED_HOSTS = ['https://weather-66jg.onrender.com/']

