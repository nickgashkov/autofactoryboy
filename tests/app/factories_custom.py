from autofactory.django import DjangoModelAutoFactory
from autofactory.django.options import DjangoAutoOptions
from autofactory.django.registry import DjangoRegistry

from tests.app.models import CustomCharField, CustomBuilderField


def build_custom_char_field(field_cls):
    return "CUSTOM_FIELD"


class CustomDjangoRegistry(DjangoRegistry):
    @property
    def builder_mapping(self):
        mapping = super(CustomDjangoRegistry, self).builder_mapping
        mapping[CustomCharField] = build_custom_char_field

        return mapping


class CustomDjangoAutoOptions(DjangoAutoOptions):
    _registry_class = CustomDjangoRegistry


class CustomDjangoModelAutoFactory(DjangoModelAutoFactory):
    _options_class = CustomDjangoAutoOptions

    class Meta:
        abstract = True


class CustomBuilderFieldFactory(CustomDjangoModelAutoFactory):
    class Meta:
        model = CustomBuilderField
        fields = "__all__"
