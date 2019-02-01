# AutoFactoryBoy

AutoFactoryBoy generates factories for you.

## Usage

```python
from autofactory import DjangoModelAutoFactory

from tests.app.models import Concrete

class ConcreteFactory(DjangoModelAutoFactory):
    class Meta:
        model = Concrete
        fields = "__all__"

concrete = ConcreteFactory.create()
```

## Testing

To perform a testing against a current environment, run:

```bash
$ make test
```
