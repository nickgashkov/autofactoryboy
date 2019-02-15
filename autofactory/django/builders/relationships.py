# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory

from autofactory.django import complain
from autofactory.django.compat import get_related_model
from autofactory.django.maker import make_django_autofactory


@complain.on_circular_dependency
def build_foreignkey(field_cls):
    model = get_related_model(field_cls)
    model_factory = make_django_autofactory(model)

    return factory.SubFactory(model_factory)


@complain.on_circular_dependency
def build_manytomanyfield(field_cls):
    field_descriptor = getattr(field_cls.model, field_cls.name)
    field_through = field_descriptor.through

    if not field_through._meta.auto_created:
        return _build_manytomanyfield_with_a_through(field_cls)

    model_factory = make_django_autofactory(get_related_model(field_cls))

    def builder(obj, create, _extracted, **_kwargs):
        if not create:
            return

        manager = getattr(obj, field_cls.name)
        manager.add(*model_factory.create_batch(2))

    return factory.PostGeneration(builder)


@complain.on_circular_dependency
def build_onetoonefield(field_cls):
    model = get_related_model(field_cls)
    model_factory = make_django_autofactory(model)

    return factory.SubFactory(model_factory)


def _build_manytomanyfield_with_a_through(field_cls):
    field_descriptor = getattr(field_cls.model, field_cls.name)
    field_through = field_descriptor.through

    field_through_factory = make_django_autofactory(field_through, **{field_cls.m2m_field_name(): None})

    return factory.RelatedFactory(field_through_factory, field_cls.m2m_field_name())
