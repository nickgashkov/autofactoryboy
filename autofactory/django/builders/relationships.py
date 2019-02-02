# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory

from autofactory.django.compat import get_related_model
from autofactory.django.shortcuts import build_django_autofactory


def build_foreignkey(field_cls):
    model = get_related_model(field_cls)
    model_factory = build_django_autofactory(model)

    return factory.SubFactory(model_factory)


def build_manytomanyfield(field_cls):
    model_factory = build_django_autofactory(get_related_model(field_cls))

    def builder(obj, create, _extracted, **_kwargs):
        if not create:
            return

        manager = getattr(obj, field_cls.name)
        manager.add(*model_factory.create_batch(2))

    return factory.PostGeneration(builder)


def build_onetoonefield(field_cls):
    model = get_related_model(field_cls)
    model_factory = build_django_autofactory(model)

    return factory.SubFactory(model_factory)
