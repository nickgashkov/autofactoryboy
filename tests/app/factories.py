from autofactory import DjangoModelAutoFactory
from tests.app.models import EveryFieldNotBlank


class EveryFieldNotBlankFactory(DjangoModelAutoFactory):
    class Meta:
        model = EveryFieldNotBlank
        fields = "__all__"
