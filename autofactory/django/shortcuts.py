# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django.maker import make_django_autofactory


def autofactory(instance):
    return make_django_autofactory(instance)
