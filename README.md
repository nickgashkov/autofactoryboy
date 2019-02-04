# AutoFactoryBoy

[![Build Status](https://travis-ci.org/nickgashkov/autofactoryboy.svg?branch=master)](https://travis-ci.org/nickgashkov/autofactoryboy)
[![PyPI Package](https://img.shields.io/pypi/v/autofactory.svg)](https://pypi.org/project/autofactory/)

> **Warning!** Current version of *AutoFactoryBoy* supports only 
[Django](https://github.com/django/django) backend.

*AutoFactoryBoy* introspects Django's models and generates a factory with all 
not blank fields.

## Installation

Install from PyPI:

```bash
$ pip install autofactory
```

Build from source:

```bash
$ git clone git://github.com/nickgashkov/autofactoryboy/
$ python setup.py install
```

## Quickstart

There are a couple of options to create an `AutoFactory` for a model:

1. Subclass a `DjangoModelAutoFactory`:

    ```python
    from autofactory.django import DjangoModelAutoFactory
    
    from models import Model
    
    class ModelFactory(DjangoModelAutoFactory):
        class Meta:
            model = Model
            fields = "__all__"
    
    model = ModelFactory.create()
    ```

2. Make a factory right from the model with the help of a
shortcut:

    ```python
    from autofactory.django import autofactory
    
    from models import Model
    
    model_factory = autofactory(Model)
    model = model_factory.create()
    ```

## Q & A

### How do I specify fields to generate automatically?

*AutoFactoryBoy* will generate a `ModelFactory` for a model with fields, 
specified in the `ModelFactory.Meta`:

```python
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        fields = ("integer", "string")
```

The code snippet above is identical to:

```python
class ModelFactory(DjangoModelFactory):
    integer = factory.Faker("pyint")
    string = factory.Faker("text")

    class Meta:
        model = Model
```

### How do I make an autofactory with all model fields?

You can set `fields` to a special value (i.e. `__all__`) and all fields with 
`blank=False` will be generated automatically:

```python
# models.py
class Model(models.Model):
    integer = models.IntegerField(blank=True, null=True)
    string = models.CharField()

# factories.py
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        fields = "__all__"
```

The code snippet above is identical to:

```python
class ModelFactory(DjangoModelFactory):
    string = factory.Faker("text")

    class Meta:
        model = Model
```

## Testing

To test, run:

```bash
$ make test      # Current environment
$ make test-tox  # All tox environments
```
