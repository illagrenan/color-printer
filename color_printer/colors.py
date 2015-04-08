# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os

from colorama import init, Fore, Back, Style


def run_from_ipython():
    try:
        # noinspection PyUnresolvedReferences
        __IPYTHON__
        return True
    except NameError:
        return False


if not run_from_ipython() and os.name == 'nt':
    # See this issue: https://code.google.com/p/colorama/issues/detail?id=58
    init()


def _print(txt):
    """
    Print text with ANSII colors and reset all styles.

    :argument txt: Any text
    :type txt: str or unicode_literals
    """

    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL
    print('{0}{1}'.format(Style.BRIGHT + txt, Fore.RESET + Back.RESET + Style.RESET_ALL))


def black(message):
    _print(Fore.BLACK + message)


def red(message):
    _print(Fore.RED + message)


def green(message):
    _print(Fore.GREEN + message)


def yellow(message):
    _print(Fore.YELLOW + message)


def blue(message):
    _print(Fore.BLUE + message)


def magenta(message):
    _print(Fore.MAGENTA + message)


def cyan(message):
    _print(Fore.CYAN + message)


def white(message):
    _print(Fore.WHITE + message)