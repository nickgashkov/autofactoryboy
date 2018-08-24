# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory import DjangoModelFactory

from autofactory.autofactory.options.django import DjangoAutoOptions


class DjangoModelAutoFactory(DjangoModelFactory):
    _options_class = DjangoAutoOptions
