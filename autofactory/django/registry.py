from django.db import models

from autofactory.core.registry import Registry
from autofactory.django import builders


FROM_CHOICES = object()
FROM_DEFAULT = object()


registry = Registry()

registry.register(FROM_CHOICES, builders.from_choices)
registry.register(FROM_DEFAULT, builders.from_default)

registry.register(models.BooleanField, builders.build_booleanfield)
registry.register(models.NullBooleanField, builders.build_nullbooleanfield)
registry.register(models.DateField, builders.build_datefield)
registry.register(models.DateTimeField, builders.build_datetimefield)
registry.register(models.DurationField, builders.build_durationfield)
registry.register(models.TimeField, builders.build_timefield)
registry.register(models.BinaryField, builders.build_binaryfield)
registry.register(models.FileField, builders.build_filefield)
registry.register(models.FilePathField, builders.build_filepathfield)
registry.register(models.ImageField, builders.build_imagefield)
registry.register(models.BigIntegerField, builders.build_bigintegerfield)
registry.register(models.DecimalField, builders.build_decimalfield)
registry.register(models.FloatField, builders.build_floatfield)
registry.register(models.IntegerField, builders.build_integerfield)
registry.register(models.PositiveIntegerField, builders.build_positiveintegerfield)
registry.register(models.PositiveSmallIntegerField, builders.build_positivesmallintegerfield)
registry.register(models.SmallIntegerField, builders.build_smallintegerfield)
registry.register(models.ForeignKey, builders.build_foreignkey)
registry.register(models.ManyToManyField, builders.build_manytomanyfield)
registry.register(models.OneToOneField, builders.build_onetoonefield)
registry.register(models.CharField, builders.build_charfield)
registry.register(models.EmailField, builders.build_emailfield)
registry.register(models.GenericIPAddressField, builders.build_genericipaddressfield)
registry.register(models.SlugField, builders.build_slugfield)
registry.register(models.TextField, builders.build_textfield)
registry.register(models.URLField, builders.build_urlfield)
registry.register(models.UUIDField, builders.build_uuidfield)
