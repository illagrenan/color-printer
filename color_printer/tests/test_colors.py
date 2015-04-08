#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
import six

from .context_manager import captured_output


# noinspection PyProtectedMember
from ..colors import _print


standard_library.install_aliases()

if six.PY2:
    from unittest2 import TestCase
else:
    from unittest import TestCase


class AddressTestCase(TestCase):
    def test_ouput_si_reseted(self):
        with captured_output() as (out, err):
            _print("abc")

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1mabc\x1b[39m\x1b[49m\x1b[0m')
