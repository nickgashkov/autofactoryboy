from django.db import models

from autofactory.django import builders


class DjangoRegistry(object):
    @property
    def builder_from_choices(self):
        return builders.from_choices

    @property
    def builder_from_default(self):
        return builders.from_default

    @property
    def builder_mapping(self):
        return {
            models.BooleanField: builders.build_booleanfield,
            models.NullBooleanField: builders.build_nullbooleanfield,
            models.DateField: builders.build_datefield,
            models.DateTimeField: builders.build_datetimefield,
            models.DurationField: builders.build_durationfield,
            models.TimeField: builders.build_timefield,
            models.BinaryField: builders.build_binaryfield,
            models.FileField: builders.build_filefield,
            models.FilePathField: builders.build_filepathfield,
            models.ImageField: builders.build_imagefield,
            models.BigIntegerField: builders.build_bigintegerfield,
            models.DecimalField: builders.build_decimalfield,
            models.FloatField: builders.build_floatfield,
            models.IntegerField: builders.build_integerfield,
            models.PositiveIntegerField: builders.build_positiveintegerfield,
            models.PositiveSmallIntegerField: builders.build_positivesmallintegerfield,
            models.SmallIntegerField: builders.build_smallintegerfield,
            models.ForeignKey: builders.build_foreignkey,
            models.ManyToManyField: builders.build_manytomanyfield,
            models.OneToOneField: builders.build_onetoonefield,
            models.CharField: builders.build_charfield,
            models.EmailField: builders.build_emailfield,
            models.GenericIPAddressField: builders.build_genericipaddressfield,
            models.SlugField: builders.build_slugfield,
            models.TextField: builders.build_textfield,
            models.URLField: builders.build_urlfield,
            models.UUIDField: builders.build_uuidfield,
        }
