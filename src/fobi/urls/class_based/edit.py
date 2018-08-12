# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from fobi.views.class_based import (
    CreateFormWizardEntryView,
    EditFormWizardEntryView,
    FormWizardDashboardView,
    FormDashboardView,
    CreateFormEntryView,
    EditFormEntryView,
    AddFormElementEntryView,
    EditFormElementEntryView,
    DeleteFormElementEntryView,
    AddFormHandlerEntryView,
    AddFormWizardFormEntryView,
    DeleteFormEntryView,
)


__title__ = 'fobi.urls.class_based'
__author__ = 'Kyle Roux <jstacoder@gmail.com>'
__copyright__ = '2018 Kyle Roux'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

urlpatterns = [
    # *********************************************************************
    # **************************** Dashboards *****************************
    # *********************************************************************

    # wizard dashboard
    url(_(r'^wizards/$'),
        view=FormWizardDashboardView.as_view(),
        name='fobi.form_wizards_dashboard'),

    # form dashbaord
    url(_(r'^$'),
        view=FormDashboardView.as_view(),
        name='fobi.dashboard'),

    # ********************************************************************
    # ************************* Form Wizard Entry C**UD ******************
    # ********************************************************************

    # create form wizard entry
    url(_(r'^wizard/create/$'),
        view=CreateFormWizardEntryView.as_view(),
        name='fobi.create_form_wizard_entry'),

    # edit form wizard entry
    url(_(r'^wizard/edit/(?P<form_wizard_entry_id>\d+)/$'),
        view=EditFormWizardEntryView.as_view(),
        name='fobi.edit_form_wizard_entry'),

    # ************************************************************
    # **************************** Form Entry CUD*****************
    # ************************************************************

    # create form entry
    url(_(r'^forms/create/$'),
        view=CreateFormEntryView.as_view(),
        name='fobi.create_form_entry'),

    # edit form entry
    url(_(r'^forms/edit/(?P<form_entry_id>\d+)/$'),
        view=EditFormEntryView.as_view(),
        name='fobi.edit_form_entry'),

    # Delete form entry
    url(_(r'^forms/delete/(?P<form_entry_id>\d+)/$'),
        view=DeleteFormEntryView.as_view(),
        name='fobi.delete_form_entry'),


    # ************************************************************
    # **************************** Form Element Entry CUD*********
    # ************************************************************

    # add form element entry
    url(_(r'^forms/elements/add/(?P<form_entry_id>\d+)/'
          r'(?P<form_element_plugin_uid>[\w_\-]+)/$'),
        view=AddFormElementEntryView.as_view(),
        name='fobi.add_form_element_entry'),

    # edit form element entry
    url(_(r'^forms/elements/edit/(?P<form_element_entry_id>\d+)/$'),
        view=EditFormElementEntryView.as_view(),
        name='fobi.edit_form_element_entry'),

    # delete form element entry
    url(_(r'^forms/elements/delete/(?P<form_element_entry_id>\d+)/$'),
        view=DeleteFormElementEntryView.as_view(),
        name='fobi.delete_form_element_entry'),

    # ***********************************************************************
    # *********************** Form handler entry CUD ************************
    # ***********************************************************************


    # add form handler entry
    url(_(r'^forms/handlers/add/(?P<form_entry_id>\d+)/'
          r'(?P<form_handler_plugin_uid>[\w_\-]+)/$'),
        view=AddFormHandlerEntryView.as_view(),
        name='fobi.add_form_handler_entry'),


    # ***********************************************************************
    # ******************** Form wizard form entry CUD ***********************
    # ***********************************************************************

    # add form wizard form entry
    url(_(r'^wizard/forms/add/(?P<form_wizard_entry_id>\d+)/'
          r'(?P<form_entry_id>[\w_\-]+)/$'),
        view=AddFormWizardFormEntryView.as_view(),
        name='fobi.add_form_wizard_form_entry'),
]

