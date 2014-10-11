__title__ = 'fobi.contrib.plugins.form_handlers.db_store.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'view_saved_form_data_entries',
)

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

#from fobi.decorators import permissions_required, SATISFY_ALL, SATISFY_ANY
from fobi.contrib.plugins.form_handlers.db_store.models import (
    SavedFormDataEntry
)

#entries_permissions = [
#    'db_store.add_savedformdataentry',
#    'db_store.change_savedformdataentry',
#    'db_store.delete_savedformdataentry',
#]

#@permissions_required(satisfy=SATISFY_ANY, perms=entries_permissions)
@login_required
def view_saved_form_data_entries(request, form_id=None, theme=None, \
                                 template_name='db_store/view_saved_form_data_entries.html'):
    """
    View saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """
    entries = SavedFormDataEntry._default_manager \
                                .filter(user__pk=request.user.pk) \
                                .select_related('form_entry')

    if form_id:
        entries = entries.filter(form__id=form_id)

    context = {'entries': entries, 'form_id': form_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
        )
