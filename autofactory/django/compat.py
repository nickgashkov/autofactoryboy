# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from django.db import models


def get_all_fields(model):
    return model._meta._get_fields(reverse=False)


def get_generic_fields():
    return [
        models.AutoField,
        models.BigAutoField,
        models.ManyToOneRel,
        models.ManyToManyRel,
    ]


def get_related_model(field_cls):
    return field_cls.remote_field.model


def get_not_blank_fields(fields):
    boolean_fields = {
        models.BooleanField,
        models.NullBooleanField,
    }

    return [f for f in fields if f.__class__ in boolean_fields or not f.blank]
