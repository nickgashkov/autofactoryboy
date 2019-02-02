from autofactory import DjangoModelAutoFactory
from tests.app.models import EveryFieldType, WithDeclaredField, WithBlankField


class EveryFieldTypeFactory(DjangoModelAutoFactory):
    class Meta:
        model = EveryFieldType
        fields = (
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
        fields = "__all__"


class WithDeclaredFieldFactory(DjangoModelAutoFactory):
    declared_integer = -42

    class Meta:
        model = WithDeclaredField
        fields = "__all__"


class WithBlankFieldAndAllFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithBlankField
        fields = "__all__"


class WithBlankFieldAndNotAllFieldsFactory(DjangoModelAutoFactory):
    class Meta:
        model = WithBlankField
        fields = ("can_be_blank", "cannot_be_blank")
