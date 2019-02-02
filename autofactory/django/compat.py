# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import django.db.models

django_version = django.VERSION[:2]


def get_all_fields(model):
    if django_version >= (1, 8):
        return model._meta._get_fields(reverse=False)

    return [
        field for field, __ in model._meta.get_fields_with_model()
    ] + [
        field for field, __ in model._meta.get_m2m_with_model()
    ]


def get_generic_fields():
    generic_fields = [
        django.db.models.AutoField,
        django.db.models.ManyToOneRel,
        django.db.models.ManyToManyRel,
    ]

    if django_version >= (2, 0):
        generic_fields.append(django.db.models.BigAutoField)

    return generic_fields


def get_related_model(field_cls):
    if django_version >= (2, 0):
        return field_cls.remote_field.model

    return field_cls.rel.to
