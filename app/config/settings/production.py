from .base import *

SECRETS = SECRETS_FULL['production']

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.production.application'
DATABASES = SECRETS['DATABASES']
ALLOWED_HOSTS += [
    'lhy.kr',
]
INSTALLED_APPS += [

]

# Storage
AWS_STORAGE_BUCKET_NAME = 'wps-instagram-lhy-production'
