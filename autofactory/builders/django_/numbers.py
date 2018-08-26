# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_bigintegerfield(field_cls):
    return factory.Faker("pyint")


def build_decimalfield(field_cls):
    return factory.Faker("pydecimal")


def build_floatfield(field_cls):
    return factory.Faker("pyfloat")


def build_integerfield(field_cls):
    return factory.Faker("pyint")


def build_positiveintegerfield(field_cls):
    return factory.Faker("pyint")


def build_positivesmallintegerfield(field_cls):
    return factory.Faker("pyint")


def build_smallintegerfield(field_cls):
    return factory.Faker("pyint")
