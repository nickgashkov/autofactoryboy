# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2019 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.app.settings')
django.setup()

from django import test
from django.test.runner import DiscoverRunner
from django.test import utils

from tests.app.factories import OneFactory


test_state = dict()


def setUpModule():
    utils.setup_test_environment()

    runner = DiscoverRunner()
    runner_state = runner.setup_databases()

    test_state['runner'] = runner
    test_state['runner_state'] = runner_state


def tearDownModule():
    runner = test_state['runner']
    runner_state = test_state['runner_state']

    runner.teardown_databases(runner_state)
    utils.teardown_test_environment()


class DjangoTestCase(test.TestCase):
    def test(self):
        concrete = OneFactory.create()
