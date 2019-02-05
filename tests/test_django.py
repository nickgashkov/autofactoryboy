# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import os
import shutil

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.app.settings")
django.setup()

from django import test
from django.conf import settings
from django.test.runner import DiscoverRunner
from django.test import utils

from autofactory.django import autofactory

from tests.app.factories_custom import CustomBuilderFieldFactory
from tests.app.factories import (
    EveryFieldTypeFactory,
    WithDeclaredFieldFactory,
    WithBlankFieldAndAllFieldsFactory,
    WithBlankFieldAndNotAllFieldsFactory,
    WithCustomThroughFactory,
    WithDefaultAllFieldsFactory,
    WithDefaultTupleFieldsFactory,
)
from tests.app.models import EveryFieldType, CustomThrough

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

    def test_autofactory_does_not_create_declaration_for_field_with_a_default_all_fields(self):
        with_default_all_fields = WithDefaultAllFieldsFactory.create()

        self.assertIsNotNone(with_default_all_fields.string)
        self.assertEqual(with_default_all_fields.string_with_default, "DEFAULT")

    def test_autofactory_does_not_create_declaration_for_field_with_a_default_tuple_fields(self):
        with_default_tuple_fields = WithDefaultTupleFieldsFactory.create()

        self.assertIsNotNone(with_default_tuple_fields.string)
        self.assertEqual(with_default_tuple_fields.string_with_default, "DEFAULT")

    def test_autofactory_builds_custom_field_if_provided_in_registry(self):
        custom_builder_field = CustomBuilderFieldFactory.create()

        self.assertEqual(custom_builder_field.custom, "CUSTOM_FIELD")
