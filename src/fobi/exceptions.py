__title__ = 'fobi.exceptions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseException', 'ImproperlyConfigured', 'InvalidRegistryItemType', 
    'DoesNotExist', 'ThemeDoesNotExist', 'PluginDoesNotExist',
    'FormElementPluginDoesNotExist', 'FormHandlerPluginDoesNotExist',
    'NoDefaultThemeSet',
)

class BaseException(Exception):
    """
    Base exception.
    """


class ImproperlyConfigured(BaseException):
    """
    Exception raised when developer didn't configure/write the code properly.
    """


class InvalidRegistryItemType(ValueError, BaseException):
    """
    Raised when an attempt is made to register an item in the registry which
    does not have a proper type.
    """


class DoesNotExist(BaseException):
    """
    Raised when something does not exist.
    """


class ThemeDoesNotExist(DoesNotExist):
    """
    Raised when no theme with given uid can be found.
    """


class PluginDoesNotExist(DoesNotExist):
    """
    Raised when no plugin with given uid can be found.
    """


class FormElementPluginDoesNotExist(PluginDoesNotExist):
    """
    Raised when no form element plugin with given uid can be found.
    """


class FormHandlerPluginDoesNotExist(PluginDoesNotExist):
    """
    Raised when no form handler plugin with given uid can be found.
    """

class NoDefaultThemeSet(ImproperlyConfigured):
    """
    Raised when no active theme is chosen.
    """
