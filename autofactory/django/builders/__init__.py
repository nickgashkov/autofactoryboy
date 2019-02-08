# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from django.db import models

from autofactory.core.registry import Registry
from autofactory.django.builders.booleans import (
    build_booleanfield,
    build_nullbooleanfield,
)
from autofactory.django.builders.concrete import from_choices, from_default
from autofactory.django.builders.datetimes import (
    build_datefield,
    build_datetimefield,
    build_durationfield,
    build_timefield,
)
from autofactory.django.builders.misc import (
    build_binaryfield,
    build_filefield,
    build_filepathfield,
    build_imagefield,
)
from autofactory.django.builders.numbers import (
    build_bigintegerfield,
    build_decimalfield,
    build_floatfield,
    build_integerfield,
    build_positiveintegerfield,
    build_positivesmallintegerfield,
    build_smallintegerfield,
)
from autofactory.django.builders.relationships import (
    build_foreignkey,
    build_manytomanyfield,
    build_onetoonefield,
)
from autofactory.django.builders.strings import (
    build_charfield,
    build_emailfield,
    build_genericipaddressfield,
    build_slugfield,
    build_textfield,
    build_urlfield,
    build_uuidfield,
)

__all__ = (
    "registry",
    "FROM_CHOICES",
    "FROM_DEFAULT",
    "from_choices",
    "from_default",
    "build_bigintegerfield",
    "build_binaryfield",
    "build_booleanfield",
    "build_charfield",
    "build_datefield",
    "build_datetimefield",
    "build_decimalfield",
    "build_durationfield",
    "build_emailfield",
    "build_filefield",
    "build_filepathfield",
    "build_floatfield",
    "build_imagefield",
    "build_integerfield",
    "build_genericipaddressfield",
    "build_nullbooleanfield",
    "build_positiveintegerfield",
    "build_positivesmallintegerfield",
    "build_slugfield",
    "build_smallintegerfield",
    "build_textfield",
    "build_timefield",
    "build_urlfield",
    "build_uuidfield",
    "build_foreignkey",
    "build_manytomanyfield",
    "build_onetoonefield",
)


FROM_CHOICES = object()
FROM_DEFAULT = object()


registry = Registry()

# Concrete builders.
registry.register(FROM_CHOICES, from_choices)
registry.register(FROM_DEFAULT, from_default)

# Generic builders.
registry.register(models.BooleanField, build_booleanfield)
registry.register(models.NullBooleanField, build_nullbooleanfield)
registry.register(models.DateField, build_datefield)
registry.register(models.DateTimeField, build_datetimefield)
registry.register(models.DurationField, build_durationfield)
registry.register(models.TimeField, build_timefield)
registry.register(models.BinaryField, build_binaryfield)
registry.register(models.FileField, build_filefield)
registry.register(models.FilePathField, build_filepathfield)
registry.register(models.ImageField, build_imagefield)
registry.register(models.BigIntegerField, build_bigintegerfield)
registry.register(models.DecimalField, build_decimalfield)
registry.register(models.FloatField, build_floatfield)
registry.register(models.IntegerField, build_integerfield)
registry.register(models.PositiveIntegerField, build_positiveintegerfield)
registry.register(models.PositiveSmallIntegerField, build_positivesmallintegerfield)
registry.register(models.SmallIntegerField, build_smallintegerfield)
registry.register(models.ForeignKey, build_foreignkey)
registry.register(models.ManyToManyField, build_manytomanyfield)
registry.register(models.OneToOneField, build_onetoonefield)
registry.register(models.CharField, build_charfield)
registry.register(models.EmailField, build_emailfield)
registry.register(models.GenericIPAddressField, build_genericipaddressfield)
registry.register(models.SlugField, build_slugfield)
registry.register(models.TextField, build_textfield)
registry.register(models.URLField, build_urlfield)
registry.register(models.UUIDField, build_uuidfield)
