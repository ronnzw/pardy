import os
from dotenv import load_dotenv
from .base import *


load_dotenv()


SECRET_KEY = os.getenv("PROD_SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','https://pardymobilemechanics.co.za']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}