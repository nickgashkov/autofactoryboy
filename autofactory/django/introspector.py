# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django import builders, compat


class DjangoIntrospector(object):
    def __init__(self, model):
        self.model = model
        self.registry = builders.registry

    def build_all(self, fields):
        declarations = dict()

        for field in compat.get_concrete_fields(fields):
            declarations[field.name] = self.build(field)

        return declarations

    def build(self, field):
        builder = self.get_builder(field)
        built = builder and builder(field)

        return built

    def get_builder(self, field):
        builder = self._get_concrete_builder(field)

        if builder is not None:
            return builder

        return self._get_generic_builder(field)

    def _get_concrete_builder(self, field):
        if field.has_default():
            return self.registry.get(builders.FROM_DEFAULT)

        if getattr(field, "choices", tuple()):
            return self.registry.get(builders.FROM_CHOICES)

        return None

    def _get_generic_builder(self, field):
        field_cls = type(field)
        field_builder = self.registry.get(field_cls)

        if field_builder is None:
            raise TypeError(
                "AutoFactoryBoy cannot generate '{model}.{field}', "
                "'{field_cls}' is not supported.".format(
                    model=self.model.__name__,
                    field=field.name,
                    field_cls=field_cls.__name__,
                )
            )

        return field_builder
