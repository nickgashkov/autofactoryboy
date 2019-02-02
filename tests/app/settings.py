# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import os

SECRET_KEY = "test"


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, "files")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}


INSTALLED_APPS = [
    "tests.app"
]


MIDDLEWARE_CLASSES = []
