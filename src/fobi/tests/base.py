from __future__ import print_function

from django.conf import settings

__title__ = 'fobi.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'PRINT_INFO',
    'print_info',
    'fobi_setup',
    'skip',
    'is_fobi_setup_completed',
    'mark_fobi_setup_as_completed',
)

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************

PRINT_INFO = True


def print_info(func):
    """Prints some useful info."""
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        result = func(self, *args, **kwargs)

        print('\n{0}'.format(func.__name__))
        print('============================')
        if func.__doc__:
            print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n')

        return result
    return inner


SKIP = False


def skip(func):
    """Simply skips the test."""
    def inner(self, *args, **kwargs):
        """Inner."""
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner


class FobiSetup(object):
    """Setup fobi.

    Basic setup class in order to avoid the fobi test data
    to be initialised multiple times.
    """

    def __init__(self):
        self.is_done = False


fobi_setup = FobiSetup()


def is_fobi_setup_completed():
    """Is fobi setup completed?"""
    return fobi_setup.is_done is True


def mark_fobi_setup_as_completed():
    """Mark fobi setup as completed."""
    fobi_setup.is_done = True
