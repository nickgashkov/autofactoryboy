# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory import fuzzy


def from_choices(field_cls):
    return fuzzy.FuzzyChoice(field_cls.choices)


def from_default(field_cls):
    return field_cls.default
