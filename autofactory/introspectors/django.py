# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.autofactory import builders


class DjangoIntrospector(object):
    def __init__(self, model):
        self.model = model

    def declare(self, field_attname):
        # TODO: Compatibility with older Django versions.
        field = self.model._meta.get_field(field_attname)
        field_cls = type(field)

        builder = self.get_builder(field_cls)

        return builder and builder(field)

    def get_builder(self, field_cls):
        builder_name = "build_" + field_cls.__name__.lower()
        builder = getattr(builders, builder_name, None)

        if builder is None:
            # raise TypeError("'{field_cls}' is not supported.".format(field_cls=field_cls.__name__))
            pass

        return builder
