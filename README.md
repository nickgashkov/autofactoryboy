# AutoFactoryBoy

[![Build Status](https://travis-ci.org/nickgashkov/autofactoryboy.svg?branch=master)](https://travis-ci.org/nickgashkov/autofactoryboy)
[![PyPI Package](https://img.shields.io/pypi/v/autofactory.svg)](https://pypi.org/project/autofactory/)

> **Warning!** *AutoFactoryBoy* supports only 
[Django](https://github.com/django/django) ORM for now.

*AutoFactoryBoy* introspects ORM models and generates factories.

## Contents
* [Installation](#installation)
* [Quickstart](#quickstart)
* [Compatibility](#compatibility)
* [Q & A](#q--a)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)

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
            autofields = "__all__"
    
    model = ModelFactory.create(some__field__to__change=42)
    ```

2. Make a factory right from the model with the help of a
shortcut:

    ```python
    from autofactory.django import autofactory
    
    from models import Model
    
    model_factory = autofactory(Model)
    model = model_factory.create(some__field__to__change=42)
    ```

## Compatibility

| Python | Django         | SQLAlchemy | Mogo | mongoengine |
| ------ | -------------- | ---------- | ---- | ----------- |
| 2.7    | 1.11           | —          | —    | —           |
| 3.4    | 1.11, 2.0      | —          | —    | —           |
| 3.5    | 1.11, 2.0, 2.1 | —          | —    | —           |
| 3.6    | 1.11, 2.0, 2.1 | —          | —    | —           |
| 3.7    | 1.11, 2.0, 2.1 | —          | —    | —           |

## Q & A

### How do I make an autofactory with specific fields?

*AutoFactoryBoy* will generate a `ModelFactory` for a model with fields, 
declared in the `ModelFactory.Meta`:

```python
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        autofields = ("integer", "string")
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
`blank=False` and without `default` will be generated automatically:

```python
# models.py
class Model(models.Model):
    integer = models.IntegerField(blank=True, null=True)
    text = models.TextField(default="Default")
    string = models.CharField(max_length=20)

# factories.py
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        autofields = "__all__"
```

The code snippet above is identical to:

```python
class ModelFactory(DjangoModelFactory):
    string = factory.Faker("text", max_nb_chars=20)

    class Meta:
        model = Model
```

### How do I make an autofactory with all model fields except one

You can add the field you want to exclude to the `Meta.autoexclude` tuple:

```python
# models.py
class Model(models.Model):
    field = models.IntegerField(blank=False, null=True)
    field_to_exclude = models.IntegerField(blank=False, null=True)

# factories.py
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        autoexclude = ("field_to_exclude",)
```

The code snippet above is identical to:

```python
class ModelFactory(DjangoModelFactory):
    field = factory.Faker("pyint")

    class Meta:
        model = Model
```

> **Warning!** One cannot set `autofields` and `autoexclude` for one factory at
the same time.

### How do I teach AutoFactoryBoy how to generate my custom field 

Make a custom builder and register it with decorator or as a function:

```python
# models.py
class Model:
    custom = CustomField()

# builders.py
from autofactory.django.builders import registry

@registry.register(CustomField)
def build_custom_field(field_cls):
    ...

registry.register(CustomField, build_custom_field)
```

**Warning!** Order is important. Make sure, that you register all 
custom fields *before* any factory declaration. I.e.:

```python
from autofactory.django.builders import registry, FROM_DEFAULT
from autofactory.django import autofactory, DjangoModelAutoFactory

from models import Model


# Register first.
registry.register(FROM_DEFAULT, lambda x: "Default for everything")


# Declare second.
class ModelFactory(DjangoModelAutoFactory):
    class Meta:
        model = Model
        autofields = "__all__"

model_factory = autofactory(Model)
``` 

### How do I override AutoFactoryBoy field builder 

`autofactory.django.builders.registry` for the rescue! Using the 
approach above, you can redeclare builder for any field:

```python
from autofactory.django.builders import registry

from django.db import models


@registry.register(models.CharField)
def custom_char_field_builder(field_cls):
    ...
```

## Contributing

### Dependencies

To install dev dependencies, run:

```bash
$ pip install pip-tools
$ make upgrade
```

### Code formatting

To format the code, run:

```bash
$ make 
```

### Testing

To test, run:

```bash
$ make test      # Current environment
$ make test-tox  # All tox environments
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) 
file for details.

## Acknowledgments

* [factory_boy](https://github.com/FactoryBoy/factory_boy)
