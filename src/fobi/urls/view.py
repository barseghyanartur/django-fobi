from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from fobi.views import (
    form_entry_submitted,
    view_form_entry,
    form_wizard_entry_submitted,
    FormWizardView
)

__title__ = 'fobi.urls.view'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

urlpatterns = [
    # ***********************************************************************
    # ****************************** Form entry *****************************
    # ***********************************************************************
    # Form submitted success page
    url(_(r'^view/submitted/$'),
        view=form_entry_submitted,
        name='fobi.form_entry_submitted'),

    # View form entry
    url(_(r'^view/(?P<form_entry_slug>[\w_\-]+)/$'),
        view_form_entry,
        name='fobi.view_form_entry'),

    # Form submitted success page
    url(_(r'^view/(?P<form_entry_slug>[\w_\-]+)/submitted/$'),
        view=form_entry_submitted,
        name='fobi.form_entry_submitted'),

    # ***********************************************************************
    # *************************** Form wizard entry *************************
    # ***********************************************************************
    # Form wizard submitted success page
    url(_(r'^wizard-view/submitted/$'),
        view=form_wizard_entry_submitted,
        name='fobi.form_wizard_entry_submitted'),

    # View form wizard entry
    url(_(r'^wizard-view/(?P<form_wizard_entry_slug>[\w_\-]+)/$'),
        FormWizardView.as_view(),
        name='fobi.view_form_wizard_entry'),

    # Form wizard submitted success page
    url(_(r'^wizard-view/(?P<form_wizard_entry_slug>[\w_\-]+)/submitted/$'),
        view=form_wizard_entry_submitted,
        name='fobi.form_wizard_entry_submitted'),
]
