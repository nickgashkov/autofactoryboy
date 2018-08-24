# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import OptionDefault
from factory.django import DjangoOptions

from autofactory.autofactory.introspectors.django import DjangoIntrospector


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
        autodeclarations = dict()
        introspecter = self.get_introspector()

        autofields = self.get_fields_to_autodeclare()
        autofields = [f for f in autofields if f not in declarations]

        for field_attname in autofields:
            autodeclarations[field_attname] = introspecter.declare(field_attname)

        return autodeclarations

    def get_fields_to_autodeclare(self):
        if self.fields == "__all__":
            # TODO: Make compatibility with previous Django versions.
            return [f.name for f in self.model._meta.get_fields()]

        return self.fields

    def _build_default_options(self):
        return super(DjangoAutoOptions, self)._build_default_options() + [
            OptionDefault("fields", tuple(), inherit=True),
        ]
