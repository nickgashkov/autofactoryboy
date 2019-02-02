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

from tests.app.factories import EveryFieldNotBlankFactory


test_state = dict()


def setUpModule():
    utils.setup_test_environment()

    runner = DiscoverRunner()
    runner_state = runner.setup_databases()

    test_state["runner"] = runner
    test_state["runner_state"] = runner_state

    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)


def tearDownModule():
    runner = test_state["runner"]
    runner_state = test_state["runner_state"]

    runner.teardown_databases(runner_state)
    utils.teardown_test_environment()

    shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)


class EveryFieldNotBlankTestCase(test.TestCase):
    def test_builders_build(self):
        every_field_not_blank = EveryFieldNotBlankFactory.create()

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
        self.assertTrue(every_field_not_blank.manytomany.exists())
        self.assertIsNotNone(every_field_not_blank.onetoone)
