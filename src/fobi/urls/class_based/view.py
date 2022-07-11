from django.urls import re_path as url
from django.utils.translation import gettext_lazy as _

from ...views import (
    FormWizardView,
    form_entry_submitted,
    form_wizard_entry_submitted,
    view_form_entry,
)
from ...views.class_based import ViewFormEntrySubmittedView, ViewFormEntryView

__title__ = "fobi.urls.class_based.view"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("urlpatterns",)

urlpatterns = [
    # ***********************************************************************
    # ****************************** Form entry *****************************
    # ***********************************************************************
    # Form submitted success page
    url(
        _(r"^view/submitted/$"),
        # view=form_entry_submitted,
        view=ViewFormEntrySubmittedView.as_view(),
        name="fobi.form_entry_submitted",
    ),
    # View form entry
    url(
        _(r"^view/(?P<form_entry_slug>[\w_\-]+)/$"),
        # view=view_form_entry,
        view=ViewFormEntryView.as_view(),
        name="fobi.view_form_entry",
    ),
    # Form submitted success page
    url(
        _(r"^view/(?P<form_entry_slug>[\w_\-]+)/submitted/$"),
        # view=form_entry_submitted,
        view=ViewFormEntrySubmittedView.as_view(),
        name="fobi.form_entry_submitted",
    ),
    # ***********************************************************************
    # *************************** Form wizard entry *************************
    # ***********************************************************************
    # Form wizard submitted success page
    url(
        _(r"^wizard-view/submitted/$"),
        view=form_wizard_entry_submitted,
        name="fobi.form_wizard_entry_submitted",
    ),
    # View form wizard entry
    url(
        _(r"^wizard-view/(?P<form_wizard_entry_slug>[\w_\-]+)/$"),
        FormWizardView.as_view(),
        name="fobi.view_form_wizard_entry",
    ),
    # Form wizard submitted success page
    url(
        _(r"^wizard-view/(?P<form_wizard_entry_slug>[\w_\-]+)/submitted/$"),
        view=form_wizard_entry_submitted,
        name="fobi.form_wizard_entry_submitted",
    ),
]
