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
    }
]

# TODO Make all these working dynamically in tests.py
COOL_PAGINATOR_SIZE = 'SMALL'
COOL_PAGINATOR_NEXT_NAME = 'Go'
COOL_PAGINATOR_PREVIOUS_NAME = 'Previous'
COOL_PAGINATOR_PARAM_NAME = 'page'
