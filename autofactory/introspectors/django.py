# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from django.db import models

from autofactory.autofactory import builders


class DjangoIntrospector(object):
    def __init__(self, model):
        self.model = model

    def build_all(self, fields):
        declarations = dict()

        for field in filter(self._is_concrete_field, fields):
            declarations[field.name] = self.build(field)

        return declarations

    def build(self, field):
        builder = self.get_builder(field)
        built = builder and builder(field)

        return built

    def get_builder(self, field):
        builder = self.get_case_builder(field)

        if builder is not None:
            return builder

        return self.get_generic_builder(field)

    def get_case_builder(self, field):
        if field.choices:
            return builders.casebuild_from_choices

        return None

    def get_generic_builder(self, field):
        field_cls = type(field)

        builder_name = "build_" + field_cls.__name__.lower()
        builder = getattr(builders, builder_name, None)

        if builder is None:
            raise TypeError("'{field_cls}' is not supported.".format(field_cls=field_cls.__name__))

        return builder

    def _is_concrete_field(self, field):
        return field.__class__ not in [
            models.AutoField,
            models.BigAutoField,
            models.ManyToOneRel,
            models.ManyToManyRel,
        ]
