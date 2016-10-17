__title__ = 'fobi.exceptions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseException',
    'ImproperlyConfigured',
    'InvalidRegistryItemType',
    'DoesNotExist',
    'ThemeDoesNotExist',
    'PluginDoesNotExist',
    'FormElementPluginDoesNotExist',
    'FormHandlerPluginDoesNotExist',
    'FormWizardHandlerPluginDoesNotExist',
    'NoDefaultThemeSet',
    'FormPluginError',
    'FormElementPluginError',
    'FormHandlerPluginError',
    'FormCallbackError',
)


class BaseException(Exception):
    """Base exception."""


class ImproperlyConfigured(BaseException):
    """Improperly configured.

    Exception raised when developer didn't configure/write the code properly.
    """


class InvalidRegistryItemType(ValueError, BaseException):
    """Invalid registry item type.

    Raised when an attempt is made to register an item in the registry which
    does not have a proper type.
    """


class DoesNotExist(BaseException):
    """Raised when something does not exist."""


class ThemeDoesNotExist(DoesNotExist):
    """Raised when no theme with given uid can be found."""


class PluginDoesNotExist(DoesNotExist):
    """Raised when no plugin with given uid can be found."""


class FormElementPluginDoesNotExist(PluginDoesNotExist):
    """Raised when no form element plugin with given uid can be found."""


class FormHandlerPluginDoesNotExist(PluginDoesNotExist):
    """Raised when no form handler plugin with given uid can be found."""


class FormWizardHandlerPluginDoesNotExist(PluginDoesNotExist):
    """FormWizardHandlerPlugin does not exist.

    Raised when no form wizard handler plugin with given uid can be found.
    """


class NoDefaultThemeSet(ImproperlyConfigured):
    """Raised when no active theme is chosen."""


class FormPluginError(BaseException):
    """Base error for form elements and handlers."""


class FormElementPluginError(FormPluginError):
    """Raised when form element plugin error occurs."""


class FormHandlerPluginError(FormPluginError):
    """Raised when form handler plugin error occurs."""


class FormCallbackError(FormPluginError):
    """Raised when form callback error occurs."""
