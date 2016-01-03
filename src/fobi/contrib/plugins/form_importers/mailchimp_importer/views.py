__title__ = 'fobi.contrib.plugins.form_importers.mailchimp_importer.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailchimpImporterWizardView',)

import logging

import mailchimp

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from nine.versions import DJANGO_GTE_1_8

if DJANGO_GTE_1_8:
    from formtools.wizard.views import SessionWizardView#, CookieWizardView
else:
    from django.contrib.formtools.wizard.views import SessionWizardView

from .forms import MailchimpAPIKeyForm, MailchimpListIDForm

logger = logging.getLogger(__name__)

class MailchimpImporterWizardView(SessionWizardView):
    """
    """
    form_list = [MailchimpAPIKeyForm, MailchimpListIDForm]

    def get_form_kwargs(self, step):
        """
        """
        #logger.debug('step: ' + step)
        #logger.debug(self.request.session.__dict__)
        if '1' == step:
            data = self.get_cleaned_data_for_step('0') or {}
            api_key = data.get('api_key', None)
            return {'api_key': api_key}
        return {}

    def done(self, form_list, **kwargs):
        # Merging cleaned data into one dict
        cleaned_data = {}
        for form in form_list:
            cleaned_data.update(form.cleaned_data)
        #cleaned_data = self.get_all_cleaned_data()

        # Connecting to mailchimp
        client = mailchimp.Mailchimp(cleaned_data['api_key'])

        # Fetching the form data
        form_data = client.lists.merge_vars(
            id={'list_id': cleaned_data['list_id']}
        )

        # We need the first form only
        try:
            form_data = form_data['data'][0]
        except Exception as err:
            messages.warning(
                self.request,
                _('Selected form could not be imported due errors.')
            )
            return redirect(reverse('fobi.dashboard'))

        # Actually, import the form
        form_entry = self._form_importer.import_data(
            {'name': form_data['name'], 'user': self.request.user},
            form_data['merge_vars']
        )

        redirect_url = reverse(
            'fobi.edit_form_entry', kwargs={'form_entry_id': form_entry.pk}
        )

        messages.info(
            self.request,
            _('Form {0} imported successfully.').format(form_data['name'])
        )

        return redirect("{0}".format(redirect_url))
