# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from autofactory.django import DjangoModelAutoFactory
from tests.app.models import (
    EveryFieldType, WithDeclaredField, WithBlankField,
    WithCustomThrough, WithDefault, WithChoiceField,
    WithExclude, WithDefaultAndChoices
)


class EveryFieldTypeFactory(DjangoModelAutoFactory):
    class Meta:
        model = EveryFieldType
        autofields = (
            "bigintegerfield",
            "binaryfield",
            "booleanfield",
            "charfield",
            "datefield",
            "datetimefield",
            "decimalfield",
            "durationfield",
            "emailfield",
            "filefield",
            "filepathfield",
            "floatfield",
            "imagefield",
            "integerfield",
            "genericipaddressfield",
            "nullbooleanfield",
            "positiveintegerfield",
            "positivesmallintegerfield",
            "slugfield",
            "smallintegerfield",
            "textfield",
            "timefield",
            "urlfield",
            "uuidfield",
            "foreignkey",
            "manytomany",
            "onetoone",
        )


class WithoutBlankEveryFieldTypeFactory(DjangoModelAutoFactory):
    class Meta:
        model = EveryFieldType
        autofields = "__all__"


class WithDeclaredFieldFactory(DjangoModelAutoFactory):
    declared_integer = -42

    class Meta:
        model = WithDeclaredField
        autofields = "__all__"


class WithBlankFieldAndAllFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithBlankField
        autofields = "__all__"


class WithBlankFieldAndNotAllFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithBlankField
        autofields = ("can_be_blank", "cannot_be_blank")


class WithBlankFieldAndExcludeFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithBlankField
        autoexclude = ("cannot_be_blank",)


class WithCustomThroughFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithCustomThrough
        autofields = ("custom_through_m2m",)


class WithDefaultAllFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithDefault
        autofields = "__all__"


class WithDefaultTupleFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithDefault
        autofields = ("string", "string_with_default")


class WithChoiceFieldFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithChoiceField
        autofields = "__all__"


class WithExcludeFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithExclude
        autoexclude = ("excluded_field",)


class WithoutExcludeFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithExclude
        autofields = "__all__"


class WithDefaultAndChoicesFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithDefaultAndChoices
        autofields = "__all__"
