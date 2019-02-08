from autofactory.django import DjangoModelAutoFactory
from autofactory.django.registry import registry

from tests.app.models import CustomCharField, CustomBuilderField


@registry.register(CustomCharField)
def build_custom_char_field(field_cls):
    return "CUSTOM_FIELD"


class CustomBuilderFieldFactory(DjangoModelAutoFactory):
    class Meta:
        model = CustomBuilderField
        fields = "__all__"
