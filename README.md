# AutoFactoryBoy

*Warning!* Currently working only with 
[Django](https://github.com/django/django).

AutoFactoryBoy generates factories for you.

It introspects Django's models and generates a factory with all fields with 
`blank=False`.

## Quickstart

To use AutoFactoryBoy, simply declare an `AutoFactory` by subclassing a 
`autofactory.DjangoModelAutoFactory`.

```python
from autofactory import DjangoModelAutoFactory

from tests.app.models import One

class OneFactory(DjangoModelAutoFactory):
    class Meta:
        model = One
        fields = "__all__"

one = OneFactory.create()
```

## Testing

To perform a testing against a current environment, run:

```bash
$ make test
```

To test a package against a bunch of environments, use tox:

```bash
$ tox
```
