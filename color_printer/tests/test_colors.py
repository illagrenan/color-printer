#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
import six

from color_printer.context_manager import captured_output
from ..colors import _print, black, red, green, yellow, blue, magenta, cyan, white


standard_library.install_aliases()

if six.PY2:
    from unittest2 import TestCase
else:
    from unittest import TestCase


class ColorsTestCase(TestCase):
    RESET_CODE = '\x1b[39m\x1b[49m\x1b[0m'
    TEST_STR = "abcABCabc"

    def test_ouput_is_reseted(self):
        with captured_output() as (out, err):
            _print(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_black(self):
        with captured_output() as (out, err):
            black(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[30m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_red(self):
        with captured_output() as (out, err):
            red(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[31m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_green(self):
        with captured_output() as (out, err):
            green(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[32m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_yellow(self):
        with captured_output() as (out, err):
            yellow(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[33m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_blue(self):
        with captured_output() as (out, err):
            blue(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[34m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)

    def test_magenta(self):
        with captured_output() as (out, err):
            magenta(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[35m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)


    def test_cyan(self):
        with captured_output() as (out, err):
            cyan(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[36m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)


    def test_white(self):
        with captured_output() as (out, err):
            white(ColorsTestCase.TEST_STR)

        output = out.getvalue().strip()
        self.assertEqual(output, '\x1b[1m\x1b[37m' + ColorsTestCase.TEST_STR + ColorsTestCase.RESET_CODE)