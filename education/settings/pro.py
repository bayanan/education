from .base import *


DEBUG = False

ADMINS = (
    ('admin', 'admin@mail.ru'),
)

ALLOWED_HOSTS = ['.educationproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '123456'
    }
}

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
