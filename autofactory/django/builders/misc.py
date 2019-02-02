# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory


def build_binaryfield(field_cls):
    return factory.Faker("binary", length=(1 * 1024))


def build_filefield(field_cls):
    return factory.django.FileField()


def build_filepathfield(field_cls):
    return factory.Faker("file_path")


def build_imagefield(field_cls):
    return factory.django.ImageField()
