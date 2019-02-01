# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import FactoryMetaClass

from autofactory.django.factory import DjangoModelAutoFactory


def build_django_autofactory(model_cls):
    class Meta:
        model = model_cls
        fields = "__all__"

    factory_cls_name = "Generated" + model_cls.__name__ + "Factory"
    factory_cls_name = str(factory_cls_name)

    return FactoryMetaClass(factory_cls_name, [DjangoModelAutoFactory], {"Meta": Meta})
