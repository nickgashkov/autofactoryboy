# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory import random


def from_choices(field_cls):
    random_choice_tuple = random.randgen.choice(field_cls.choices)
    random_choice = random_choice_tuple[0]

    return random_choice
