from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopio',
        'USER': 'shopio',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': 'db',
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['location'] = REDIS_URL