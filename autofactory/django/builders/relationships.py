# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import factory

from autofactory.utils.compat.django_ import get_related_model
from autofactory.utils.shortcuts.build import build_django_autofactory


def build_foreignkey(field_cls):
    model = get_related_model(field_cls)
    model_factory = build_django_autofactory(model)

    return factory.SubFactory(model_factory)


def build_manytomanyfield(field_cls):
    raise NotImplementedError("M2M fields are not supported yet.")


def build_onetoonefield(field_cls):
    model = get_related_model(field_cls)
    model_factory = build_django_autofactory(model)

    return factory.SubFactory(model_factory)
