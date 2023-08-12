#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S50_database --

"""
from . import S21_path as path


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S50_database.py ends here
