Color printer
=============

|Travis CI Badge|   |Coverage Status|   |Requirements Status|

Installation
------------

**This package is not yet on PyPI.**

.. code:: bash

    pip install --upgrade git+git://github.com/illagrenan/color-printer.git#egg=color_printer

Usage
-----

.. code:: bash

    from color_printer import colors

    colors.black("Foo bar")
    colors.red("Foo bar")
    colors.green("Foo bar")
    colors.yellow("Foo bar")
    colors.blue("Foo bar")
    colors.magenta("Foo bar")
    colors.cyan("Foo bar")
    colors.white("Foo bar")

.. |Travis CI Badge| image:: https://api.travis-ci.org/illagrenan/color_printer.png
   :target: https://travis-ci.org/illagrenan/color_printer
.. |Coverage Status| image:: https://coveralls.io/repos/illagrenan/color_printer/badge.png
   :target: https://coveralls.io/r/illagrenan/color_printer
.. |Requirements Status| image:: https://requires.io/github/illagrenan/color_printer/requirements.svg?branch=master
   :target: https://requires.io/github/illagrenan/color_printer/requirements/?branch=master
