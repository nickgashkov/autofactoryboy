# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import OptionDefault
from factory.django import DjangoOptions

from autofactory.django.introspector import DjangoIntrospector
from autofactory.django import compat


class DjangoAutoOptions(DjangoOptions):
    _introspector_class = DjangoIntrospector

    @property
    def declarations(self):
        declarations = super(DjangoAutoOptions, self).declarations
        declarations.update(self.get_autodeclarations(declarations=declarations))

        return declarations

    def get_introspector(self):
        return self._introspector_class(self.model)

    def get_autodeclarations(self, declarations):
        introspecter = self.get_introspector()

        autofields = self.get_fields_to_autodeclare()
        autofields = [f for f in autofields if f.name not in declarations]

        return introspecter.build_all(autofields)

    def get_fields_to_autodeclare(self):
        all_fields = self._get_all_fields()

        if self.fields == "__all__":
            return all_fields

        return filter(lambda x: x.name in self.fields, all_fields)

    def _build_default_options(self):
        return super(DjangoAutoOptions, self)._build_default_options() + [
            OptionDefault("fields", tuple(), inherit=True),
        ]

    def _get_all_fields(self):
        return compat.get_all_fields(self.model)
