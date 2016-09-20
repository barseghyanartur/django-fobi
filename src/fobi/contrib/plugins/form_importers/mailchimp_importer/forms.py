import mailchimp

from django import forms

__title__ = 'fobi.contrib.plugins.form_importers.mailchimp_importer.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailchimpAPIKeyForm', 'MailchimpListIDForm',)


class MailchimpAPIKeyForm(forms.Form):
    """MailchimpAPIKeyForm.

    First form the the wizard. Here users are supposed to provide the
    API key of their Mailchimp account.
    """
    api_key = forms.CharField(required=True)


class MailchimpListIDForm(forms.Form):
    """MailchimpListIDForm.

    Second form of the wizard. Here users are supposed to choose the form
    they want to import.
    """
    list_id = forms.ChoiceField(required=True, choices=[])

    def __init__(self, *args, **kwargs):
        """Constructor."""
        self._api_key = None

        if 'api_key' in kwargs:
            self._api_key = kwargs.pop('api_key', None)

        super(MailchimpListIDForm, self).__init__(*args, **kwargs)

        if self._api_key:
            client = mailchimp.Mailchimp(self._api_key)
            lists = client.lists.list()
            choices = [(l['id'], l['name']) for l in lists['data']]
            self.fields['list_id'].choices = choices
        # else:
        #     self.fields['list_id'] = forms.CharField(required=True)
