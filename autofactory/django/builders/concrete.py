# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory
from factory import fuzzy


def from_choices(field_cls):
    return fuzzy.FuzzyChoice([c[0] for c in field_cls.choices])


def from_default(field_cls):
    if callable(field_cls.default):
        return factory.LazyFunction(field_cls.default)

    return field_cls.default
