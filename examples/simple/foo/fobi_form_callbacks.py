from __future__ import print_function

import logging

from fobi.base import (
    form_callback_registry,
    FormCallback,
    integration_form_callback_registry,
    IntegrationFormCallback,
)

from fobi.constants import (
    CALLBACK_BEFORE_FORM_VALIDATION,
    CALLBACK_FORM_INVALID,
    CALLBACK_FORM_VALID,
    CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
    CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
)

from fobi.contrib.apps.drf_integration import UID as INTEGRATE_WITH
# from fobi.contrib.plugins.form_handlers.db_store.callbacks import (
#     AutoFormDbStore
# )
# from fobi.contrib.plugins.form_handlers.mail.callbacks import (
#     AutoFormMail
# )

logger = logging.getLogger('fobi')

__all__ = (
    'SaveAsFooItem',
    'DummyInvalidCallback',
)

# *************************************************************
# *************************************************************
# ********************** Core callbacks ***********************
# *************************************************************
# *************************************************************

# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************


class SaveAsFooItem(FormCallback):
    """Save the form as a foo item, if certain conditions are met."""

    stage = CALLBACK_FORM_VALID

    def callback(self, form_entry, request, form):
        """Custom callback login comes here."""
        logger.debug("Great! Your form is valid!")


form_callback_registry.register(SaveAsFooItem)

# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************


class DummyInvalidCallback(FormCallback):
    """Saves the form as a foo item, if certain conditions are met."""

    stage = CALLBACK_FORM_INVALID

    def callback(self, form_entry, request, form):
        """Custom callback login comes here."""
        logger.debug("Damn! You've made a mistake, boy!")


form_callback_registry.register(DummyInvalidCallback)

# *************************************************************
# *************************************************************
# ****************** DRF integration callbacks ****************
# *************************************************************
# *************************************************************


# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************


class DRFSaveAsFooItem(IntegrationFormCallback):
    """Save the form as a foo item, if certain conditions are met."""

    stage = CALLBACK_FORM_VALID
    integrate_with = INTEGRATE_WITH

    def callback(self, form_entry, request, **kwargs):
        """Custom callback login comes here."""
        logger.debug("Great! Your form is valid!")


integration_form_callback_registry.register(DRFSaveAsFooItem)

# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************


class DRFDummyInvalidCallback(IntegrationFormCallback):
    """Saves the form as a foo item, if certain conditions are met."""

    stage = CALLBACK_FORM_INVALID
    integrate_with = INTEGRATE_WITH

    def callback(self, form_entry, request, **kwargs):
        """Custom callback login comes here."""
        logger.debug("Damn! You've made a mistake, boy!")


integration_form_callback_registry.register(DRFDummyInvalidCallback)

# *************************************************************
# **************** Auto Form DB store callback ****************
# *************************************************************

# form_callback_registry.register(AutoFormDbStore)

# *************************************************************
# ****************** Auto Form Mail callback ******************
# *************************************************************

# form_callback_registry.register(AutoFormMail)
