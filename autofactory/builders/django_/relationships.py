# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Nick Gashkov
#
# Distributed under MIT License. See LICENSE file for details.
from __future__ import unicode_literals


def build_foreignkey(field_cls):
    raise NotImplementedError('Relational fields are not supported yet.')


def build_manytomanyfield(field_cls):
    raise NotImplementedError('Relational fields are not supported yet.')


def build_onetoonefield(field_cls):
    raise NotImplementedError('Relational fields are not supported yet.')
