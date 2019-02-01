# AutoFactoryBoy

AutoFactoryBoy generates factories for you.

## Usage

```python
from autofactory.factories.django_ import DjangoModelAutoFactory
from project.fruits.models import Fruit

class FruitAutoFactory(DjangoModelAutoFactory):
    class Meta:
        model = Friut
        fields = "__all__"
```
