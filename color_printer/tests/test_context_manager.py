#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
import six

from color_printer.context_manager import captured_output


standard_library.install_aliases()

if six.PY2:
    from unittest2 import TestCase
else:
    from unittest import TestCase


class ContextManagerTestCase(TestCase):
    def test_output_is_captured(self):
        test_string = "Some test string..."

        print("Some... random...")

        with captured_output() as (out, err):
            print(test_string)

        print("string outside manager...")

        output = out.getvalue().strip()
        self.assertEqual(output, test_string)
