import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'tests',
    'django_cool_paginator'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }
]

# TODO Make all these working dynamically in tests.py
COOL_PAGINATOR_SIZE = 'LARGE'
COOL_PAGINATOR_NEXT_NAME = 'Next'
