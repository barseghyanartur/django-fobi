from __future__ import unicode_literals

import bleach
import json
from six import python_2_unicode_compatible, string_types

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .....helpers import two_dicts_to_string

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AbstractSavedFormDataEntry',
    'SavedFormDataEntry',
    'SavedFormWizardDataEntry',
)

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************


class AbstractSavedFormDataEntry(models.Model):
    """Abstract saved form data entry."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    form_data_headers = models.TextField(
        _("Form data headers"),
        null=True,
        blank=True
    )
    saved_data = models.TextField(_("Plugin data"), null=True, blank=True)
    created = models.DateTimeField(_("Date created"), auto_now_add=True)

    class Meta(object):
        """Meta options."""

        abstract = True

    def formatted_saved_data(self):
        """Shows the formatted saved data records.

        :return string:
        """
        try:
            headers = json.loads(self.form_data_headers)
            data = json.loads(self.saved_data)
            for key, value in data.items():

                if isinstance(value, string_types):
                    value = bleach.clean(value, strip=True)
                    if (value.startswith(settings.MEDIA_URL) or
                            value.startswith('http://') or
                            value.startswith('https://')):
                        value = '<a href="{value}">{value}</a>'.format(
                            value=value
                        )
                    data[key] = value

            return two_dicts_to_string(headers, data)
        except (ValueError, json.decoder.JSONDecodeError) as err:
            return ''

    formatted_saved_data.allow_tags = True
    formatted_saved_data.short_description = _("Saved data")


@python_2_unicode_compatible
class SavedFormDataEntry(AbstractSavedFormDataEntry):
    """Saved form data."""

    form_entry = models.ForeignKey(
        'fobi.FormEntry',
        verbose_name=_("Form"),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta(object):
        """Meta options."""

        abstract = False
        verbose_name = _("Saved form data entry")
        verbose_name_plural = _("Saved form data entries")
        db_table = 'db_store_savedformdataentry'

    def __str__(self):
        return "Saved form data entry from {0}".format(self.created)


@python_2_unicode_compatible
class SavedFormWizardDataEntry(AbstractSavedFormDataEntry):
    """Saved form data."""

    form_wizard_entry = models.ForeignKey(
        'fobi.FormWizardEntry',
        verbose_name=_("Form"),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta(object):
        """Meta options."""

        abstract = False
        verbose_name = _("Saved form wizard data entry")
        verbose_name_plural = _("Saved form wizard data entries")
        db_table = 'db_store_savedformwizarddataentry'

    def __str__(self):
        return "Saved form wizard data entry from {0}".format(self.created)
