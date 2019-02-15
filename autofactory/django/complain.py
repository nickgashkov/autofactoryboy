# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django import compat


def on_circular_dependency(func):
    def wrapper(field_cls):
        model = field_cls.model

        related_model = compat.get_related_model(field_cls)
        related_model_fields = compat.get_all_fields(related_model)

        for related_model_field in related_model_fields:
            remote_field = related_model_field.remote_field
            remote_field_model = remote_field and remote_field.model

            if remote_field_model is model:
                raise RuntimeError(
                    "Cannot build factories with circular "
                    "dependencies. If {model}.{field} is nullable, add "
                    "{field} = None to the factory.".format(
                        model=model.__name__,
                        field=field_cls.name
                    )
                )

        return func(field_cls)

    return wrapper
