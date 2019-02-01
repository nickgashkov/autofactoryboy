from autofactory import DjangoModelAutoFactory
from tests.app.models import Concrete


class ConcreteFactory(DjangoModelAutoFactory):
    class Meta:
        model = Concrete
        fields = "__all__"
