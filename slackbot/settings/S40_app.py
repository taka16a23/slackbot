#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S04_app --

"""

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # SessionMiddlewareの後かつCommonMiddlewareの前に記載すること
    # sessionとURL prefixesを利用するため
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

WSGI_APPLICATION = 'slackbot.wsgi.application'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S40_app.py ends here
