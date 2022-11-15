from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .....base import (
    get_form_handler_plugin_widget,
    get_form_wizard_handler_plugin_widget,
)
from . import UID
from .helpers import DataExporter
from .models import SavedFormDataEntry, SavedFormWizardDataEntry

__title__ = "fobi.contrib.plugins.form_handlers.db_store.views"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "Copyright (c) 2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "view_saved_form_data_entries",
    "export_saved_form_data_entries",
    "view_saved_form_wizard_data_entries",
    "export_saved_form_wizard_data_entries",
)

# *****************************************************************************
# *************************** Form handler views ******************************
# *****************************************************************************

# entries_permissions = [
#    'db_store.add_savedformdataentry',
#    'db_store.change_savedformdataentry',
#    'db_store.delete_savedformdataentry',
# ]


# @permissions_required(satisfy=SATISFY_ANY, perms=entries_permissions)
@login_required
def view_saved_form_data_entries(
    request,
    form_entry_id=None,
    theme=None,
    template_name="db_store/view_saved_form_data_entries.html",
):
    """View saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """
    entries = SavedFormDataEntry._default_manager.select_related(
        "form_entry"
    ).filter(form_entry__user__pk=request.user.pk)

    if form_entry_id:
        entries = entries.filter(form_entry__id=form_entry_id)

    context = {"entries": entries, "form_entry_id": form_entry_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({"fobi_theme": theme})

    widget = get_form_handler_plugin_widget(
        UID, request=request, as_instance=True, theme=theme
    )

    if widget and widget.view_saved_form_data_entries_template_name:
        template_name = widget.view_saved_form_data_entries_template_name

    return render(request, template_name, context)


@login_required
def export_saved_form_data_entries(request, form_entry_id=None, theme=None):
    """Export saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :return django.http.HttpResponse:
    """
    entries = SavedFormDataEntry._default_manager.select_related(
        "form_entry"
    ).filter(form_entry__user__pk=request.user.pk)

    if form_entry_id:
        entries = entries.filter(form_entry__id=form_entry_id)

    data_exporter = DataExporter(entries, ["form_entry"])

    return data_exporter.graceful_export()


# *****************************************************************************
# ************************ Form wizard handler views  *************************
# *****************************************************************************


@login_required
def view_saved_form_wizard_data_entries(
    request,
    form_wizard_entry_id=None,
    theme=None,
    template_name="db_store/view_saved_form_wizard_data_entries.html",
):
    """View saved form wizard data entries.

    :param django.http.HttpRequest request:
    :param int form_wizard_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """
    entries = SavedFormWizardDataEntry._default_manager.select_related(
        "form_wizard_entry"
    ).filter(form_wizard_entry__user__pk=request.user.pk)

    if form_wizard_entry_id:
        entries = entries.filter(form_wizard_entry__id=form_wizard_entry_id)

    context = {"entries": entries, "form_wizard_entry_id": form_wizard_entry_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({"fobi_theme": theme})

    widget = get_form_wizard_handler_plugin_widget(
        UID, request=request, as_instance=True, theme=theme
    )

    if widget and widget.view_saved_form_wizard_data_entries_template_name:
        template_name = widget.view_saved_form_wizard_data_entries_template_name

    return render(request, template_name, context)


@login_required
def export_saved_form_wizard_data_entries(
    request, form_wizard_entry_id=None, theme=None
):
    """Export saved form wizard data entries.

    :param django.http.HttpRequest request:
    :param int form_wizard_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :return django.http.HttpResponse:
    """
    entries = SavedFormWizardDataEntry._default_manager.select_related(
        "form_wizard_entry"
    ).filter(form_wizard_entry__user__pk=request.user.pk)

    if form_wizard_entry_id:
        entries = entries.filter(form_wizard_entry__id=form_wizard_entry_id)

    data_exporter = DataExporter(entries, ["form_wizard_entry"])

    return data_exporter.graceful_export()
