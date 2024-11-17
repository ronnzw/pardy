import os
from dotenv import load_dotenv
from .base import *


load_dotenv()


SECRET_KEY = os.getenv("LOCAL_SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}