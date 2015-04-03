__all__ = ('SavedFormDataEntryReference',)

from django.db import models

from fobi.contrib.plugins.form_handlers.db_store.models import (
    SavedFormDataEntry
    )

class SavedFormDataEntryReference(models.Model):
    """
    Model which references the
    `fobi.contrib.plugins.form_handlers.db_store.models.SavedFormDataEntry`.
    """
    form = models.ForeignKey(SavedFormDataEntry)
