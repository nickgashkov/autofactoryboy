# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import datetime

from django.db import models


class CustomCharField(models.CharField):
    pass


class EveryFieldType(models.Model):
    bigintegerfield = models.BigIntegerField()
    binaryfield = models.BinaryField()
    booleanfield = models.BooleanField()
    charfield = models.CharField(max_length=50)
    datefield = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(max_digits=5, decimal_places=2)
    durationfield = models.DurationField()
    emailfield = models.EmailField()
    filefield = models.FileField(upload_to='files/')
    filepathfield = models.FilePathField()
    floatfield = models.FloatField()
    imagefield = models.ImageField(upload_to='images/')
    integerfield = models.IntegerField()
    genericipaddressfield = models.GenericIPAddressField()
    nullbooleanfield = models.NullBooleanField()
    positiveintegerfield = models.PositiveIntegerField()
    positivesmallintegerfield = models.PositiveSmallIntegerField()
    slugfield = models.SlugField()
    smallintegerfield = models.SmallIntegerField()
    textfield = models.TextField()
    timefield = models.TimeField()
    urlfield = models.URLField()
    uuidfield = models.UUIDField()
    foreignkey = models.ForeignKey("WithDeclaredField", on_delete=models.CASCADE)
    manytomany = models.ManyToManyField("WithDeclaredField")
    onetoone = models.OneToOneField("WithBlankField", on_delete=models.CASCADE)

    class Meta:
        app_label = "app"


class WithDeclaredField(models.Model):
    declared_integer = models.IntegerField()
    autodeclared_integer = models.IntegerField()

    class Meta:
        app_label = "app"


class WithBlankField(models.Model):
    can_be_blank = models.IntegerField(blank=True, null=True)
    cannot_be_blank = models.IntegerField(null=True)

    class Meta:
        app_label = "app"


class WithCustomThrough(models.Model):
    custom_through_m2m = models.ManyToManyField("WithBlankField", through="CustomThrough")

    class Meta:
        app_label = "app"


class CustomThrough(models.Model):
    with_custom_through = models.ForeignKey("WithCustomThrough", on_delete=models.CASCADE)
    with_blank_field = models.ForeignKey("WithBlankField", on_delete=models.CASCADE)

    non_blank_field = models.CharField(max_length=100)

    class Meta:
        app_label = "app"


class WithDefault(models.Model):
    string = models.TextField()
    string_with_default = models.TextField(default="DEFAULT")

    class Meta:
        app_label = "app"


class WithChoiceField(models.Model):
    CHOICES = (
        ("__CHOICE_ONE_VALUE__", "__CHOICE_ONE_HUMAN_NAME__"),
        ("__CHOICE_TWO_VALUE__", "__CHOICE_TWO_HUMAN_NAME__"),
    )

    string_with_choices = models.CharField(max_length=500, choices=CHOICES)

    class Meta:
        app_label = "app"


class CustomBuilderField(models.Model):
    custom = CustomCharField(max_length=200)

    class Meta:
        app_label = "app"


def beginning_of_time():
    return datetime.datetime.fromtimestamp(0)


class WithDefaultCallable(models.Model):
    datetime_with_default_callable = models.DateTimeField(default=beginning_of_time)

    class Meta:
        app_label = "app"


class WithExclude(models.Model):
    field = models.IntegerField(blank=False, null=True)
    excluded_field = models.IntegerField(blank=False, null=True)

    class Meta:
        app_label = "app"


class WithDefaultAndChoices(models.Model):
    CHOICES = (
        (1, "CHOICE_ONE"),
        (2, "CHOICE_TWO"),
        (3, "CHOICE_THREE"),
    )

    field = models.IntegerField(
        blank=False,
        null=True,
        choices=CHOICES,
        default=4,
    )

    class Meta:
        app_label = "app"


class One(models.Model):
    two = models.ForeignKey("Two", on_delete=models.CASCADE)

    class Meta:
        app_label = "app"


class Two(models.Model):
    one = models.ForeignKey("One", on_delete=models.CASCADE)

    class Meta:
        app_label = "app"
