import json

from django.core.mail import send_mail

from fobi.base import FormHandlerPlugin, form_handler_plugin_registry

from sample_mail.forms import SampleMailForm


class SampleMailHandlerPlugin(FormHandlerPlugin):
    """SampleMailHandlerPlugin."""

    uid = "sample_mail"
    name = _("Sample mail")
    form = SampleMailForm

    def run(self, form_entry, request, form):
        send_mail(
            self.data.subject,
            json.dumps(form.cleaned_data),
            self.data.from_email,
            [self.data.to_email],
            fail_silently=True
        )

    def plugin_data_repr(self):
        """Human readable representation of plugin data.

        :return str:
        """
        return self.data.__dict__


form_handler_plugin_registry.register(SampleMailHandlerPlugin)
