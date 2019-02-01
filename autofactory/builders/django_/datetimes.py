# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_datefield(field_cls):
    return factory.Faker('date_this_decade')


def build_datetimefield(field_cls):
    return factory.Faker('date_time')


def build_durationfield(field_cls):
    return factory.Faker('time_delta')


def build_timefield(field_cls):
    return factory.Faker('time_object')
