# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import OptionDefault
from factory.django import DjangoOptions

from autofactory.django import compat
from autofactory.django.introspector import DjangoIntrospector


class DjangoAutoOptions(DjangoOptions):
    _introspector_class = DjangoIntrospector

    @property
    def declarations(self):
        if self.abstract:
            return super(DjangoAutoOptions, self).declarations

        declarations = super(DjangoAutoOptions, self).declarations
        declarations.update(self.get_autodeclarations(declarations))

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
        not_blank_fields = self._get_not_blank_fields(all_fields)

        if self.autofields == "__all__":
            return not_blank_fields

        if self.autoexclude:
            return filter(
                lambda x: x.name not in self.autoexclude,
                not_blank_fields,
            )

        return filter(lambda x: x.name in self.autofields, all_fields)

    def _build_default_options(self):
        return super(DjangoAutoOptions, self)._build_default_options() + [
            OptionDefault("autofields", tuple(), inherit=True),
            OptionDefault("autoexclude", tuple(), inherit=True),
        ]

    def _fill_from_meta(self, meta, base_meta):
        super(DjangoAutoOptions, self)._fill_from_meta(meta, base_meta)

        assert not (self.autofields and self.autoexclude), (
            "Cannot set 'autofields' and 'autoexclude' at the same time"
        )

    def _get_all_fields(self):
        return compat.get_all_fields(self.model)

    def _get_not_blank_fields(self, fields):
        return compat.get_not_blank_fields(fields)
