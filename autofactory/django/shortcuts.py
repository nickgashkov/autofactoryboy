# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import FactoryMetaClass


def build_django_autofactory(model_cls, **kwargs):
    from autofactory.django.factory import DjangoModelAutoFactory

    class Meta:
        model = model_cls
        fields = "__all__"

    factory_cls_name = "Generated" + model_cls.__name__ + "Factory"
    factory_cls_name = str(factory_cls_name)

    factory_attrs = kwargs.copy()
    factory_attrs["Meta"] = Meta

    return FactoryMetaClass(
        factory_cls_name,
        (DjangoModelAutoFactory,),
        factory_attrs,
    )
