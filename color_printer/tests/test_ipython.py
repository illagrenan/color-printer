#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
import six

from ..colors import run_from_ipython


standard_library.install_aliases()

if six.PY2:
    from unittest2 import TestCase
else:
    from unittest import TestCase


class IPythonTestCase(TestCase):
    def test_run_from_ipython_is_false_in_normal_console(self):
        self.assertFalse(run_from_ipython())