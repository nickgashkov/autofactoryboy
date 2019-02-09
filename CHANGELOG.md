# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
- **Breaking change.** Rename `DjangoModelAutoFactory.Meta.fields` into
`DjangoModelAutoFactory.Meta.autofields`.
- *Add* `DjangoModelAutoFactory.Meta.autoexclude`.
- *Change* generated with `autofactory` name from `GeneratedModelFactory` to 
`ModelFactory`.
- *Fix* callable as a `django.db.models.Field.default` not being called on 
instance generation.
- *Fix* `from_choices` filling a choice tuple into field instead of the database
value.

## [0.2.0] — 2019-02-08
- Add builders registry for Django ORM.

## 0.1.0 — 2019-02-03
- Add Django ORM support.

[Unreleased]: https://github.com/nickgashkov/autofactoryboy/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/nickgashkov/autofactoryboy/compare/v0.2.0...v0.1.0