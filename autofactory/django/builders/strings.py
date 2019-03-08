# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_charfield(field_cls):
    # FAQ: `pystr` is used insted of `text` because `text` provider may
    # contain newlines. For a text-like data `TextField` should be used.
    return factory.Faker("pystr", max_chars=field_cls.max_length)


def build_emailfield(field_cls):
    return factory.Faker("email")


def build_genericipaddressfield(field_cls):
    return factory.Faker("ipv4")


def build_slugfield(field_cls):
    return factory.Faker("slug")


def build_textfield(field_cls):
    if field_cls.max_length is not None:
        return factory.Faker("text", max_nb_chars=field_cls.max_length)

    return factory.Faker("text")


def build_urlfield(field_cls):
    return factory.Faker("url")


def build_uuidfield(field_cls):
    return factory.Faker("uuid4")
