# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


# `factory.Faker("pyint")` is a random integer ranges from 0 to 9999, so it
# will be good enough for every integer-related field.


def build_bigintegerfield(field_cls):
    return factory.Faker("pyint")


def build_decimalfield(field_cls):
    characteristic = field_cls.max_digits - field_cls.decimal_places
    mantissa = field_cls.decimal_places

    return factory.Faker(
        "pydecimal",
        left_digits=characteristic,
        right_digits=mantissa,
    )


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
