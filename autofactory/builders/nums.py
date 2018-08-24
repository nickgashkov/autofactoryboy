# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from decimal import Decimal


def build_bigintegerfield(field_cls):
    return 1


def build_decimalfield(field_cls):
    return Decimal('1')


def build_floatfield(field_cls):
    return 1.0


def build_integerfield(field_cls):
    return 1


def build_positiveintegerfield(field_cls):
    return 1


def build_positivesmallintegerfield(field_cls):
    return 1


def build_smallintegerfield(field_cls):
    return 1
