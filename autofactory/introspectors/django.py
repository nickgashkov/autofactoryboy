# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals


class DjangoIntrospector(object):
    def __init__(self, model):
        self.model = model

    def declare(self):
        return None
