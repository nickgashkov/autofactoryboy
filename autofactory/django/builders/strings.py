# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_charfield(field_cls):
    return factory.Faker("pystr", max_chars=field_cls.max_length)


def build_emailfield(field_cls):
    return factory.Faker("email")


def build_genericipaddressfield(field_cls):
    return factory.Faker("ipv4")


def build_slugfield(field_cls):
    return factory.Faker("slug")


def build_textfield(field_cls):
    return factory.Faker("text")


def build_urlfield(field_cls):
    return factory.Faker("url")


def build_uuidfield(field_cls):
    return factory.Faker("uuid4")
