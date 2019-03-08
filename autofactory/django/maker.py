# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from factory.base import FactoryMetaClass


def make_django_autofactory(model_cls, use_cache=True, **kwargs):
    if use_cache:
        return _make_django_autofactory_cached(model_cls, **kwargs)

    return _make_django_autofactory(model_cls, **kwargs)


_cache = dict()


def _make_django_autofactory_cached(model_cls, **kwargs):
    if model_cls not in _cache:
        _cache[model_cls] = _make_django_autofactory(model_cls, **kwargs)

    return _cache[model_cls]


def _make_django_autofactory(model_cls, **kwargs):
    from autofactory.django.factories import DjangoModelAutoFactory

    class Meta:
        model = model_cls
        autofields = "__all__"

    factory_cls_name = model_cls.__name__ + "Factory"
    factory_cls_name = str(factory_cls_name)

    factory_bases = (DjangoModelAutoFactory,)

    factory_attrs = kwargs.copy()
    factory_attrs["Meta"] = Meta

    return FactoryMetaClass(
        factory_cls_name,
        factory_bases,
        factory_attrs,
    )
