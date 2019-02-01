# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

from django.db import models


class One(models.Model):
    bigintegerfield = models.BigIntegerField()
    binaryfield = models.BinaryField()
    booleanfield = models.BooleanField()
    charfield = models.CharField(max_length=50)
    datefield = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(max_digits=5, decimal_places=2)
    durationfield = models.DurationField()
    emailfield = models.EmailField()
    # filefield = models.FileField()
    filepathfield = models.FilePathField()
    floatfield = models.FloatField()
    # imagefield = models.ImageField()
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
    foreignkey = models.ForeignKey("Two", on_delete=models.CASCADE)
    # manytomany = models.ManyToManyField("Two")
    onetoone = models.OneToOneField("Two", on_delete=models.CASCADE)

    class Meta:
        app_label = "app"


class Two(models.Model):
    class Meta:
        app_label = "app"
