from .....base import FormCallback, get_processed_form_data
from .....constants import CALLBACK_FORM_VALID
from .....helpers import safe_text
from .helpers import send_mail
from .mixins import MailHandlerMixin
from .settings import (
    AUTO_MAIL_TO,
    AUTO_MAIL_BODY,
    AUTO_MAIL_FROM,
    AUTO_MAIL_SUBJECT,
    MULTI_EMAIL_FIELD_VALUE_SPLITTER,
)

__title__ = 'fobi.contrib.plugins.form_handlers.mail.callbacks'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AutoFormMail',
)


class AutoFormMail(FormCallback, MailHandlerMixin):
    """Auto mail form entries.

    Note, that this callback is not active. In order to activate it, you
    should import the ``AutoFormMail`` and register it using the
    callback register as follows.

    >>> from fobi.base import form_callback_registry
    >>> from fobi.contrib.plugins.form_handlers.mail.callbacks import (
    >>>     AutoFormMail
    >>> )
    >>> form_callback_registry.register(AutoFormMail)
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

        base_url = self.get_base_url(request)

        # Clean up the values, leave our content fields and empty values.
        field_name_to_label_map, cleaned_data = get_processed_form_data(
            form,
            form_element_entries
        )

        rendered_data = self.get_rendered_data(
            cleaned_data,
            field_name_to_label_map,
            base_url
        )

        files = self._prepare_files(request, form)

        self.send_email(rendered_data, files)

    def send_email(self, rendered_data, files):
        """Send email.

        Might be used in integration packages.
        """
        # Handling more than one email address
        if isinstance(AUTO_MAIL_TO, (list, tuple)):
            to_email = AUTO_MAIL_TO
        else:
            # Assume that it's string
            to_email = AUTO_MAIL_TO.split(
                MULTI_EMAIL_FIELD_VALUE_SPLITTER
            )

        send_mail(
            safe_text(AUTO_MAIL_SUBJECT),
            "{0}\n\n{1}".format(
                safe_text(AUTO_MAIL_BODY),
                ''.join(rendered_data)
            ),
            AUTO_MAIL_FROM,
            to_email,
            fail_silently=False,
            attachments=files.values()
        )
