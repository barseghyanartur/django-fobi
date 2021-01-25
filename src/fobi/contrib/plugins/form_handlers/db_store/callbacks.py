import datetime

import json

from django.core.serializers.json import DjangoJSONEncoder

from fobi.base import (
    FormCallback,
    get_processed_form_data,
)
from fobi.constants import CALLBACK_FORM_VALID
from .models import SavedFormDataEntry

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.callbacks'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AutoFormDbStore',
)


class AutoFormDbStore(FormCallback):
    """Auto save form entries.

    Note, that this callback is not active. In order to activate it, you
    should import the ``AutoFormDbStore`` and register it using the
    callback register as follows.

    >>> from fobi.base import form_callback_registry
    >>> from fobi.contrib.plugins.form_handlers.db_store.callbacks import (
    >>>     AutoFormDbStore
    >>> )
    >>> form_callback_registry.register(AutoFormDbStore)
    """

    stage = CALLBACK_FORM_VALID

    def callback(self, form_entry, request, form):
        """Callback.

        :param form_entry:
        :param request:
        :param form:
        :return:
        """
        form_element_entries = form_entry.formelemententry_set.all()

        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_form_data(
            form,
            form_element_entries
        )

        for key, value in cleaned_data.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                cleaned_data[key] = value.isoformat() \
                    if hasattr(value, 'isoformat') \
                    else value

        saved_form_data_entry = SavedFormDataEntry(
            form_entry=form_entry,
            user=request.user if request.user and request.user.pk else None,
            form_data_headers=json.dumps(
                field_name_to_label_map,
                cls=DjangoJSONEncoder
            ),
            saved_data=json.dumps(cleaned_data, cls=DjangoJSONEncoder)
        )
        saved_form_data_entry.save()
