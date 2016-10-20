from six import python_2_unicode_compatible

from django.db import models

__all__ = ('SavedFormDataEntryReference',)


@python_2_unicode_compatible
class SavedFormDataEntryReference(models.Model):
    """SavedFormDataEntryReference model.

    References the
    `fobi.contrib.plugins.form_handlers.db_store.models.SavedFormDataEntry`.
    """

    form = models.ForeignKey(
        'fobi_contrib_plugins_form_handlers_db_store.SavedFormDataEntry'
    )

    def __str__(self):
        return self.form.name
