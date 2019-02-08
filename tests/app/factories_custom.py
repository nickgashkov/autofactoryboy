# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django import DjangoModelAutoFactory
from autofactory.django.registry import registry

from tests.app.models import CustomCharField, CustomBuilderField


@registry.register(CustomCharField)
def build_custom_char_field(field_cls):
    return "CUSTOM_FIELD"


class CustomBuilderFieldFactory(DjangoModelAutoFactory):
    class Meta:
        model = CustomBuilderField
        fields = "__all__"
