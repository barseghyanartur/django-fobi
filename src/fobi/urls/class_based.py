from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from fobi.views.class_based import (
    CreateFormWizardEntryView,
    EditFormWizardEntryView,
    FormWizardDashboardView,
    FormDashboardView,
    CreateFormEntryView,
    EditFormEntryView,
)

__title__ = 'fobi.urls.class_based'
__author__ = 'Kyle Roux <jstacoder@gmail.com>'
__copyright__ = '2018 Kyle Roux'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    # *********************************************************************
    # **************************** Dashboards ***************************
    # *********************************************************************

    # wizard dashboard
    url( _(r'^dashboard/wizards/$'), 
            view=FormWizardDashboardView.as_view(),
            name='fobi.class_based.form_wizards_dashboard'),
           
    # form dashbaord
    url(_(r'^dashboard/forms/$'),
        view=FormDashboardView.as_view(),
        name='fobi.class_based.dashboard'),
        
    # ********************************************************************
    # **************************** Form WIzard Entry CUD***************
    # ********************************************************************

    # create form wizard entry
    url(_(r'^wizard/create/$'),
        view=CreateFormWizardEntryView.as_view(),
        name='fobi.class_based.create_form_wizard_entry'),
    
    # edit form wizard entry
    url(_(r'^wizard/edit/(?P<form_wizard_entry_id>\d+)/$'),
        view=EditFormWizardEntryView.as_view(),
        name='fobi.class_based.edit_form_wizard_entry'),

    # ************************************************************
    # **************************** Form Entry CUD**************
    # ************************************************************

    # create form entry
    url(_(r'^forms/create/$'),
        view=CreateFormEntryView.as_view(),
        name='fobi.class_based.create_form_entry'),
    
    # edit form entry
    url(_(r'^forms/edit/(?P<form_entry_id>\d+)/$'),
        view=EditFormEntryView,
        name='fobi.class_based.edit_form_entry'),
]

