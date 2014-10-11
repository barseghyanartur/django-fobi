from __future__ import print_function

import logging

logger = logging.getLogger('fobi')

from fobi.constants import (
    CALLBACK_BEFORE_FORM_VALIDATION, CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
    CALLBACK_FORM_VALID, CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS, CALLBACK_FORM_INVALID
    )
from fobi.base import FormCallback, form_callback_registry

# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************

class SaveAsFooItem(FormCallback):
    """
    Saves the form as a foo item, if certain conditions are met.
    """
    stage = CALLBACK_FORM_VALID

    def callback(self, form_entry, request, form):
        """
        Custom callback login comes here.
        """
        logger.debug("Great! Your form is valid!")


form_callback_registry.register(SaveAsFooItem)

# *************************************************************
# **************** Save as foo callback ***********************
# *************************************************************

class DummyInvalidCallback(FormCallback):
    """
    Saves the form as a foo item, if certain conditions are met.
    """
    stage = CALLBACK_FORM_INVALID

    def callback(self, form_entry, request, form):
        """
        Custom callback login comes here.
        """
        logger.debug("Damn! You've made a mistake, boy!")


form_callback_registry.register(DummyInvalidCallback)
