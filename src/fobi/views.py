__title__ = 'fobi.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'create_form_entry', 'edit_form_entry', 'delete_form_entry',
    'add_form_element_entry', 'edit_form_element_entry',
    'delete_form_element_entry', 'add_form_handler_entry',
    'edit_form_handler_entry', 'delete_form_handler_entry',
    'dashboard', 'view_form_entry', 'form_entry_submitted',
)

import logging

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.decorators import login_required, permission_required
from django.db import models, IntegrityError
from django.utils.datastructures import MultiValueDictKeyError

from fobi.models import FormEntry, FormElementEntry, FormHandlerEntry
from fobi.forms import FormEntryForm, FormElementEntryFormSet
from fobi.dynamic import assemble_form_class
from fobi.decorators import permissions_required, SATISFY_ALL, SATISFY_ANY
from fobi.base import (
    fire_form_callbacks, run_form_handlers, form_element_plugin_registry,
    form_handler_plugin_registry, submit_plugin_form_data, get_theme
    )
from fobi.constants import (
    CALLBACK_BEFORE_FORM_VALIDATION,
    CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
    CALLBACK_FORM_VALID, CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
    CALLBACK_FORM_INVALID
    )
from fobi.utils import (
    get_user_form_field_plugin_uids,
    #get_user_form_element_plugins,
    get_user_form_element_plugins_grouped,
    #get_user_form_handler_plugins_grouped,
    get_user_form_handler_plugins, get_user_form_handler_plugin_uids,
    append_edit_and_delete_links_to_field
    )
from fobi.settings import DEBUG

logger = logging.getLogger(__name__)

# *****************************************************************************
# *****************************************************************************
# *********************************** Generic *********************************
# *****************************************************************************
# *****************************************************************************

def _delete_plugin_entry(request, entry_id, EntryModel, \
                         get_user_plugin_uids_func, message, html_anchor):
    """
    Abstract delete element entry.

    :param django.http.HttpRequest request:
    :param int entry_id:
    :param fobi.models.AbstractPluginEntry EntryModel: Subclass of
        ``fobi.models.AbstractPluginEntry``.
    :param callable get_user_plugin_uids_func:
    :return django.http.HttpResponse:
    """
    try:
        obj = EntryModel._default_manager \
                        .select_related('form_entry') \
                        .get(pk=entry_id, form_entry__user__pk=request.user.pk)
    except ObjectDoesNotExist as e:
        raise Http404(_("{0} not found.").format(EntryModel._meta.verbose_name))

    form_entry = obj.form_entry
    plugin = obj.get_plugin(request=request)
    plugin.request = request

    plugin._delete_plugin_data()

    obj.delete()

    messages.info(request, message.format(plugin.name))

    redirect_url = reverse(
        'fobi.edit_form_entry', kwargs={'form_entry_id': form_entry.pk}
        )
    return redirect("{0}{1}".format(redirect_url, html_anchor))

# *****************************************************************************
# *****************************************************************************
# ********************************* Dashboard *********************************
# *****************************************************************************
# *****************************************************************************

dashboard_permissions = [
    'fobi.add_formentry',
    'fobi.change_formentry',
    'fobi.delete_formentry',
]

@login_required
@permissions_required(satisfy=SATISFY_ANY, perms=dashboard_permissions)
def dashboard(request, theme=None, template_name=None):
    """
    Dashboard.

    :param django.http.HttpRequest request:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    form_entries = FormEntry._default_manager \
                            .filter(user__pk=request.user.pk) \
                            .select_related('user')

    context = {'form_entries': form_entries}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        theme = get_theme(request=request, as_instance=True)
        template_name = theme.dashboard_template

    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
        )

# *****************************************************************************
# *****************************************************************************
# ********************************** Builder **********************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# **************************** Create form entry ******************************
# *****************************************************************************

create_form_entry_permissions = [
    'fobi.add_formentry',
    'fobi.add_formelemententry',
    'fobi.add_formhandlerentry',
]

@login_required
@permissions_required(satisfy=SATISFY_ALL, perms=create_form_entry_permissions)
def create_form_entry(request, theme=None, template_name=None):
    """
    :param django.http.HttpRequest request:
    :return django.http.HttpResponse:
    """
    if 'POST' == request.method:
        form = FormEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form_entry = form.save(commit=False)
            form_entry.user = request.user
            try:
                form_entry.save()
                messages.info(
                    request,
                    _('Form {0} was created successfully.').format(form_entry.name)
                    )
                return redirect(
                    'fobi.edit_form_entry', form_entry_id=form_entry.pk
                    )
            except IntegrityError as e:
                messages.info(
                    request,
                    _('Errors occured while saving the form: {0}.').format(str(e))
                    )

    else:
        form = FormEntryForm()

    context = {'form': form}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        if not theme:
            theme = get_theme(request=request, as_instance=True)
        template_name = theme.create_form_entry_template

    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
        )

# **************************************************************************
# ******************************* Edit form entry **************************
# **************************************************************************

edit_form_entry_permissions = [
    'fobi.change_formentry', 'fobi.change_formelemententry',
    'fobi.change_formhandlerentry',
    'fobi.add_formelemententry', 'fobi.add_formhandlerentry',
    'fobi.delete_formelemententry', 'fobi.delete_formhandlerentry',
]

@login_required
@permissions_required(satisfy=SATISFY_ANY, perms=edit_form_entry_permissions)
def edit_form_entry(request, form_entry_id, theme=None, template_name=None):
    """
    Edit form entry.

    :param django.http.HttpRequest request:
    :param int form_entry_id:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        form_entry = FormEntry._default_manager \
                              .select_related('user') \
                              .prefetch_related('formelemententry_set') \
                              .get(pk=form_entry_id, user__pk=request.user.pk)
                              #.prefetch_related('formhandlerentry_set') \
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    if 'POST' == request.method:
        # The form entry form (does not contain form elenments)
        form = FormEntryForm(request.POST, request.FILES, instance=form_entry)

        if 'ordering' in request.POST:
            form_element_entry_formset = FormElementEntryFormSet(
                request.POST,
                request.FILES,
                queryset = form_entry.formelemententry_set.all(),
                #prefix = 'form_element'
                )
            # If form elements aren't properly made (developers's fault)
            # there might be problems with saving the ordering - likely
            # in case of hidden elements only. Thus, we want to avoid
            # errors here.
            try:
                if form_element_entry_formset.is_valid():
                    form_element_entry_formset.save()
                    messages.info(
                        request,
                        _("Elements ordering edited successfully.")
                        )
                    return redirect(
                        reverse('fobi.edit_form_entry', kwargs={'form_entry_id': form_entry_id})
                        )
            except MultiValueDictKeyError as e:
                messages.error(
                    request,
                    _("Errors occured while trying to change the elements ordering!")
                    )
                return redirect(
                    reverse('fobi.edit_form_entry', kwargs={'form_entry_id': form_entry_id})
                    )
        else:
            form_element_entry_formset = FormElementEntryFormSet(
                queryset = form_entry.formelemententry_set.all(),
                #prefix = 'form_element'
                )

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            try:
                obj.save()
                messages.info(
                    request,
                    _('Form {0} was edited successfully.').format(form_entry.name)
                    )
                return redirect(
                    reverse('fobi.edit_form_entry', kwargs={'form_entry_id': form_entry_id})
                    )
            except IntegrityError as e:
                messages.info(
                    request,
                    _('Errors occured while saving the form: {0}.').format(str(e))
                    )
    else:
        # The form entry form (does not contain form elenments)
        form = FormEntryForm(instance=form_entry)

        form_element_entry_formset = FormElementEntryFormSet(
            queryset = form_entry.formelemententry_set.all(),
            #prefix = 'form_element'
            )

    # In case of success, we don't need this (since redirect would happen).
    # Thus, fetch only if needed.
    form_elements = form_entry.formelemententry_set.all()
    form_handlers = form_entry.formhandlerentry_set.all()
    all_form_entries = FormEntry._default_manager.only('id', 'name', 'slug') \
                                .filter(user__pk=request.user.pk)
    user_form_element_plugins = get_user_form_element_plugins_grouped(
        request.user
        )
    user_form_handler_plugins = get_user_form_handler_plugins(request.user)
    # Assembling the form for preview
    FormClass = assemble_form_class(
        form_entry,
        origin = 'edit_form_entry',
        origin_kwargs_update_func = append_edit_and_delete_links_to_field
        )

    assembled_form = FormClass()

    # In debug mode, try to identify possible problems.
    if DEBUG:
        try:
            assembled_form.as_p()
        except Exception as e:
            logger.error(e)

    # If no theme provided, pick a default one.
    if not theme:
        theme = get_theme(request=request, as_instance=True)

    theme.collect_plugin_media(form_elements)

    context = {
        'form': form,
        'form_entry': form_entry,
        'form_elements': form_elements,
        'form_handlers': form_handlers,
        'all_form_entries': all_form_entries,
        'user_form_element_plugins': user_form_element_plugins,
        'user_form_handler_plugins': user_form_handler_plugins,
        'assembled_form': assembled_form,
        'form_element_entry_formset': form_element_entry_formset,
        'fobi_theme': theme,
    }

    if not template_name:
        template_name = theme.edit_form_entry_template

    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
        )

# *****************************************************************************
# **************************** Add form element entry *************************
# *****************************************************************************

@login_required
@permission_required('fobi.add_formelemententry')
def add_form_element_entry(request, form_entry_id, form_element_plugin_uid, \
                           theme=None, template_name=None):
    """
    Add form element entry.

    :param django.http.HttpRequest request:
    :param int form_entry_id:
    :param int form_element_plugin_uid:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        form_entry = FormEntry._default_manager \
                              .prefetch_related('formelemententry_set') \
                              .get(pk=form_entry_id)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    form_elements = form_entry.formelemententry_set.all()

    user_form_element_plugin_uids = get_user_form_field_plugin_uids(
        request.user
        )

    if not form_element_plugin_uid in user_form_element_plugin_uids:
        raise Exception("Plugin does not exist or you are not allowed to "
                        "use this plugin!")

    FormElementPlugin = form_element_plugin_registry.get(
        form_element_plugin_uid
        )
    form_element_plugin = FormElementPlugin(user=request.user)
    form_element_plugin.request = request

    FormElementPluginForm = form_element_plugin.get_form()
    form = None

    obj = FormElementEntry()
    obj.form_entry = form_entry
    obj.plugin_uid = form_element_plugin_uid
    obj.user = request.user

    save_object = False

    # If plugin doesn't have a form
    if not FormElementPluginForm:
        save_object = True

    # If POST
    elif 'POST' == request.method:
        # If element has a form
        form = form_element_plugin.get_initialised_create_form_or_404(
            data = request.POST,
            files = request.FILES
            )
        form.validate_plugin_data(form_elements, request=request)
        if form.is_valid():
            # Saving the plugin form data.
            form.save_plugin_data(request=request)

            # Getting the plugin data.
            obj.plugin_data = form.get_plugin_data(request=request)

            save_object = True

    # If not POST
    else:
        form = form_element_plugin.get_initialised_create_form_or_404()

    if save_object:
        # Handling the position
        position = 1
        records = FormElementEntry._default_manager \
                                  .aggregate(models.Max('position'))
        if records:
            try:
                position = records['{0}__max'.format('position')] + 1

            except TypeError as e:
                pass

        obj.position = position

        # Save the object.
        obj.save()

        messages.info(
            request,
            _('The form element plugin "{0}" was added '
              'successfully.').format(form_element_plugin.name)
            )
        return redirect(
            "{0}?active_tab=tab-form-elemenets".format(reverse('fobi.edit_form_entry', kwargs={'form_entry_id': form_entry_id}))
            )

    context = {
        'form': form,
        'form_entry': form_entry,
        'form_element_plugin': form_element_plugin,
    }

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        if not theme:
            theme = get_theme(request=request, as_instance=True)
        template_name = theme.add_form_element_entry_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# **************************** Edit form element entry ************************
# *****************************************************************************

@login_required
@permission_required('fobi.change_formelemententry')
def edit_form_element_entry(request, form_element_entry_id, theme=None, \
                            template_name=None):
    """
    Edit form element entry.

    :param django.http.HttpRequest request:
    :param int form_element_entry_id:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        obj = FormElementEntry._default_manager \
                              .select_related('form_entry', 'form_entry__user') \
                              .get(pk=form_element_entry_id,
                                   form_entry__user__pk=request.user.pk)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form element entry not found."))

    form_entry = obj.form_entry
    form_element_plugin = obj.get_plugin(request=request)
    form_element_plugin.request = request

    FormElementPluginForm = form_element_plugin.get_form()
    form = None

    if not FormElementPluginForm:
        messages.info(
            request,
            _('The form element plugin "{0}" is not configurable!').format(
                form_element_plugin.name
                )
            )
        return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)

    elif 'POST' == request.method:
        form = form_element_plugin.get_initialised_edit_form_or_404(
            data = request.POST,
            files = request.FILES
            )

        form_elements = FormElementEntry._default_manager \
                                        .select_related('form_entry', \
                                                        'form_entry__user') \
                                        .exclude(pk=form_element_entry_id) \
                                        .filter(form_entry=form_entry)

        form.validate_plugin_data(form_elements, request=request)

        if form.is_valid():
            # Saving the plugin form data.
            form.save_plugin_data(request=request)

            # Getting the plugin data.
            obj.plugin_data = form.get_plugin_data(request=request)

            # Save the object.
            obj.save()

            messages.info(
                request,
                _('The form element plugin "{0}" was edited '
                  'successfully.').format(form_element_plugin.name)
                )

            return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)

    else:
        form = form_element_plugin.get_initialised_edit_form_or_404()

    form_element_plugin = obj.get_plugin(request=request)
    form_element_plugin.request = request

    context = {
        'form': form,
        'form_entry': form_entry,
        'form_element_plugin': form_element_plugin,
    }

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        if not theme:
            theme = get_theme(request=request, as_instance=True)
        template_name = theme.edit_form_element_entry_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# **************************** Delete form element entry **********************
# *****************************************************************************

@login_required
@permission_required('fobi.delete_formelemententry')
def delete_form_element_entry(request, form_element_entry_id):
    """
    Delete form element entry.

    :param django.http.HttpRequest request:
    :param int form_element_entry_id:
    :return django.http.HttpResponse:
    """
    return _delete_plugin_entry(
        request = request,
        entry_id = form_element_entry_id,
        EntryModel = FormElementEntry,
        get_user_plugin_uids_func = get_user_form_field_plugin_uids,
        message = _('The form element plugin "{0}" was deleted successfully.'),
        html_anchor = '?active_tab=tab-form-elemenets'
        )

# *****************************************************************************
# **************************** Add form handler entry *************************
# *****************************************************************************

@login_required
@permission_required('fobi.add_formhandlerentry')
def add_form_handler_entry(request, form_entry_id, form_handler_plugin_uid, \
                           theme=None, template_name=None):
    """
    Add form handler entry.

    :param django.http.HttpRequest request:
    :param int form_entry_id:
    :param int form_handler_plugin_uid:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        form_entry = FormEntry._default_manager.get(pk=form_entry_id)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    user_form_handler_plugin_uids = get_user_form_handler_plugin_uids(
        request.user
        )

    if not form_handler_plugin_uid in user_form_handler_plugin_uids:
        raise Exception(_("Plugin does not exist or you are not allowed to "
                          " use this plugin!"))

    FormHandlerPlugin = form_handler_plugin_registry.get(
        form_handler_plugin_uid
        )
    form_handler_plugin = FormHandlerPlugin(user=request.user)
    form_handler_plugin.request = request

    FormHandlerPluginForm = form_handler_plugin.get_form()
    form = None

    obj = FormHandlerEntry()
    obj.form_entry = form_entry
    obj.plugin_uid = form_handler_plugin_uid
    obj.user = request.user

    save_object = False

    if not FormHandlerPluginForm:
        save_object = True

    elif 'POST' == request.method:
        form = form_handler_plugin.get_initialised_create_form_or_404(
            data = request.POST,
            files = request.FILES
            )
        if form.is_valid():
            # Saving the plugin form data.
            form.save_plugin_data(request=request)

            # Getting the plugin data.
            obj.plugin_data = form.get_plugin_data(request=request)

            save_object = True

    else:
        form = form_handler_plugin.get_initialised_create_form_or_404()

    if save_object:
        # Save the object.
        obj.save()

        messages.info(
            request,
            _('The form handler plugin "{0}" was added successfully.').format(
                form_handler_plugin.name
                )
            )
        return redirect(
            "{0}?active_tab=tab-form-handlers".format(
                reverse(
                    'fobi.edit_form_entry',
                    kwargs = {'form_entry_id': form_entry_id}
                    )
                )
            )

    context = {
        'form': form,
        'form_entry': form_entry,
        'form_handler_plugin': form_handler_plugin,
    }

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        if not theme:
            theme = get_theme(request=request, as_instance=True)
        template_name = theme.add_form_handler_entry_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# **************************** Edit form handler entry ************************
# *****************************************************************************

@login_required
@permission_required('fobi.change_formhandlerentry')
def edit_form_handler_entry(request, form_handler_entry_id, theme=None, \
                            template_name=None):
    """
    Edit form handler entry.

    :param django.http.HttpRequest request:
    :param int form_element_entry_id:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        obj = FormHandlerEntry._default_manager \
                              .select_related('form_entry') \
                              .get(pk=form_handler_entry_id)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form handler entry not found."))

    form_entry = obj.form_entry

    form_handler_plugin = obj.get_plugin(request=request)
    form_handler_plugin.request = request

    FormHandlerPluginForm = form_handler_plugin.get_form()
    form = None

    if not FormHandlerPluginForm:
        messages.info(
            request,
            _('The form handler plugin "{0}" is not '
              'configurable!').format(form_handler_plugin.name)
            )
        return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)

    elif 'POST' == request.method:
        form = form_handler_plugin.get_initialised_edit_form_or_404(
            data = request.POST,
            files = request.FILES
            )

        if form.is_valid():
            # Saving the plugin form data.
            form.save_plugin_data(request=request)

            # Getting the plugin data.
            obj.plugin_data = form.get_plugin_data(request=request)

            # Save the object.
            obj.save()

            messages.info(
                request,
                _('The form handler plugin "{0}" was edited '
                  'successfully.').format(form_handler_plugin.name)
                )

            return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)

    else:
        form = form_handler_plugin.get_initialised_edit_form_or_404()

    context = {
        'form': form,
        'form_entry': form_entry,
        'form_handler_plugin': form_handler_plugin,
    }

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    if not template_name:
        if not theme:
            theme = get_theme(request=request, as_instance=True)
        template_name = theme.edit_form_handler_entry_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# **************************** Delete form handler entry **********************
# *****************************************************************************

@login_required
@permission_required('fobi.delete_formhandlerentry')
def delete_form_handler_entry(request, form_handler_entry_id):
    """
    Delete form handler entry.

    #TODO - permissions

    :param django.http.HttpRequest request:
    :param int form_element_entry_id:
    :return django.http.HttpResponse:
    """
    return _delete_plugin_entry(
        request = request,
        entry_id = form_handler_entry_id,
        EntryModel = FormHandlerEntry,
        get_user_plugin_uids_func = get_user_form_handler_plugin_uids,
        message = _('The form handler plugin "{0}" was deleted successfully.'),
        html_anchor = '?active_tab=tab-form-handlers'
        )

# *****************************************************************************
# *****************************************************************************
# ******************************** View form entry ****************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# ******************************** View form entry ****************************
# *****************************************************************************

def view_form_entry(request, form_entry_slug, theme=None, template_name=None):
    """
    View create form.

    :param django.http.HttpRequest request:
    :param string form_entry_slug:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        kwargs = {'slug': form_entry_slug}
        if not request.user.is_authenticated():
            kwargs.update({'is_public': True})
        form_entry = FormEntry._default_manager.select_related('user') \
                              .get(**kwargs)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    form_element_entries = form_entry.formelemententry_set.all()[:]

    # This is where the most of the magic happens. Our form is being built
    # dynamically.
    FormClass = assemble_form_class(form_entry,
                                    form_element_entries=form_element_entries)

    if 'POST' == request.method:
        form = FormClass(request.POST, request.FILES)

        # Fire pre form validation callbacks
        fire_form_callbacks(form_entry=form_entry, request=request, form=form,
                            stage=CALLBACK_BEFORE_FORM_VALIDATION)

        if form.is_valid():
            # Fire form valid callbacks, before handling submitted plugin
            # form data.
            form = fire_form_callbacks(
                form_entry = form_entry,
                request = request,
                form = form,
                stage = CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA
                )

            # Fire plugin processors
            form = submit_plugin_form_data(form_entry=form_entry,
                                           request=request, form=form)

            # Fire form valid callbacks
            form = fire_form_callbacks(form_entry=form_entry,
                                       request=request, form=form,
                                       stage=CALLBACK_FORM_VALID)

            # Run all handlers
            run_form_handlers(
                form_entry = form_entry,
                request = request,
                form = form,
                form_element_entries = form_element_entries
                )

            # Fire post handler callbacks
            fire_form_callbacks(
                form_entry = form_entry,
                request = request,
                form = form,
                stage = CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS
                )

            messages.info(
                request,
                _('Form {0} was submitted successfully.').format(form_entry.name)
                )
            return redirect(
                reverse('fobi.form_entry_submitted', args=[form_entry.slug])
                )
        else:
            # Fire post form validation callbacks
            fire_form_callbacks(form_entry=form_entry, request=request,
                                form=form, stage=CALLBACK_FORM_INVALID)

    else:
        form = FormClass()

    # In debug mode, try to identify possible problems.
    if DEBUG:
        try:
            form.as_p()
        except Exception as e:
            logger.error(e)

    theme = get_theme(request=request, as_instance=True)
    theme.collect_plugin_media(form_element_entries)

    context = {
        'form': form,
        'form_entry': form_entry,
        'fobi_theme': theme,
    }

    if not template_name:
        template_name = theme.view_form_entry_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# **************************** View form entry success ************************
# *****************************************************************************

def form_entry_submitted(request, form_entry_slug=None, template_name=None):
    """
    Form entry submitted.

    :param django.http.HttpRequest request:
    :param string form_entry_slug:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        form_entry = FormEntry._default_manager.get(slug=form_entry_slug,
                                                    user__pk=request.user.pk)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    context = {
        'form_entry_slug': form_entry_slug,
        'form_entry': form_entry
    }

    if not template_name:
        theme = get_theme(request=request, as_instance=True)
        template_name = theme.form_entry_submitted_template

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

# *****************************************************************************
# *****************************************************************************
# ********************************* Delete form entry *************************
# *****************************************************************************
# *****************************************************************************

delete_form_entry_permissions = [
    'fobi.delete_formentry', 'fobi.delete_formelemententry',
    'fobi.delete_formhandlerentry',
]

@login_required
@permissions_required(satisfy=SATISFY_ALL, perms=delete_form_entry_permissions)
def delete_form_entry(request, form_entry_id, template_name=None):
    """
    Delete form entry.

    #TODO - permissions

    :param django.http.HttpRequest request:
    :param int form_entry_id:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    try:
        obj = FormEntry._default_manager \
                       .get(pk=form_entry_id, user__pk=request.user.pk)
    except ObjectDoesNotExist as e:
        raise Http404(ugettext("Form entry not found."))

    obj.delete()

    messages.info(
        request,
        _('The form "{0}" was deleted successfully.').format(obj.name)
        )

    return redirect('fobi.dashboard')
