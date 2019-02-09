# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import datetime
import os
import shutil

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.app.settings")
django.setup()

from django import test
from django.conf import settings
from django.test.runner import DiscoverRunner
from django.test import utils

from autofactory.django import autofactory, DjangoModelAutoFactory, builders
from autofactory.django.builders import registry, FROM_DEFAULT

from tests.app.factories_custom import CustomBuilderFieldFactory
from tests.app.factories import (
    EveryFieldTypeFactory,
    WithDeclaredFieldFactory,
    WithBlankFieldAndAllFieldsFactory,
    WithBlankFieldAndNotAllFieldsFactory,
    WithCustomThroughFactory,
    WithDefaultAllFieldsFactory,
    WithDefaultTupleFieldsFactory,
    WithChoiceFieldFactory,
    WithExcludeFactory, WithoutExcludeFactory, WithBlankFieldAndExcludeFactory)
from tests.app.models import (
    CustomThrough,
    EveryFieldType,
    WithChoiceField,
    WithDefault,
    WithDefaultCallable)

test_state = dict()


def setUpModule():
    utils.setup_test_environment()

    runner = DiscoverRunner()
    runner_state = runner.setup_databases()

    test_state["runner"] = runner
    test_state["runner_state"] = runner_state

    if os.path.exists(settings.MEDIA_ROOT):
        return

    os.makedirs(settings.MEDIA_ROOT)


def tearDownModule():
    runner = test_state["runner"]
    runner_state = test_state["runner_state"]

    runner.teardown_databases(runner_state)
    utils.teardown_test_environment()

    shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)


class DjangoTestCase(test.TestCase):
    def test_autofactory_can_create_and_build(self):
        EveryFieldTypeFactory.create()
        EveryFieldTypeFactory.build()
        EveryFieldTypeFactory.create_batch(2)
        EveryFieldTypeFactory.build_batch(2)

    def test_regular_autofactory_builds_every_field(self):
        every_field_not_blank = EveryFieldTypeFactory.create()

        self.assertIsNotNone(every_field_not_blank.bigintegerfield)
        self.assertIsNotNone(every_field_not_blank.binaryfield)
        self.assertIsNotNone(every_field_not_blank.booleanfield)
        self.assertIsNotNone(every_field_not_blank.charfield)
        self.assertIsNotNone(every_field_not_blank.datefield)
        self.assertIsNotNone(every_field_not_blank.datetimefield)
        self.assertIsNotNone(every_field_not_blank.decimalfield)
        self.assertIsNotNone(every_field_not_blank.durationfield)
        self.assertIsNotNone(every_field_not_blank.emailfield)
        self.assertIsNotNone(every_field_not_blank.filefield)
        self.assertIsNotNone(every_field_not_blank.filepathfield)
        self.assertIsNotNone(every_field_not_blank.floatfield)
        self.assertIsNotNone(every_field_not_blank.imagefield)
        self.assertIsNotNone(every_field_not_blank.integerfield)
        self.assertIsNotNone(every_field_not_blank.genericipaddressfield)
        self.assertIsNotNone(every_field_not_blank.nullbooleanfield)
        self.assertIsNotNone(every_field_not_blank.positiveintegerfield)
        self.assertIsNotNone(every_field_not_blank.positivesmallintegerfield)
        self.assertIsNotNone(every_field_not_blank.slugfield)
        self.assertIsNotNone(every_field_not_blank.smallintegerfield)
        self.assertIsNotNone(every_field_not_blank.textfield)
        self.assertIsNotNone(every_field_not_blank.timefield)
        self.assertIsNotNone(every_field_not_blank.urlfield)
        self.assertIsNotNone(every_field_not_blank.uuidfield)
        self.assertIsNotNone(every_field_not_blank.foreignkey)
        self.assertIsNotNone(every_field_not_blank.onetoone)

        self.assertTrue(every_field_not_blank.manytomany.exists())

    def test_shortcut_autofactory_builds_every_field_except_blank_one(self):
        every_field_not_blank_factory = autofactory(EveryFieldType)
        every_field_not_blank = every_field_not_blank_factory.create()

        self.assertIsNotNone(every_field_not_blank.bigintegerfield)
        self.assertIsNotNone(every_field_not_blank.binaryfield)
        self.assertIsNotNone(every_field_not_blank.booleanfield)
        self.assertIsNotNone(every_field_not_blank.charfield)
        self.assertIsNotNone(every_field_not_blank.datefield)
        self.assertIsNotNone(every_field_not_blank.datetimefield)
        self.assertIsNotNone(every_field_not_blank.decimalfield)
        self.assertIsNotNone(every_field_not_blank.durationfield)
        self.assertIsNotNone(every_field_not_blank.emailfield)
        self.assertIsNotNone(every_field_not_blank.filefield)
        self.assertIsNotNone(every_field_not_blank.filepathfield)
        self.assertIsNotNone(every_field_not_blank.floatfield)
        self.assertIsNotNone(every_field_not_blank.imagefield)
        self.assertIsNotNone(every_field_not_blank.integerfield)
        self.assertIsNotNone(every_field_not_blank.genericipaddressfield)
        self.assertIsNotNone(every_field_not_blank.nullbooleanfield)
        self.assertIsNotNone(every_field_not_blank.positiveintegerfield)
        self.assertIsNotNone(every_field_not_blank.positivesmallintegerfield)
        self.assertIsNotNone(every_field_not_blank.slugfield)
        self.assertIsNotNone(every_field_not_blank.smallintegerfield)
        self.assertIsNotNone(every_field_not_blank.textfield)
        self.assertIsNotNone(every_field_not_blank.timefield)
        self.assertIsNotNone(every_field_not_blank.urlfield)
        self.assertIsNotNone(every_field_not_blank.uuidfield)
        self.assertIsNotNone(every_field_not_blank.foreignkey)
        self.assertIsNotNone(every_field_not_blank.onetoone)

        self.assertTrue(every_field_not_blank.manytomany.exists())

    def test_autofactory_does_not_override_declared_field(self):
        with_declared_field = WithDeclaredFieldFactory.create()

        self.assertIsNotNone(with_declared_field.autodeclared_integer)
        self.assertEqual(with_declared_field.declared_integer, -42)

    def test_autofactory_does_not_fill_blank_field_if_fields_is___all__(self):
        with_blank_field = WithBlankFieldAndAllFieldsFactory.create()

        self.assertIsNone(with_blank_field.can_be_blank)
        self.assertIsNotNone(with_blank_field.cannot_be_blank)

    def test_autofactory_does_fill_blank_field_if_it_is_specified_in_fields(self):
        with_blank_field = WithBlankFieldAndNotAllFieldsFactory.create()

        self.assertIsNotNone(with_blank_field.can_be_blank)
        self.assertIsNotNone(with_blank_field.cannot_be_blank)

    def test_autofactory_does_creates_m2m_with_a_custom_through(self):
        with_custom_through = WithCustomThroughFactory.create()

        self.assertTrue(with_custom_through.custom_through_m2m.exists())

        through_qs = CustomThrough.objects.filter(with_custom_through=with_custom_through)
        through_list = [t.non_blank_field for t in through_qs.all()]

        self.assertNotIn(None, through_list)
        self.assertNotIn("", through_list)

    def test_autofactory_takes_default_for_a_field_instead_of_a_random_value(self):
        with_default_all_fields = WithDefaultAllFieldsFactory.create()
        with_default_tuple_fields = WithDefaultTupleFieldsFactory.create()

        self.assertIsNotNone(with_default_all_fields.string)
        self.assertIsNotNone(with_default_tuple_fields.string)

        self.assertEqual(with_default_all_fields.string_with_default, "DEFAULT")
        self.assertEqual(with_default_tuple_fields.string_with_default, "DEFAULT")

    def test_autofactory_takes_a_random_choice_if_field_has_it(self):
        with_choice_field = WithChoiceFieldFactory.create()

        self.assertIn("VALUE", with_choice_field.string_with_choices)
        self.assertNotIn("HUMAN_NAME", with_choice_field.string_with_choices)
        self.assertIn(
            with_choice_field.string_with_choices,
            [c[0] for c in WithChoiceField.CHOICES],
        )

    def test_autofactory_builds_custom_field_if_provided_in_registry(self):
        custom_builder_field = CustomBuilderFieldFactory.create()

        self.assertEqual(custom_builder_field.custom, "CUSTOM_FIELD")

    def test_patching_registry_changes_builders(self):
        def setUp():
            # Has to be this way to encapsulate test.
            registry.register(FROM_DEFAULT, lambda x: "PATCHED DEFAULT")

        def tearDown():
            registry.register(FROM_DEFAULT, builders.from_default)

        setUp()

        class PatchedDefaultFactory(DjangoModelAutoFactory):
            class Meta:
                model = WithDefault
                autofields = "__all__"

        with_default = PatchedDefaultFactory.create()
        self.assertEqual(with_default.string_with_default, "PATCHED DEFAULT")

        tearDown()

    def test_autofactory_from_shortcut_has_classname_like_ModelFactory(self):
        with_default_factory = autofactory(WithDefault)

        self.assertEqual(with_default_factory.__name__, "WithDefaultFactory")

    def test_autofactory_calls_a_default_if_it_is_callable(self):
        with_default_callable_factory = autofactory(WithDefaultCallable)
        with_default_callable = with_default_callable_factory.create()

        self.assertEqual(
            with_default_callable.datetime_with_default_callable,
            datetime.datetime.fromtimestamp(0),
        )

    def test_autofactory_restricts_to_set_autofields_and_autoexclude_at_the_same_time(self):
        with self.assertRaises(AssertionError) as cm:
            class AutofieldsAutoexcludeFactory(DjangoModelAutoFactory):
                class Meta:
                    model = WithDefault
                    autofields = ("string",)
                    autoexclude = ("string_with_default",)

        self.assertEqual(
            cm.exception.args[0],
            "Cannot set 'autofields' and 'autoexclude' at the same time",
        )

    def test_autofactory_does_not_autodeclare_fields_from_exclude(self):
        with_exclude = WithExcludeFactory.create()
        without_exclude = WithoutExcludeFactory.create()

        self.assertIsNone(with_exclude.excluded_field)
        self.assertIsNotNone(with_exclude.field)

        self.assertIsNotNone(without_exclude.excluded_field)
        self.assertIsNotNone(without_exclude.field)

    def test_autofactory_does_not_declare_blank_fields_if_autoexclude_is_used(self):
        with_blank_field_and_exclude = WithBlankFieldAndExcludeFactory.create()

        self.assertIsNone(with_blank_field_and_exclude.can_be_blank)
        self.assertIsNone(with_blank_field_and_exclude.cannot_be_blank)
