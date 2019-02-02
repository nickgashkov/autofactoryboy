# AutoFactoryBoy

[![Build Status](https://travis-ci.org/nickgashkov/autofactoryboy.svg?branch=master)](https://travis-ci.org/nickgashkov/autofactoryboy)

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

from models import Model

class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        fields = "__all__"

model = ModelFactory.create()
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
