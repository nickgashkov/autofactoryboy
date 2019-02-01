from autofactory import DjangoModelAutoFactory
from tests.app.models import One


class OneFactory(DjangoModelAutoFactory):
    class Meta:
        model = One
        fields = "__all__"
