# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_booleanfield(field_cls):
    return factory.Faker('pybool')


def build_nullbooleanfield(field_cls):
    return factory.Faker('null_boolean')
