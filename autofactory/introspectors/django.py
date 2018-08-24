# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

# TODO: Raise detailed error if Django is not installed.
from django.db import models

from autofactory.autofactory.declarators.text import declare_text_field


class DjangoIntrospector(object):
    def __init__(self, model):
        self.model = model

    def declare(self, field_attname):
        return None

    def get_declarator(self, field_attname):
        # TODO: Compatibility with older Django versions.
        field = self.model.get_field(field_attname)
        field_cls = type(field)

        declarator_mapping = self.get_declarator_mapping()
        declarator = declarator_mapping.get(field_cls)

        if declarator is None:
            raise TypeError("'{field_cls}' is not supported.".format(field_cls=field_cls.__name__))

        return declarator

    def get_declarator_mapping(self):
        return {
            models.TextField: declare_text_field,
        }
