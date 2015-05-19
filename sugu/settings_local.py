#!/usr/bin/env python
# encoding=utf-8


import settings

settings.DEBUG = True

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sugu.sqlite3',
    }
}

# change that one!
settings.SECRET_KEY = '___(-_-)___'
