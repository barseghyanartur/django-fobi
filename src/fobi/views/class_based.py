# -*- coding: UTF-8 -*-
"""
Class based views.
"""
import datetime
import logging

from collections import OrderedDict

import simplejson as json

# from six import string_types

from django.db import models, IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import ValidationError
from django.http import Http404, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import View, RedirectView, TemplateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import FormMixin, DeleteView, UpdateView, ProcessFormView


from nine import versions

from ..base import (
    fire_form_callbacks,
    run_form_handlers,
    run_form_wizard_handlers,
    form_element_plugin_registry,
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
    submit_plugin_form_data,
    get_theme,
)
from ..constants import (
    CALLBACK_BEFORE_FORM_VALIDATION,
    CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
    CALLBACK_FORM_VALID,
    CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
    CALLBACK_FORM_INVALID,
)
from ..decorators import permissions_required, SATISFY_ALL, SATISFY_ANY
from ..dynamic import assemble_form_class
from ..form_importers import (
    ensure_autodiscover as ensure_importers_autodiscover,
    form_importer_plugin_registry, get_form_importer_plugin_urls,
) 
from ..forms import (
    FormEntryForm,
    FormElementEntryFormSet,
    ImportFormEntryForm,
    ImportFormWizardEntryForm,
    FormWizardEntryForm,
    FormWizardFormEntry,
    FormWizardFormEntryFormSet,
    FormWizardFormEntryForm,
)
from ..helpers import JSONDataExporter
from ..models import (
    FormEntry,
    FormElementEntry,
    FormHandlerEntry,
    FormWizardEntry,
    FormWizardFormEntry,
    FormWizardHandlerEntry,
)
from ..settings import (
    GET_PARAM_INITIAL_DATA,
    DEBUG,
    SORT_PLUGINS_BY_VALUE,
)
from ..utils import (
    append_edit_and_delete_links_to_field,
    get_user_form_element_plugins_grouped,
    get_user_form_field_plugin_uids,
    get_user_form_element_plugins,
    get_user_form_handler_plugins_grouped,
    get_user_form_handler_plugins,
    get_user_form_wizard_handler_plugins,
    get_user_form_handler_plugin_uids,
    get_user_form_wizard_handler_plugin_uids,
    get_wizard_files_upload_dir,
    # perform_form_entry_import,
    # prepare_form_entry_export_data,
)
from ..wizard import (
    # DynamicCookieWizardView,
    DynamicSessionWizardView,
)

if versions.DJANGO_GTE_1_10:
    from django.shortcuts import render, redirect
    from django.urls import reverse, reverse_lazy
else:
    from django.core.urlresolvers import reverse, reverse_lazy
    from django.shortcuts import render_to_response, redirect
    from django.template import RequestContext

if versions.DJANGO_GTE_1_8:
    from formtools.wizard.forms import ManagementForm
else:
    from django.contrib.formtools.wizard.forms import ManagementForm

__title__ = 'fobi.views.class_based'
__author__ = 'Kyle Roux <jstacoder@gmail.com>'
__copyright__ = '2018 Kyle Roux'
__license__ = 'GPL 2.0/LGPL 2.1'


__all__ = (
    'AddFormElementEntryView',
    'AddFormWizardFormEntryView',
    'CreateFormWizardEntryView',
    'CreateFormEntryView',
    'DeletePluginMixin',
    'DeleteFormElementEntryView',
    'EditFormWizardEntryView',
    'EditFormEntryView',
    'EditFormElementEntryView',
    'FormWizardView',
    'FobiThemeMixin',
    'FobiFormRedirectMixin',
    'FobiThemeRedirectMixin',
    'FobiFormsetMixin',
    'FobiFormsetOrderingMixin',    
    'FormWizardDashboardView',
    'FormDashboardView',    
)

class FormEntryMixin(object):
    """ mixin class to grab the form_entry from kwargs """
    form_entry = None
    form_entry_class = FormEntry
    form_entry_kwarg = 'form_entry_id'
    form_entry_query_arg = 'pk'

    def get_form_entry_kwarg(self):
        return self.form_entry_kwarg

    def get_form_entry_query_arg(self):
        return self.form_entry_query_arg

    def get_form_entry_class(self):
        return self.form_entry_class

    def get_query_kwargs(self):
        return {
            self.get_form_entry_query_arg() : 
            self.kwargs.get(
                self.get_form_entry_kwarg()
            )
        }

    def dispatch(self, request, *args, **kwargs):
        try:
            self.form_entry = self.get_form_entry_class()._default_manager.get(**
                self.get_query_kwargs()
            )

        except ObjectDoesNotExist as err:
            raise Http404(ugettext("Form Entry Not Found"))
        return super(FormEntryMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['form_entry'] = self.form_entry
        return super(FormEntryMixin, self).get_context_data(**kwargs)

class DeletePluginMixin(object):
    entry_model_cls = None
    get_user_plugin_uids_func = None
    message = None
    html_anchor = None
    entry_model_id = 'entry_id'
    form_entry_id = None

    def get_entry_id(self):
        return self.kwargs.get(self.get_entry_model_id())

    def get_entry_model_id(self):
        return self.entry_model_id

    def get_entry_model_cls(self):
        return self.entry_model_cls

    def get_entry_model(self):
        try:
            return self.get_entry_model_cls() \
                             ._default_manager \
                             .select_related('form_entry') \
                             .get(
                                 pk=self.get_entry_id(), 
                                 form_entry__user__pk=self.request.user.pk
                            )
        except ObjectDoesNotExist as err:
            raise Http404(
                ugettext(
                    "{0} not found."
                ).format(self.get_entry_model_cls()._meta.verbose_name)
            )
    
    def get_form_entry(self):
        return self.get_entry_model().form_entry

    def get_plugin(self):
        plugin = self.get_entry_model().get_plugin(request=self.request)
        plugin.request = self.request
        return plugin

    def get_message(self):
        return self.message

    def get_html_anchor(self):
        return self.html_anchor

    def redirect(self):
        redirect_url = reverse(
            'fobi.edit_form_entry', kwargs={'form_entry_id': self.form_entry_id}
        )
        return redirect("{0}{1}".format(redirect_url, self.get_html_anchor()))

    def dispatch(self, *args, **kwargs):
        obj = self.get_entry_model()
        self.form_entry_id = obj.form_entry.id
        plugin = self.get_plugin()

        plugin._delete_plugin_data()
        obj.delete()
        messages.info(self.request, self.get_message().format(plugin.name))
        return self.redirect()

class FobiModelPropertyMixin(object):
    model = None
    model_property_name = None
    model_request_kwarg = None
    model_missing_message = None

    def get_model_missing_message(self):
        return self.model_missing_message

    def get_model(self):
        return self.model

    def get_model_property_name(self):
        return self.model_property_name

    def get_model_request_kwarg(self):
        return self.model_request_kwarg

    @classmethod
    def _inject_property(cls, obj):
        def tmp(self):
            try:
                return self.get_model().objects.get(
                    pk=self.kwargs.get(self.get_model_request_kwarg()),
                    user=self.request.user,
                )
            except ObjectDoesNotExist as err:
                raise Http404(ugettext(self.get_model_missing_message()))
        prop_name = obj.get_model_property_name()
        setattr(obj.__class__, prop_name, property(tmp))

    def __new__(cls):
        obj = super(FobiModelPropertyMixin, cls).__new__(cls)
        if not hasattr(obj, obj.get_model_property_name()):
            cls._inject_property(obj)
        return obj

class FormWizardPropertyMixin(FobiModelPropertyMixin):
    model = FormWizardEntry
    model_property_name = 'form_wizard_entry'
    model_request_kwarg = 'form_wizard_entry_id'
    model_missing_message = 'Form Wizard Entry Not Found'

class FormEntryPropertyMixin(FobiModelPropertyMixin):
    model = FormEntry
    model_property_name = 'form_entry'
    model_request_kwarg = 'form_entry_id'
    model_missing_message = 'Form Entry Not Found'

class FobiThemeMixin(TemplateView):
    theme = None
    theme_template_name = None

    def get_context_data(self, **kwargs):
        context = super(FobiThemeMixin, self).get_context_data(**kwargs)
        if 'fobi_theme' not in context:
            self.get_theme(self.request)
            context['fobi_theme'] = self.theme
        return context

    def get_theme_template_name(self):
        return self.theme_template_name

    def get_theme(self, request=None, theme=None):
        if request is None:
            request = self.request
        if theme is None:
            theme = get_theme(request=request, as_instance=True)
        self.theme = theme
        return self.theme

    def get_template_names(self):
        if self.theme is None:
            self.get_theme()
        if self.template_name is None:
            self.template_name = getattr(
                self.theme, self.get_theme_template_name())
        return [self.template_name]

class FobiFormRedirectMixin(FormMixin):    
    object = None    
    form_valid_redirect = None
    form_valid_redirect_kwargs = None
    success_message = None
    error_message = None
    success_url = None    

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        return super(FobiFormRedirectMixin, self).post(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.get_theme(request=request)
        return super(FobiFormRedirectMixin, self).dispatch(request, *args, **kwargs)

    def get_success_message(self):
        return self.success_message

    def get_error_message(self, e):
        return self.error_message

    def get_form_valid_redirect(self, *args, **kwargs):
        return self.form_valid_redirect

    def _get_form_valid_redirect_kwargs(self, *args, **kwargs):
        return self.form_valid_redirect_kwargs

    def get_form_valid_redirect_kwargs(self, result=None,  *args, **kwargs):
        form_valid_redirect_kwargs = dict()
        for key, value_key in self._get_form_valid_redirect_kwargs():
            form_valid_redirect_kwargs.update(
                {
                    key: getattr(
                        result,
                        value_key
                    )
                }
            )
        return form_valid_redirect_kwargs

    def get_success_url(self, *args, **kwargs):
        reverse_kwargs = self.get_form_valid_redirect_kwargs(
            result=self.object)
        return reverse_lazy(
            self.get_form_valid_redirect(),
            kwargs=reverse_kwargs
        )

    def _save_object(self, form=None):
        self.object.save()

    def get_object(self,  queryset=None):        
        form = self.get_form()
        if getattr(self, 'object', None) is None and hasattr(form, 'save'):
            self.object = form.save(commit=False)
            self.object.user = self.request.user            
            return self.object
        return super(FobiFormRedirectMixin, self).get_object(queryset=queryset)

    def form_valid(self, form=None):
        self.get_object()
        try:
            self._save_object(form=form)
            messages.info(
                self.request,
                ugettext(
                    self.get_success_message()
                )
            )
            return redirect(self.get_success_url())
        except IntegrityError as e:
            messages.info(
                self.request,
                ugettext(
                    self.get_error_message(e)
                )
            )
            return super(FobiFormRedirectMixin, self).form_invalid(form)

class FobiThemeRedirectMixin(FobiThemeMixin, FobiFormRedirectMixin):
    def get_form_valid_redirect(self, *args, **kwargs):
        self.get_theme()
        return getattr(self.theme, super(FobiThemeRedirectMixin, self).get_form_valid_redirect(*args, **kwargs))
        
class FobiFormsetMixin(object):
    context_formset_name = None
    object_formset_name = None
    formset_class = None
    property_formset_name = None
    formset_success_message = None
    formset_error_message = None    
    
    def get_formset_error_message(self, err):
        return self.formset_error_message
    
    def get_formset_success_message(self):
        return self.formset_success_message
    
    def get_property_formset_name(self):
        return self.property_formset_name

    def get_formset_class(self):
        return self.formset_class    
    
    def get_object_formset_name(self):
        return self.object_formset_name

    def get_context_formset_name(self):
        return self.context_formset_name

    def get_formset_queryset(self):
        return  getattr(self.get_object(), self.get_object_formset_name()).all()
    
    @classmethod
    def _provide_formset(cls, obj):
        tmp = lambda self, *args, **kwargs: \
            self.get_formset_class()(
                *(
                    [] if self.request.method.lower() == 'get' 
                    else [self.request.POST, self.request.FILES]
                ),
                **dict(
                    queryset=self.get_formset_queryset()
                )
            ) if 'ordering' in self.request.POST else self.get_formset_class()
        prop_name = obj.get_property_formset_name()
        setattr(obj.__class__, prop_name, property(tmp))        
    
    def __new__(cls):
        obj = super(FobiFormsetMixin, cls).__new__(cls)
        if not hasattr(obj, obj.get_property_formset_name()):
            cls._provide_formset(obj)
        return obj        
    
    def get_context_data(self, *args, **kwargs):
        context = super(FobiFormsetMixin, self).get_context_data(*args, **kwargs)
        context[self.get_context_formset_name()] = getattr(self, self.get_property_formset_name())
        return context

    def process_formset(self, formset=None):        
        formset = getattr(self, self.get_property_formset_name()) if formset is None else formset
        try:
            if formset.is_valid():
                formset.save()
                messages.info(
                    self.request,
                    _(self.get_formset_success_message())
                )                    
        except MultiValueDictKeyError as err:
            messages.error(
                self.request,
                _(self.get_formset_error_message(err))
            )
        return redirect(self.get_success_url())        
    
class FobiFormsetOrderingMixin(FobiFormsetMixin):
    def post(self, *args, **kwargs):        
        if 'ordering' in self.request.POST:
            return super(FobiFormsetOrderingMixin, self).process_formset()           
        form = self.get_form_class()(**self.get_form_kwargs())
        if form.is_valid():
            return super(FobiFormsetOrderingMixin, self).form_valid(form=form)
        return super(FobiFormsetOrderingMixin, self).form_invalid(form=form)


class PageTitleMixin(object):
    """ mixin to provide page title """
    page_title = None

    def get_page_title(self, **kwargs):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super(PageTitleMixin, self).get_context_data(**kwargs)
        if 'page_title' not in context:
            context['page_title'] = self.get_page_title(**context)
        return context

class ViewFormEntryView(FormEntryMixin,FobiThemeRedirectMixin,ProcessFormView):
    form_entry_kwarg = 'form_entry_slug'
    form_entry_query_arg = 'slug'
    form_valid_redirect = 'fobi.form_entry_submitted'
    theme_template_name = 'view_form_entry_template'

    def get_query_kwargs(self):
        kwargs = super(ViewFormEntryView, self).get_query_kwargs()
        if not self.request.user.is_authenticated:
            kwargs['is_public'] = True
        return kwargs        
    
    def get_form_valid_redirect_kwargs(self):
        return {'form_entry_slug': self.form_entry.slug}

    def get_theme_template_name(self):
        if not self.form_entry.is_active:
            return self.theme.form_entry_inactive_template
        return super(ViewFormEntryView, self).get_theme_template_name()

    def get_form(self, **kwargs):
        form = super(ViewFormEntryView, self).get_form(**kwargs)
        if DEBUG:
            try:
                form.as_p()
            except Exception as err:
                logger.error(err)
        return form

    def dispatch(self, request,  *args, **kwargs):
        response = super(ViewFormEntryView, self).dispatch(request, *args, **kwargs)
        self.theme.collect_plugin_media(self.form_entry.formelemententry_set.all()[:])
        return response

    def get_form_class(self):
        return assemble_form_class(
            self.form_entry,
            form_element_entries=self.form_entry.formelemententry_set.all()[:],
            request=self.request,
        )

    def get_context_data(self, **kwargs):
        kwargs = super(ViewFormEntryView, self).get_context_data(**kwargs)
        kwargs['form_entry'] = self.form_entry
        if not self.form_entry.is_active:
            kwargs.update({
                'page_header':  (self.form_entry.inactive_page_title
                            or self.form_entry.title
                            or self.form_entry.name)
            })
        kwargs['form_element_entries'] = self.form_entry.formelemententry_set.all()[:]
        kwargs['fobi_form_title'] = self.form_entry.title
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return kwargs

    def _get_form_callback_kwargs(self, stage=None):
        kwargs =  dict(
            form_entry=self.form_entry,
            request=self.request,
            form=self.form,
        )
        if stage is not None:
            kwargs['stage'] = stage
        return kwargs

    def get_success_message(self):
        return  ugettext("Form {0} was submitted successfully.").format(self.form_entry.name)

    def initial_data_check(self):
        return GET_PARAM_INITIAL_DATA in self.request.GET

    def get_initial_data(self):
        return self.request.GET

    def get_form_kwargs(self, **kwargs):
         # Providing initial form data by feeding entire GET dictionary
        # to the form, if ``GET_PARAM_INITIAL_DATA`` is present in the
        # GET.
        kwargs = super(ViewFormEntryView, self).get_form_kwargs(**kwargs)
        if self.initial_data_check():
            kwargs['initial'] = self.get_initial_data()
        return kwargs

    def post(self, *args, **kwargs):
        form = self.form = self.get_form()
        fire_form_callbacks(
            **self._get_form_callback_kwargs(
                stage=CALLBACK_BEFORE_FORM_VALIDATION
            )
        )
        if form.is_valid():
             # Fire form valid callbacks, before handling submitted plugin
            # form data.
            form = fire_form_callbacks(
                **self._get_form_callback_kwargs(       
                    stage=CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA
                )
            )
            # fire plugin processors
            form = submit_plugin_form_data(**self._get_form_callback_kwargs())
            # fire plugin processors
            form = fire_form_callbacks(
                 **self._get_form_callback_kwargs(
                     stage=CALLBACK_FORM_VALID,
                 )                    
            )
            # Run all handlers
            handler_responses, handler_errors = run_form_handlers(
                form_entry=self.form_entry,
                request=self.request,
                form=form,
                form_element_entries=self.get_context_data().get('form_element_entries'),
            )
            if handler_errors:
                for handler_error in handler_errors:
                    messages.warning(
                        request,
                        ugettext("Error occurred: {0}.").format(handler_error)
                    )

        else:
            fire_form_callbacks(
                **self._get_form_callback_kwargs(
                    stage=CALLBACK_FORM_INVALID
                )
            )
        return super(ViewFormEntryView, self).post(*args, **kwargs)
        
 

class FormWizardView(DynamicSessionWizardView):
    """Dynamic form wizard."""

    file_storage = FileSystemStorage(
        location=get_wizard_files_upload_dir()
    )

    def get_context_data(self, form, **kwargs):
        """Get context data."""
        context_data = super(FormWizardView, self).get_context_data(
            form=form, **kwargs
        )
        form_entry = self.get_form_entry_for_step(self.steps.step0)
        context_data.update({
            'form_wizard_entry': self.form_wizard_entry,
            'form_wizard_mode': True,
            'fobi_theme': self.fobi_theme,
            'fobi_form_title': form_entry.title,
            'fobi_form_wizard_title': self.form_wizard_entry.title,
            'steps_range': range(1, self.steps.count + 1),
        })

        return context_data

    def get_form_entry_for_step(self, step):
        """Get form entry title for step."""
        form_slug = self.form_list[self.steps.step0][0]
        return self.form_entry_mapping[form_slug]

    def get_initial_wizard_data(self, request, *args, **kwargs):
        """Get initial wizard data."""
        if versions.DJANGO_GTE_1_10:
            user_is_authenticated = request.user.is_authenticated
        else:
            user_is_authenticated = request.user.is_authenticated()
        try:
            qs_kwargs = {'slug': kwargs.get('form_wizard_entry_slug')}
            if not user_is_authenticated:
                qs_kwargs.update({'is_public': True})
            form_wizard_entry = FormWizardEntry.objects \
                .select_related('user') \
                .get(**qs_kwargs)
        except ObjectDoesNotExist as err:
            raise Http404(ugettext("Form wizard entry not found."))

        form_entries = [
            form_wizard_form_entry.form_entry
            for form_wizard_form_entry
            in form_wizard_entry.formwizardformentry_set
                                .all()
                                .select_related('form_entry')
        ]
        form_list = []
        form_entry_mapping = {}
        form_element_entry_mapping = {}
        wizard_form_element_entries = []
        for creation_counter, form_entry in enumerate(form_entries):
            # Using frozen queryset to minimize query usage
            form_element_entries = form_entry.formelemententry_set.all()[:]
            wizard_form_element_entries += form_element_entries
            form_cls = assemble_form_class(
                form_entry,
                request=request,
                form_element_entries=form_element_entries,
                get_form_field_instances_kwargs={
                    'form_wizard_entry': form_wizard_entry,
                }
            )

            form_list.append(
                (form_entry.slug, form_cls)
            )
            form_entry_mapping[form_entry.slug] = form_entry
            form_element_entry_mapping[form_entry.slug] = form_element_entries

        if len(form_list) == 0:
            raise Http404(
                ugettext("Form wizard entry does not contain any forms.")
            )

        theme = get_theme(request=request, as_instance=True)
        theme.collect_plugin_media(wizard_form_element_entries)

        return {
            'form_list': form_list,
            'template_name': theme.view_form_wizard_entry_template,
            'form_wizard_entry': form_wizard_entry,
            'wizard_form_element_entries': wizard_form_element_entries,
            'form_entry_mapping': form_entry_mapping,
            'form_element_entry_mapping': form_element_entry_mapping,
            'fobi_theme': theme,
        }

    def post(self, *args, **kwargs):
        """POST requests.

        This method handles POST requests.

        The wizard will render either the current step (if form validation
        wasn't successful), the next step (if the current step was stored
        successful) or the done view (if no more steps are available)
        """
        # Without this fix POST actions breaks on Django 1.11. Introduce
        # a better fix if you can.
        if versions.DJANGO_GTE_1_11:
            self.request.POST._mutable = True

        # Look for a wizard_goto_step element in the posted data which
        # contains a valid step name. If one was found, render the requested
        # form. (This makes stepping back a lot easier).
        wizard_goto_step = self.request.POST.get('wizard_goto_step', None)
        if wizard_goto_step and wizard_goto_step in self.get_form_list():
            return self.render_goto_step(wizard_goto_step)

        # Check if form was refreshed
        management_form = ManagementForm(self.request.POST, prefix=self.prefix)
        if not management_form.is_valid():
            raise ValidationError(
                _('ManagementForm data is missing or has been tampered.'),
                code='missing_management_form',
            )

        form_current_step = management_form.cleaned_data['current_step']
        if (form_current_step != self.steps.current and
                self.storage.current_step is not None):
            # form refreshed, change current step
            self.storage.current_step = form_current_step

        # get the form for the current step
        form = self.get_form(data=self.request.POST, files=self.request.FILES)

        # and try to validate
        if form.is_valid():
            # Get current form entry
            form_entry = self.form_entry_mapping[self.steps.current]
            # Get form elements for the current form entry
            form_element_entries = \
                self.form_element_entry_mapping[self.steps.current]
            # Fire plugin processors
            form = submit_plugin_form_data(
                form_entry=form_entry,
                request=self.request,
                form=form,
                form_element_entries=form_element_entries,
                **{'form_wizard_entry': self.form_wizard_entry}
            )
            # Form wizards make use of form.data instead of form.cleaned_data.
            # Therefore, we update the form.data with values from
            # form.cleaned_data.
            wizard_field_pattern = "{0}-{1}"
            # We can't update values of a `MultiValueDict`, which `QueryDict`
            # is, using `update` method. That's why we do it one by one.
            for field_key, field_value in form.cleaned_data.items():
                wizard_form_key = wizard_field_pattern.format(
                    self.steps.current,
                    field_key
                )
                # Do not overwrite field data. Only empty or missing values.
                if not (
                    wizard_form_key in form.data
                    and form.data[wizard_form_key]
                ):
                    form.data[wizard_form_key] = field_value

                # This is dirty hack to make wizard validate empty multiple
                # choice fields. Otherwise it would fail with message
                # Select a valid choice. [] is not one of the available
                # choices.
                if wizard_form_key in form.data:
                    if not form.data[wizard_form_key]:
                        if isinstance(form.data[wizard_form_key], list):
                            del form.data[wizard_form_key]

            # if the form is valid, store the cleaned data and files.
            self.storage.set_step_data(self.steps.current,
                                       self.process_step(form))

            self.storage.set_step_files(self.steps.current,
                                        self.process_step_files(form))

            # check if the current step is the last step
            if self.steps.current == self.steps.last:
                # no more steps, render done view
                return self.render_done(form, **kwargs)
            else:
                # proceed to the next step
                return self.render_next_step(form)
        return self.render(form)

    def get_ignorable_field_names(self, form_element_entries):
        """Get ignorable field names."""
        ignorable_field_names = []
        for form_element_entry in form_element_entries:
            plugin = form_element_entry.get_plugin()
            # If plugin doesn't have a value, we don't need to have it
            # on the last step (otherwise validation issues may arise, as
            # it happens with captcha/re-captcha).
            if not plugin.has_value:
                ignorable_field_names.append(plugin.data.name)
        return ignorable_field_names

    def render_done(self, form, **kwargs):
        """Render done.

        This method gets called when all forms passed. The method should also
        re-validate all steps to prevent manipulation. If any form fails to
        validate, `render_revalidation_failure` should get called.
        If everything is fine call `done`.
        """
        final_forms = OrderedDict()
        # walk through the form list and try to validate the data again.
        for form_key in self.get_form_list():

            form_obj = self.get_form(
                step=form_key,
                data=self.storage.get_step_data(form_key),
                files=self.storage.get_step_files(form_key)
            )

            # Get form elements for the current form entry
            form_element_entries = \
                self.form_element_entry_mapping[form_key]

            ignorable_field_names = self.get_ignorable_field_names(
                form_element_entries
            )

            for ignorable_field_name in ignorable_field_names:
                if ignorable_field_name in form_obj.fields:
                    form_obj.fields.pop(ignorable_field_name)

            if not form_obj.is_valid():
                return self.render_revalidation_failure(form_key,
                                                        form_obj,
                                                        **kwargs)

            # Fire plugin processors
            # Get current form entry
            form_entry = self.form_entry_mapping[form_key]

            form_obj = submit_plugin_form_data(
                form_entry=form_entry,
                request=self.request,
                form=form_obj,
                form_element_entries=form_element_entries,
                **{'form_wizard_entry': self.form_wizard_entry}
            )

            final_forms[form_key] = form_obj

        # render the done view and reset the wizard before returning the
        # response. This is needed to prevent from rendering done with the
        # same data twice.
        done_response = self.done(final_forms.values(),
                                  form_dict=final_forms,
                                  **kwargs)
        self.storage.reset()
        return done_response

    def done(self, form_list, **kwargs):
        """Done."""
        if versions.DJANGO_GTE_1_10:
            user_is_authenticated = self.request.user.is_authenticated
        else:
            user_is_authenticated = self.request.user.is_authenticated()
        try:
            qs_kwargs = {'slug': kwargs.get('form_wizard_entry_slug')}
            if not user_is_authenticated:
                kwargs.update({'is_public': True})
            form_wizard_entry = FormWizardEntry.objects \
                .select_related('user') \
                .get(**qs_kwargs)
        except ObjectDoesNotExist as err:
            raise Http404(ugettext("Form wizard entry not found."))

        # Run all handlers
        handler_responses, handler_errors = run_form_wizard_handlers(
            form_wizard_entry=form_wizard_entry,
            request=self.request,
            form_list=form_list,
            form_wizard=self,
            form_element_entries=self.wizard_form_element_entries
        )

        # do_something_with_the_form_data(form_list)
        redirect_url = reverse('fobi.form_wizard_entry_submitted',
                               args=[form_wizard_entry.slug])
        return HttpResponseRedirect(redirect_url)

class CreateFormWizardEntryView(FobiThemeRedirectMixin, PageTitleMixin, SingleObjectMixin):
    result = None
    page_title = 'Create form wizard entry'
    template_name = None
    model = FormWizardEntry
    form_class = FormWizardEntryForm
    context_object_name = 'form_wizard_entry'
    theme_template_name = 'create_form_wizard_entry_template'
    form_valid_redirect = 'edit_form_wizard_entry'
    form_valid_redirect_kwargs = (
        ('form_wizard_entry_id', 'pk'),
    )

    def get_success_message(self):
        return 'Form wizard {0} was created successfully.'.format(self.object.name)

    def get_error_message(self, e):
        return 'Errors occurred while saving the form wizard: {0}.'.format(str(e))

    def dispatch(self, request, theme=None, *args, **kwargs):
        self.get_theme(request)
        return super(CreateFormWizardEntryView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super(CreateFormWizardEntryView, self).form_valid()

    def get_context_data(self, **kwargs):
        context = super(CreateFormWizardEntryView,
                        self).get_context_data(**kwargs)
        if self.theme:
            context['fobi_theme'] = self.theme
        return context

    def get_form(self, form_class=None):
        form_args = [] if self.request.method == 'GET' else [
            self.request.POST, self.request.FILES
        ]
        form_kwargs = dict(request=self.request)
        if form_class is None:
            form_class = self.form_class
        return form_class(*form_args, **form_kwargs)

class EditFormWizardEntryView(FobiThemeRedirectMixin, PageTitleMixin, FobiFormsetOrderingMixin, SingleObjectMixin, View):
    form_wizard_entry_id = None
    theme = None
    page_title = 'Edit form wizard entry'
    model = FormWizardEntry
    pk_url_kwarg = 'form_wizard_entry_id'
    form_class = FormWizardEntryForm    
    form_valid_redirect = 'edit_form_wizard_entry'
    form_valid_redirect_kwargs = (
        ('form_wizard_entry_id', 'pk')
    )
    context_object_name = 'form_wizard_entry'
    theme_template_name = 'edit_form_wizard_entry_template'
    context_formset_name = 'form_wizard_form_entry_formset'
    object_formset_name = 'formwizardformentry_set'
    formset_class = FormWizardFormEntryFormSet
    property_formset_name = 'form_wizard_form_entry_formset'
    formset_success_message = 'Forms ordering edited successfully.'
    formset_error_message = 'Errors occurred while trying to change the elements ordering!'

    def get_success_message(self):
        return "Form wizard {0} was edited successfully".format(self.object.name)

    def get_error_message(self, e):
        return "Errors occurred while saving the Form wizard {0}".format(e)

    def get_context_data(self, **kwargs):
        context = super(EditFormWizardEntryView,
                        self).get_context_data(**kwargs)
        context['form_wizard_entry_forms'] = self.object.formwizardformentry_set \
            .all().select_related('form_entry') \
            .order_by('position')[:]

        context['form_wizard_handlers'] = self.object.formwizardhandlerentry_set.all()[:]
        context['used_form_wizard_handler_uids'] = [
            form_wizard_handler.plugin_uid
            for form_wizard_handler
            in context['form_wizard_handlers']
        ]
        context['form_wizard_form_entry_ids'] = [
            _f.form_entry_id
            for _f in context['form_wizard_entry_forms']
        ]
        context['all_form_entries'] = FormEntry._default_manager \
                                               .only('id', 'name', 'slug') \
                                               .filter(user__pk=self.request.user.pk) \
                                               .exclude(id__in=context['form_wizard_form_entry_ids'])

        context['user_form_wizard_handler_plugins'] = get_user_form_wizard_handler_plugins(
            self.request.user,
            exclude_used_singles=True,
            used_form_wizard_handler_plugin_uids=context['used_form_wizard_handler_uids'],
        )        
        return context

    def dispatch(self, request, *args, **kwargs):
        self.form_wizard_entry_id = kwargs.pop('form_wizard_entry_id', None)
        self.object = self.get_object()
        return super(EditFormWizardEntryView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def get_queryset(self):
        return self.model._default_manager \
                         .select_related('user') \
                         .prefetch_related('formwizardformentry_set')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(pk=self.form_wizard_entry_id, user__pk=self.request.user.pk)
        except self.model.ObjectDoesNotExist as err:
            raise Http404(ugettext('not found'))

    def get_form_kwargs(self):
        kwargs = super(EditFormWizardEntryView, self).get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        if 'request' not in kwargs:
            kwargs.update({'request': self.request})
        return kwargs

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        form_args = []
        if self.request.method == 'POST':
            form_args = [self.request.POST, self.request.FILES]
        return form_class(*form_args, **self.get_form_kwargs())

class FormWizardDashboardView(MultipleObjectMixin, FobiThemeMixin, TemplateView):
    theme = None
    model = FormWizardEntry
    theme_template_name = 'form_wizards_dashboard_template'
    context_object_name = 'form_wizard_entries'

    def get_queryset(self):
        return super(FormWizardDashboardView, self).get_queryset().filter(
            user__pk=self.request.user.pk,
        ).select_related('user')

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super(FormWizardDashboardView, self).get_context_data(**kwargs)
        context['form_wizard_entries'] = self.get_queryset()
        return context

class FormDashboardView(MultipleObjectMixin, FobiThemeMixin, TemplateView):
    theme = None
    model = FormEntry
    theme_template_name = 'dashboard_template'
    context_object_name = 'form_entries'

    def get_queryset(self):
        return super(FormDashboardView, self).get_queryset().filter(
            user__pk=self.request.user.pk
        ).select_related('user')

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super(FormDashboardView, self).get_context_data(**kwargs)
        context[self.context_object_name] = self.object_list[:]
        context['form_importers'] = get_form_importer_plugin_urls()
        return context

class CreateFormEntryView(FobiThemeRedirectMixin, PageTitleMixin, View):
    template_name = None
    model = FormEntry
    page_title = 'Create Form'
    form_class = FormEntryForm
    theme_template_name = 'create_form_entry_template'
    form_valid_redirect = 'edit_form_entry'
    form_valid_redirect_kwargs = (
        ('form_entry_id', 'pk'),
    )

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.get_form()
        return super(CreateFormEntryView, self).get_context_data(**kwargs)

    def get_success_message(self):
        return 'Form {0} was created successfully.'.format(self.object.name)

    def get_error_message(self, e):
        return 'Errors occurred while saving the form: {0}.'.format(str(e))

    def dispatch(self, request, *args, **kwargs):
        self.get_theme(request)
        return super(CreateFormEntryView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super(CreateFormEntryView, self).form_valid()

    def get_form(self, form_class=None):
        form_args = [] if self.request.method == 'GET' else [
            self.request.POST, self.request.FILES]
        form_kwargs = dict(request=self.request)
        if form_class is None:
            form_class = self.form_class
        return form_class(*form_args, **form_kwargs)

class EditFormEntryView(FobiThemeRedirectMixin, PageTitleMixin, FobiFormsetOrderingMixin, SingleObjectMixin, View):
    form_entry_id = None
    theme = None
    model = FormEntry
    page_title = 'Edit form entry'
    pk_url_kwarg = 'form_entry_id'
    form_class = FormEntryForm
    context_formset_name = 'form_element_entry_formset'
    property_formset_name = 'form_element_entry_formset'
    formset_success_message = 'Forms ordering edited successfully.'
    formset_error_message = 'Errors occurred while trying to change the elements ordering!'
    formset_class = FormElementEntryFormSet
    object_formset_name = 'formelemententry_set'    
    form_valid_redirect = 'edit_form_entry'
    form_valid_redirect_kwargs = (
        ('form_entry_id', 'pk'),
    )
    context_object_name = 'form_entry'
    theme_template_name = 'edit_form_entry_template'

    def get_success_message(self):
        return "Form {0} was edited successfully".format(self.object.name)

    def get_error_message(self, e):
        return "Errors occurred while saving the Form: {0}".format(e)

    def get_context_data(self, **kwargs):
        context = super(EditFormEntryView, self).get_context_data(**kwargs)
        context['form_elements'] = self.object.formelemententry_set.all()
        context['form_handlers'] = self.object.formhandlerentry_set.all()[:]

        context['used_form_handler_uids'] = [
            form_handler.plugin_uid
            for form_handler
            in context['form_handlers']
        ]
        # The code below (two lines below) is not really used at the moment,
        # thus - comment out, but do not remove, as we might need it later on.
        # context['all_form_entries'] = self.model._default_manager \
        #                            .only('id', 'name', 'slug') \
        #                            .filter(user__pk=self.request.user.pk)

        context['user_form_element_plugins'] = get_user_form_element_plugins_grouped(
            self.request.user,
            sort_by_value=SORT_PLUGINS_BY_VALUE,
        )

        context['user_form_handler_plugins'] = get_user_form_handler_plugins(
            self.request.user,
            exclude_used_singles=True,
            used_form_handler_plugin_uids=context['used_form_handler_uids'],
        )
        form_cls = assemble_form_class(
            self.object,
            origin='edit_form_entry',
            origin_kwargs_update_func=append_edit_and_delete_links_to_field,
            request=self.request,
        )
        context['assembled_form'] = form_cls()
        if DEBUG:
            context['assembled_form'].as_p()
        else:
            try:
                context['assembled_form'].as_p()
            except Exception as err:
                logger.error(err)
        context['fobi_theme'].collect_plugin_media(context['form_elements'])        
        return context

    def dispatch(self, request, *args, **kwargs):
        self.form_entry_id = kwargs.pop('form_entry_id', None)
        self.object = self.get_object()
        return super(EditFormEntryView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def get_queryset(self):
        return self.model._default_manager \
            .select_related('user') \
            .prefetch_related('formelemententry_set')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(pk=self.form_entry_id, user__pk=self.request.user.pk)
        except self.model.DoesNotExist as err:
            raise Http404(ugettext('{0} not found'.format(self.model.__name__)))

    def get_form_kwargs(self):
        kwargs = super(EditFormEntryView, self).get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        if 'request' not in kwargs:
            kwargs.update({'request': self.request})
        return kwargs

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        form_args = []
        if self.request.method == 'POST':
            form_args = [self.request.POST, self.request.FILES]
        return form_class(*form_args, **self.get_form_kwargs())

class AddFormElementEntryView(FobiThemeRedirectMixin, SingleObjectMixin, RedirectView):
    obj = None
    form_element_plugin = None
    form_element_entry_class = FormElementEntry
    save_object = False
    form_element_plugin_form_cls = None
    pk_url_kwarg = 'form_entry_id'
    model = FormEntry
    form_class = None
    theme_template_name = 'add_form_element_entry_template'
    context_object_name = 'form_entry'
    form_valid_redirect = 'edit_form_entry'
    form_valid_redirect_kwargs = (
        ('form_entry_id', 'pk'),
    )

    def get_success_url(self, *args, **kwargs):
        return "{0}?active_tab=tab-form-elements".format(
            super(AddFormElementEntryView, self).get_success_url(*args, **kwargs)
        )

    def get_queryset(self):
        return super(AddFormElementEntryView, self).get_queryset() \
                                               .prefetch_related('formelemententry_set')

    def _save_object(self, form=None):
        form.save_plugin_data(request=self.request)
        self.obj.plugin_data = form.get_plugin_data(request=self.request)
        self.save_object = True
        self.obj.save()

    def get_context_data(self, **kwargs):
        context = super(AddFormElementEntryView, self).get_context_data(**kwargs)
        self.object = self.get_object()
        context['form_elements'] = self.object.formelemententry_set.all()
        user_form_element_plugin_uids = get_user_form_field_plugin_uids(
            self.request.user
        )
        if self.kwargs.get('form_element_plugin_uid') not in user_form_element_plugin_uids:
            raise Http404(
                ugettext('plugin does not exist or you are not allowed to use this plugin.'))
        form_element_plugin_cls = form_element_plugin_registry.get(
            self.kwargs.get('form_element_plugin_uid')
        )
        self.form_element_plugin = \
            context['form_element_plugin'] = \
            form_element_plugin_cls(user=self.request.user)

        context['form_element_plugin'].request = self.request
        if 'form' not in context:
            form_kwargs = {} if self.request.method.lower() == 'get' else dict(data=self.request.POST,
                                                                               files=self.request.FILES)
            kwargs['form'] = self.get_form()
            context['form'] = self.form = kwargs['form']
        return context

    def get_form_kwargs(self):
        if self.request.method.lower() == 'post':
            return dict(data=self.request.POST, files=self.request.FILES)
        return {}

    def get_form(self):
        form_element_plugin_cls = form_element_plugin_registry.get(
            self.kwargs.get('form_element_plugin_uid')
        )
        self.form_element_plugin = \
            form_element_plugin_cls(user=self.request.user)
        self.form_element_plugin.request = self.request
        return self.form_element_plugin.get_initialised_create_form_or_404(**self.get_form_kwargs())

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object(self.get_queryset())
        self.context = self.get_context_data(
            form_element_plugin=self.form_element_plugin)
        self.form_element_plugin_form_cls = self.form_element_plugin.get_form()
        self.obj = FormElementEntry()
        self.obj.form_entry = self.object
        self.obj.plugin_uid = self.kwargs.get('form_element_plugin_uid')
        self.obj.user = request.user

        if not self.form_element_plugin_form_cls:
            self.save_object = True
        res = super(AddFormElementEntryView, self).dispatch(
            request, *args, **kwargs
        )
        if self.save_object:
            position = 1
            records = FormElementEntry._default_manager.filter(form_entry=self.object) \
                                                  .aggregate(models.Max('position'))
            if records:
                try:
                    position = records['{0}__max'.format('position')] + 1
                except TypeError as err:
                    pass

            self.obj.position = position
            # save the object
            self.obj.save()

            messages.info(
                self.request,
                self.get_success_message()
            )
        return res

    def get_success_message(self):
        return ugettext('The form element plugin "{0}" was added successfully') \
            .format(self.form_element_plugin.name)

    def post(self, request, *args, **kwargs):
        context = self.context
        form = self.get_form()
        form.validate_plugin_data(
            context['form_elements'], request=self.request)
        if form.is_valid():
            form.save_plugin_data(request=self.request)
            self.obj.plugin_data = form.get_plugin_data(request=self.request)
            self.save_object = True
            return super(AddFormElementEntryView, self).form_valid(form=form)
        return super(AddFormElementEntryView, self).form_invalid(form=form)

class EditFormElementEntryView(FobiThemeRedirectMixin, UpdateView):
    form_valid_redirect = 'edit_form_entry'
    form_valid_redirect_kwargs = (
        ('form_entry_id', 'pk'),
    )
    form_element_entry = None
    model = FormEntry
    context_object_name = 'form_entry'
    theme_template_name = 'edit_form_element_entry_template'
    success_message = 'The form element plugin "{0}" was edited successfully.'

    def get_queryset(self):    
        return FormElementEntry._default_manager \
            .select_related('form_entry', 'form_entry__user')    

    def get_object(self):
        qs = self.get_queryset()
        try:
            self.form_element_entry = qs.get(
                pk=self.kwargs.get('form_element_entry_id'),
                form_entry__user__pk=self.request.user.pk
            )
        except ObjectDoesNotExist as err:
            raise Http404(ugettext("Form element entry not found."))
        return self.form_element_entry.form_entry

    def get_context_data(self, **kwargs):
        context = super(EditFormElementEntryView, self).get_context_data(**kwargs)
        ctx_obj_name = self.get_context_object_name()
        if ctx_obj_name not in context:
            context[self.get_context_object_name()] = self.get_object()
            context['form_element_entry'] = self.form_element_entry
            form_element_plugin = self.form_element_entry.get_plugin(request=self.request)
            form_element_plugin.request = self.request
            form_element_plugin_form = form_element_plugin.get_form()
            context['form'] = None
            context['form_element_plugin_form'] = form_element_plugin_form
            context['form_element_plugin'] = form_element_plugin
            if not form_element_plugin_form:
                messages.info(
                    self.request,
                    ugettext('The Form Element Plugin"{0}" is not configurable!'.format(form_element_plugin.name))
                )
                return redirect(self.get_success_url())
            context['form'] = self.get_form(context)
        return context
    
    def get_form(self, context=None, **kwargs):
        if self.request.method.lower() == 'post':
            kwargs.update(dict(files=self.request.FILES, data=self.request.POST))
        return context.get('form_element_plugin').get_initialised_create_form_or_404(**kwargs)
        
    def get_form_elements(self):
        return self.get_queryset() \
            .exclude(
                pk=self.kwargs.get(
                    'form_element_entry_id'
                )
            ).filter(form_entry=self.get_object())

    def get_success_message(self):
        return super(EditFormElementEntryView, self) \
                    .get_success_message() \
                    .format(self.get_context_data().get('form_element_plugin').name)

    def _save_object(self, form=None):
        form.save_plugin_data(request=self.request)
        # get the plugin data
        self.form_element_entry.plugin_data = form.get_plugin_data(request=self.request)
        # save the object
        self.form_element_entry.save()
    
    def post(self, *args, **kwargs):
        context = self.get_context_data()
        form = context['form']
        form.validate_plugin_data(self.get_form_elements(), request=self.request)
        if form.is_valid():                       
            return super(EditFormElementEntryView, self).form_valid(form=form)
        return super(EditFormElementEntryView, self).form_invalid(form=form)

class AddFormWizardFormEntryView(FobiFormRedirectMixin, FormWizardPropertyMixin, FormEntryPropertyMixin, View):
    """ Add a form entry to a form wizard """
    form_valid_redirect = 'edit_form_wizard_entry'    
    
    def get_form_valid_redirect_kwargs(self):
        return dict(form_wizard_entry_id=self.form_wizard_entry.id)

    def get_success_url(self):
        return  "{0}?active_tab=tab-form-elements".format(super(AddFormWizardFormEntry, self).get_success_url())

    def dispatch(self, request, *args, **kwargs):
        try:
            obj = FormWizardFormEntry.objects.create(
                form_wizard_entry=self.form_wizard_entry,
                form_entry=self.form_entry,
            )
        except IntegrityError as err:
            messages.error(
                request,
                ugettext(
                    'The form entry "{0}" could not be added to the '
                    'wizard "{1}" due to the following error "{2}".'
                ).format(self.form_entry.name, self.form_wizard_entry.name, str(err))
            )              
            return self.form_valid()
        # Handling the position
        position = 1
        records = FormWizardFormEntry.objects.filter(
            form_wizard_entry_id=self.kwargs.get('form_wizard_entry_id'),
            # form_entry_id=form_entry_id
        ).aggregate(models.Max('position'))
        if records:
            try:
                position = records['{0}__max'.format('position')] + 1
            except TypeError as err:
                pass
        obj.position = position
        # Save the object.
        obj.save()

        messages.info(
            request,
            ugettext(
                'The form entry "{0}" was added successfully to the wizard "{1}".'
            ).format(self.form_entry.name, self.form_wizard_entry.name)
        )
        return self.form_valid(form=None)
    
class DeleteFormElementEntryView(DeletePluginMixin, View):
    entry_model_cls = FormElementEntry
    message = ugettext('The form element plugin "{0}" was deleted successfully.')
    html_anchor = '?active_tab=tab-form-elements'

    def get_entry_id(self):
        return self.kwargs.get('form_element_entry_id')

class DeleteFormEntryView(DeleteView):
    model = FormEntry
    pk_url_kwarg = 'form_entry_id'
    success_url = reverse_lazy('fobi.dashboard')

    def get_object(self, queryset=None):
        return super(DeleteFormEntryView, self).filter(user__id=self.request.user.id).get_object(queryset)

    def post(self, *args, **kwargs):
        res = super(DeleteFormElementEntryView).post(*args, **kwargs)
        messages.info(
            request,
            ugettext('The form "{0}" was deleted successfully.').format(self.object.name)
        )


    
class AddFormHandlerEntryView(FormEntryMixin, FobiThemeRedirectMixin):
    theme = None
    model = FormHandlerEntry
    form_class = None
    form_valid_redirect = 'edit_form_entry'
    form_valid_redirect_kwargs = None
    theme_template_name = 'add_form_handler_entry_template'
    save_object = False

    def get_form(self):
        form_kwargs = {} if self.request.method.lower() == 'get' else dict(data=self.request.POST, files=self.request.FILES)
        return self._get_form_handler_plugin().get_initialised_create_form_or_404(
            **form_kwargs
        )

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.get_form()
        kwargs['form_handler_plugin'] = self._get_form_handler_plugin()
        return super(AddFormHandlerEntryView, self).get_context_data(**kwargs)
        
    def _get_form_handler_plugin_cls(self):
        return form_handler_plugin_registry.get(
            self.kwargs.get('form_handler_plugin_uid')
        )

    def _get_form_handler_plugin(self):
        plugin = self._get_form_handler_plugin_cls()(user=self.request.user)
        plugin.request = self.request
        return plugin

    def check_multiple(self):
        form_handler_plugin_cls = self._get_form_handler_plugin_cls()
        if not form_handler_plugin_cls.allow_multiple:
            times_used  = FormHandlerEntry._default_manager \
                .filter(
                    form_entry__id=self.kwargs.get('form_entry_id'),
                    plugin_uid=form_handler_plugin_cls.uid
                ).count()
            if times_used > 0:
                raise Http404(
                     ugettext("The {0} plugin can be used only once in a form.")
                    .format(form_handler_plugin_cls.name)
                )
                
    def check_allowed(self):
        user_form_handler_plugin_uids =  get_user_form_handler_plugin_uids(
            self.request.user
        )
        if self.kwargs.get('form_handler_plugin_uid') not in user_form_handler_plugin_uids:
             raise Http404(ugettext("Plugin does not exist or you are not allowed "
                                    "to use this plugin!"))
    
    def get_form_valid_redirect_kwargs(self):
        return (
            ('form_entry_id', self.kwargs.get('form_entry_id'))
        )
    def get_success_url(self):
        return "{0}?active_tab=tab-form-handlers".format(super(AddFormHandlerEntryView, self).get_success_url())

    def dispatch(self, request, *args, **kwargs):
        self.check_allowed()

        self.check_multiple()

        form_handler_plugin_form_cls = self._get_form_handler_plugin().get_form()
        obj  = FormHandlerEntry()
        obj.form_entry = self.form_entry
        obj.plugin_uid = self.kwargs.get('form_handler_plugin_uid')
        obj.user = self.request.user

        if not form_handler_plugin_form_cls:
            self.save_object = True

        form = self.get_form()
        if self.request.method.lower() == 'post':
            if form.is_valid():
                form.save_plugin_data(request=self.request)
                obj.plugin_data = form.get_plugin_data(request=self.request)

                self.save_object = True
        if self.save_object:
            obj.save()

            messages.info(
                self.request,
                ugettext("The form handler plugin '{0}' was added").format(self._get_form_handler_plugin().name)
            )
            return super(AddFormHandlerEntryView, self).form_valid()
        

