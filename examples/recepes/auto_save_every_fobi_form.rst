Question
--------
How to set a ``db_store`` form-handler as default form handler in django-fobi
(in order to save all forms by default)?

Answer
------
There's no out-of-box solution for that.

However, you could do as follows:

Solution 1
~~~~~~~~~~
Using django signals, watch updates of the FormEntry model and add the
``db_handler`` plugin programmatically each time a form is saved (if it
doesn't yet have it assigned).

.. code-block:: python

    from django.core.exceptions import ObjectDoesNotExist
    from django.db.models.signals import post_save, post_delete
    from django.dispatch import receiver

    @receiver(post_save)
    def update_document(sender, **kwargs):
        app_label = sender._meta.app_label
        model_name = sender._meta.model_name.lower()
        instance = kwargs['instance']

        if app_label == 'fobi' and model_name == 'formentry':
            from fobi.models import FormHandlerEntry
            FormHandlerEntry.objects.get_or_create(
                plugin_uid='db_store',
                form_entry=instance     
            )

Solution 2
~~~~~~~~~~
You could also register a form callback (fobi has callbacks implemented for
almost each stage of form submission process).

In your callback you would have to mimic the functionality of the ``db_store``
plugin (copy-paste mainly).

.. code-block:: python

    import datetime

    import simplejson as json

    from fobi.base import (
        form_callback_registry,
        FormCallback,
        get_processed_form_data,
    )
    from fobi.constants import CALLBACK_FORM_VALID
    from fobi.contrib.plugins.form_handlers.db_store.models import (
        SavedFormDataEntry
    )


    class AutoDbStore(FormCallback):

        stage = CALLBACK_FORM_VALID

        def callback(self, form_entry, request, form):
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
                form_data_headers=json.dumps(field_name_to_label_map),
                saved_data=json.dumps(cleaned_data)
            )
            saved_form_data_entry.save()


    form_callback_registry.register(AutoDbStore)
