# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django import compat


class DjangoIntrospector(object):
    def __init__(self, model, registry):
        self.model = model
        self.registry = registry

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
        builder = self._get_concrete_builder(field)

        if builder is not None:
            return builder

        return self._get_generic_builder(field)

    def _get_concrete_builder(self, field):
        if getattr(field, "choices", tuple()):
            return self.registry.builder_from_choices

        if field.has_default():
            return self.registry.builder_from_default

        return None

    def _get_generic_builder(self, field):
        field_cls = type(field)
        field_builder = self.registry.builder_mapping.get(field_cls)

        if field_builder is None:
            raise TypeError(
                "'{field_cls}' is not supported.".format(
                    field_cls=field_cls.__name__,
                )
            )

        return field_builder

    def _is_concrete_field(self, field):
        return field.__class__ not in compat.get_generic_fields()
