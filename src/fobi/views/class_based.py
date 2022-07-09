import datetime
import json
import logging

from django.contrib import messages
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db import IntegrityError, models
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from ..base import (
    fire_form_callbacks,
    run_form_handlers,
    run_form_wizard_handlers,
    form_element_plugin_registry,
    form_handler_plugin_registry,
    form_wizard_handler_plugin_registry,
    submit_plugin_form_data,
    get_theme,
    # get_registered_form_handler_plugins
)
from ..dynamic import assemble_form_class
from ..forms import (
    FormElementEntryFormSet,
    FormEntryForm,
    FormWizardEntryForm,
    FormWizardFormEntryFormSet,
    ImportFormEntryForm,
    ImportFormWizardEntryForm,
)
from ..models import (
    FormElementEntry,
    FormEntry,
    FormHandlerEntry,
    FormWizardEntry,
    FormWizardFormEntry,
    FormWizardHandlerEntry,
)
from ..permissions.default import (
    CreateFormEntryPermission,
    EditFormEntryPermission,
    DeleteFormEntryPermission,
    AddFormElementEntryPermission,
    EditFormElementEntryPermission,
)
from ..settings import DEBUG, GET_PARAM_INITIAL_DATA, SORT_PLUGINS_BY_VALUE
from ..utils import (
    append_edit_and_delete_links_to_field,
    get_user_form_element_plugins_grouped,
    get_user_form_field_plugin_uids,
    get_user_form_handler_plugin_uids,
    get_user_form_handler_plugins,
    get_user_form_wizard_handler_plugin_uids,
    get_user_form_wizard_handler_plugins,
    get_wizard_files_upload_dir,
    perform_form_entry_import,
    prepare_form_entry_export_data,
)

__all__ = (
    "CreateFormEntryView",
    "EditFormEntryView",
    "DeleteFormEntryView",
    "AddFormElementEntryView",
    "EditFormElementEntryView",
)

logger = logging.getLogger(__name__)


class PermissionMixin(View):
    """Mixin for permission-based views."""

    permission_classes: tuple = ()

    def permission_denied(self, request, message=None, code=None):
        """If request is not permitted, raise."""
        raise PermissionDenied()

    def get_permissions(self):
        """Return initialized list of permissions required by this view."""
        return [permission() for permission in self.permission_classes]

    def dispatch(self, request, *args, **kwargs):
        """Dispatch the request."""
        self.check_permissions(request)
        return super(PermissionMixin, self).dispatch(request, *args, **kwargs)

    def check_permissions(self, request):
        """Check if the request should be permitted.

        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )

# *****************************************************************************
# *****************************************************************************
# ********************************** Builder **********************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# **************************** Create form entry ******************************
# *****************************************************************************


class CreateFormEntryView(PermissionMixin, CreateView):
    """Create form entry."""

    template_name = None
    form_class = FormEntryForm
    theme = None
    permission_classes = (CreateFormEntryPermission,)

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super(CreateFormEntryView, self).get_context_data(**kwargs)
        context["form"] = self.get_form()
        if not self.theme:
            theme = get_theme(request=self.request, as_instance=True)
        else:
            theme = self.theme

        if theme:
            context.update({"fobi_theme": theme})
        return context

    def get_template_names(self):
        """Get template names."""
        template_name = self.template_name
        if not template_name:
            if not self.theme:
                theme = get_theme(request=self.request, as_instance=True)
            else:
                theme = self.theme
            template_name = theme.create_form_entry_template
        return [template_name]

    def get_form_kwargs(self):
        kwargs = super(CreateFormEntryView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        self.object = None
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form_entry = form.save(commit=False)
            form_entry.user = request.user
            self._run_before_form_create(request, form_entry)
            try:
                form_entry.save()
                self._run_after_form_create(request, form_entry)
                messages.info(
                    request,
                    _("Form {0} was created successfully.").format(
                        form_entry.name
                    ),
                )
                return redirect(
                    "fobi.edit_form_entry", form_entry_id=form_entry.pk
                )
            except IntegrityError as err:
                messages.info(
                    request,
                    _("Errors occurred while saving the form: {0}.").format(
                        str(err)
                    ),
                )

        return self.render_to_response(self.get_context_data())

    def _run_before_form_create(self, request, form_entry):
        """Run just before form_entry has been created/saved."""
        try:
            self.run_before_form_create(request, form_entry)
            return True
        except:
            return False

    def run_before_form_create(self, request, form_entry):
        """Run just before form_entry has been created/saved."""

    def _run_after_form_create(self, request, form_entry):
        """Run after form_entry has been created/saved."""
        try:
            self.run_after_form_create(request, form_entry)
            return True
        except:
            return False

    def run_after_form_create(self, request, form_entry):
        """Run after the form_entry has been created/saved."""

# **************************************************************************
# ******************************* Edit form entry **************************
# **************************************************************************


class EditFormEntryView(PermissionMixin, UpdateView):
    """Edit form entry."""

    template_name = None
    form_class = FormEntryForm
    theme = None
    pk_url_kwarg = "form_entry_id"
    permission_classes = (EditFormEntryPermission,)

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super(EditFormEntryView, self).get_context_data(**kwargs)

        # In case of success, we don't need this (since redirect would happen).
        # Thus, fetch only if needed.
        form_elements = self.object.formelemententry_set.all()
        form_handlers = self.object.formhandlerentry_set.all()[:]
        used_form_handler_uids = [
            form_handler.plugin_uid for form_handler in form_handlers
        ]

        # The code below (two lines below) is not really used at the moment,
        # thus - comment out, but do not remove, as we might need it later on.
        # all_form_entries = FormEntry._default_manager \
        #                            .only('id', 'name', 'slug') \
        #                            .filter(user__pk=request.user.pk)

        # List of form element plugins allowed to user
        user_form_element_plugins = get_user_form_element_plugins_grouped(
            self.request.user, sort_by_value=SORT_PLUGINS_BY_VALUE
        )
        # List of form handler plugins allowed to user
        user_form_handler_plugins = get_user_form_handler_plugins(
            self.request.user,
            exclude_used_singles=True,
            used_form_handler_plugin_uids=used_form_handler_uids,
        )

        # Assembling the form for preview
        form_cls = assemble_form_class(
            self.object,
            origin="edit_form_entry",
            origin_kwargs_update_func=append_edit_and_delete_links_to_field,
            request=self.request,
        )

        assembled_form = form_cls()

        # In debug mode, try to identify possible problems.
        if DEBUG:
            assembled_form.as_p()
        else:
            try:
                assembled_form.as_p()
            except Exception as err:
                logger.error(err)

        # If no theme provided, pick a default one.
        if not self.theme:
            theme = get_theme(request=self.request, as_instance=True)
        else:
            theme = self.theme

        if theme:
            context.update({"fobi_theme": theme})

        theme.collect_plugin_media(form_elements)

        context.update(
            {
                "form": self.get_form(),
                "form_entry": self.object,
                "form_elements": form_elements,
                "form_handlers": form_handlers,
                "user_form_element_plugins": user_form_element_plugins,
                "user_form_handler_plugins": user_form_handler_plugins,
                "assembled_form": assembled_form,
                "fobi_theme": theme,
            }
        )

        return context

    def get_template_names(self):
        """Get template names."""
        template_name = self.template_name
        if not template_name:
            if not self.theme:
                theme = get_theme(request=self.request, as_instance=True)
            else:
                theme = self.theme
            template_name = theme.edit_form_entry_template
        return [template_name]

    def get_form_kwargs(self):
        kwargs = super(EditFormEntryView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def _get_queryset(self, request):
        """Get queryset."""
        return FormEntry._default_manager \
            .select_related('user') \
            .prefetch_related('formelemententry_set') \
            .filter(user__pk=request.user.pk)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self._get_queryset(request))
        """Handle GET requests: instantiate a blank version of the form."""
        form_element_entry_formset = FormElementEntryFormSet(
            queryset=self.object.formelemententry_set.all(),
            # prefix='form_element'
        )
        return self.render_to_response(
            self.get_context_data(
                form_element_entry_formset=form_element_entry_formset,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object(queryset=self._get_queryset(request))
        form = self.get_form()

        # This is where we save ordering if it has been changed.
        # The `FormElementEntryFormSet` contain ids and positions only.
        if "ordering" in request.POST:
            form_element_entry_formset = FormElementEntryFormSet(
                request.POST,
                request.FILES,
                queryset=self.object.formelemententry_set.all(),
                # prefix = 'form_element'
            )
            # If form elements aren't properly made (developers's fault)
            # there might be problems with saving the ordering - likely
            # in case of hidden elements only. Thus, we want to avoid
            # errors here.
            try:
                if form_element_entry_formset.is_valid():
                    form_element_entry_formset.save()
                    messages.info(
                        request, _("Elements ordering edited successfully.")
                    )
                    return redirect(
                        reverse_lazy(
                            "fobi.edit_form_entry",
                            kwargs={"form_entry_id": self.object.pk},
                        )
                    )
            except MultiValueDictKeyError as err:
                messages.error(
                    request,
                    _(
                        "Errors occurred while trying to change the "
                        "elements ordering!"
                    ),
                )
                return redirect(
                    reverse_lazy(
                        "fobi.edit_form_entry",
                        kwargs={"form_entry_id": self.object.pk},
                    )
                )
        else:
            form_element_entry_formset = FormElementEntryFormSet(
                queryset=self.object.formelemententry_set.all(),
                # prefix='form_element'
            )

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            try:
                obj.save()
                messages.info(
                    request,
                    _("Form {0} was edited successfully.").format(obj.name),
                )
                return redirect(
                    reverse_lazy(
                        "fobi.edit_form_entry", kwargs={"form_entry_id": obj.pk}
                    )
                )
            except IntegrityError as err:
                messages.info(
                    request,
                    _("Errors occurred while saving the form: {0}.").format(
                        str(err)
                    ),
                )

        return self.render_to_response(
            self.get_context_data(
                form_element_entry_formset=form_element_entry_formset,
            )
        )

# *****************************************************************************
# ********************************* Delete form entry *************************
# *****************************************************************************


class DeleteFormEntryView(PermissionMixin, DeleteView):
    """Delete form entry."""

    model = FormEntry
    success_url = reverse_lazy("fobi.dashboard")
    permission_classes = (DeleteFormEntryPermission,)

    def get_object(self, queryset=None):
        """Get object."""
        return get_object_or_404(
            FormEntry._default_manager.all(),
            pk=self.kwargs.get("form_entry_id"),
            user__pk=self.request.user.pk
        )

    def delete(self, request, *args, **kwargs):
        """Delete."""
        self.object = self.get_object()
        success_url = self.get_success_url()
        self._run_before_form_delete(request, self.object)
        self.object.delete()
        self._run_after_form_delete(request, self.kwargs.get("form_entry_id"))
        messages.info(
            request,
            _("Form {0} was deleted successfully.").format(self.object.name),
        )
        return redirect(success_url)

    def _run_before_form_delete(self, request, form_entry):
        """Run just before form_entry has been delete."""
        try:
            self.run_before_form_delete(request, form_entry)
            return True
        except:
            return False

    def run_before_form_delete(self, request, form_entry):
        """Run just before form_entry has been deleted."""

    def _run_after_form_delete(self, request, form_entry_id):
        """Run after form_entry has been deleted."""
        try:
            self.run_after_form_delete(request, form_entry_id)
            return True
        except:
            return False

    def run_after_form_delete(self, request, form_entry_id):
        """Run after form_entry has been deleted."""

# *****************************************************************************
# **************************** Add form element entry *************************
# *****************************************************************************


class AddFormElementEntryView(PermissionMixin, CreateView):
    """Add form element entry."""

    template_name = None
    form_class = None
    theme = None
    permission_classes = (AddFormElementEntryPermission,)

    def get_essential_objects(
            self,
            form_entry_id,
            form_element_plugin_uid,
            request,
    ):
        """Get essential objects."""
        try:
            form_entry = FormEntry._default_manager \
                .prefetch_related('formelemententry_set') \
                .get(pk=form_entry_id)
        except ObjectDoesNotExist as err:
            raise Http404(_("Form entry not found."))

        form_elements = form_entry.formelemententry_set.all()

        user_form_element_plugin_uids = get_user_form_field_plugin_uids(
            request.user
        )

        if form_element_plugin_uid not in user_form_element_plugin_uids:
            raise Http404(
                _("Plugin does not exist or you are not allowed "
                  "to use this plugin!"))

        form_element_plugin_cls = form_element_plugin_registry.get(
            form_element_plugin_uid
        )
        form_element_plugin = form_element_plugin_cls(user=request.user)
        form_element_plugin.request = request

        form_element_plugin_form_cls = form_element_plugin.get_form()
        # form = None

        obj = FormElementEntry()
        obj.form_entry = form_entry
        obj.plugin_uid = form_element_plugin_uid
        obj.user = request.user

        return (
            form_entry,
            form_elements,
            form_element_plugin_cls,
            form_element_plugin,
            form_element_plugin_form_cls,
            user_form_element_plugin_uids,
            obj,
        )

    def do_save_object(
        self,
        form_entry_id,
        form_entry,
        obj,
        form_element_plugin,
        request
    ):
        """Do save object."""
        # Handling the position
        position = 1
        records = FormElementEntry.objects.filter(form_entry=form_entry) \
            .aggregate(models.Max('position'))
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
            _('The form element plugin "{0}" was added '
              'successfully.').format(form_element_plugin.name)
        )
        return redirect(
            "{0}?active_tab=tab-form-elements".format(
                reverse_lazy(
                    'fobi.edit_form_entry',
                    kwargs={'form_entry_id': form_entry_id}
                )
            )
        )

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super(AddFormElementEntryView, self).get_context_data(**kwargs)

        if not self.theme:
            theme = get_theme(request=self.request, as_instance=True)
        else:
            theme = self.theme

        if theme:
            context.update({"fobi_theme": theme})
        return context

    def get_template_names(self):
        """Get template names."""
        template_name = self.template_name
        if not template_name:
            if not self.theme:
                theme = get_theme(request=self.request, as_instance=True)
            else:
                theme = self.theme
            template_name = theme.add_form_element_entry_template
        return [template_name]

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        self.object = None
        (
            form_entry,
            form_elements,
            form_element_plugin_cls,
            form_element_plugin,
            form_element_plugin_form_cls,
            user_form_element_plugin_uids,
            obj,
        ) = self.get_essential_objects(
            self.kwargs.get("form_entry_id"),
            self.kwargs.get("form_element_plugin_uid"),
            self.request,
        )

        save_object = False
        if not form_element_plugin_form_cls:
            save_object = True

        if not save_object:
            form = form_element_plugin.get_initialised_create_form_or_404()

        if save_object:
            return self.do_save_object(
                self.kwargs.get("form_entry_id"),
                form_entry,
                obj,
                form_element_plugin,
                request
            )

        return self.render_to_response(
            self.get_context_data(
                form=form,
                form_entry=form_entry,
                form_element_plugin=form_element_plugin,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        (
            form_entry,
            form_elements,
            form_element_plugin_cls,
            form_element_plugin,
            form_element_plugin_form_cls,
            user_form_element_plugin_uids,
            obj,
        ) = self.get_essential_objects(
            self.kwargs.get("form_entry_id"),
            self.kwargs.get("form_element_plugin_uid"),
            self.request,
        )

        save_object = False
        if not form_element_plugin_form_cls:
            save_object = True

        if not save_object:
            form = form_element_plugin.get_initialised_create_form_or_404(
                data=request.POST,
                files=request.FILES
            )
            form.validate_plugin_data(form_elements, request=request)
            if form.is_valid():
                # Saving the plugin form data.
                form.save_plugin_data(request=request)

                # Getting the plugin data.
                obj.plugin_data = form.get_plugin_data(request=request)
                save_object = True

        if save_object:
            return self.do_save_object(
                self.kwargs.get("form_entry_id"),
                form_entry,
                obj,
                form_element_plugin,
                request
            )

        return self.render_to_response(
            self.get_context_data(
                form=form,
                form_entry=form_entry,
                form_element_plugin=form_element_plugin,
            )
        )

# *****************************************************************************
# **************************** Edit form element entry ************************
# *****************************************************************************


class EditFormElementEntryView(PermissionMixin, UpdateView):
    """Edit form element entry view."""

    template_name = None
    form_class = None
    theme = None
    pk_url_kwarg = "form_element_entry_id"
    permission_classes = (EditFormElementEntryPermission,)

    # def __init__(self, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #     super(EditFormElementEntryView, self).__init__(*args, **kwargs)

    # def _get_queryset(self, request):
    #     """Get queryset."""
    #     return FormElementEntry._default_manager \
    #         .select_related('form_entry', 'form_entry__user') \
    #         .filter(form_entry__user__pk=request.user.pk)
    #
    # def get_essential_objects(
    #         self,
    #         form_element_entry_id,
    #         request,
    # ):
    #     """Get essential objects."""
    #     try:
    #         obj = self.get_object(queryset=self._get_queryset(request))
    #     except ObjectDoesNotExist as err:
    #         raise Http404(_("Form element entry not found."))
    #
    #     form_entry = obj.form_entry
    #     form_element_plugin = obj.get_plugin(request=request)
    #     form_element_plugin.request = request
    #
    #     form_element_plugin_form_cls = form_element_plugin.get_form()
    #
    #     return (
    #         form_entry,
    #         form_element_entry_id,
    #         form_element_plugin,
    #         form_element_plugin,
    #         form_element_plugin_form_cls,
    #         obj,
    #     )
    #
    # def get_context_data(self, **kwargs):
    #     """Get context data."""
    #     context = super(EditFormElementEntryView, self).get_context_data(**kwargs)
    #
    #     if not self.theme:
    #         theme = get_theme(request=self.request, as_instance=True)
    #     else:
    #         theme = self.theme
    #
    #     if theme:
    #         context.update({"fobi_theme": theme})
    #     return context
    #
    # def get_template_names(self):
    #     """Get template names."""
    #     template_name = self.template_name
    #     if not template_name:
    #         if not self.theme:
    #             theme = get_theme(request=self.request, as_instance=True)
    #         else:
    #             theme = self.theme
    #         template_name = theme.edit_form_element_entry_template
    #     return [template_name]
    #
    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     (
    #         form_entry,
    #         form_element_entry_id,
    #         form_element_plugin,
    #         form_element_plugin,
    #         form_element_plugin_form_cls,
    #         obj,
    #     ) = self.get_essential_objects(
    #         self.kwargs.get("form_element_entry_id"),
    #         self.request,
    #     )
    #     self.object = obj
    #     form = None
    #
    #     if not form_element_plugin_form_cls:
    #         messages.info(
    #             request,
    #             _('The form element plugin "{0}" '
    #               'is not configurable!').format(form_element_plugin.name)
    #         )
    #         return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)
    #
    #     else:
    #         form = form_element_plugin.get_initialised_edit_form_or_404()
    #
    #     return self.render_to_response(
    #         self.get_context_data(
    #             form=form,
    #             form_entry=form_entry,
    #             form_element_plugin=form_element_plugin,
    #         )
    #     )
    #
    # def post(self, request, *args, **kwargs):
    #     """
    #     Handle POST requests: instantiate a form instance with the passed
    #     POST variables and then check if it's valid.
    #     """
    #     self.object = None
    #     (
    #         form_entry,
    #         form_element_entry_id,
    #         form_element_plugin,
    #         form_element_plugin,
    #         form_element_plugin_form_cls,
    #         obj,
    #     ) = self.get_essential_objects(
    #         self.kwargs.get("form_element_entry_id"),
    #         self.request,
    #     )
    #     self.object = obj
    #
    #     if not form_element_plugin_form_cls:
    #         messages.info(
    #             request,
    #             _('The form element plugin "{0}" '
    #               'is not configurable!').format(form_element_plugin.name)
    #         )
    #         return redirect('fobi.edit_form_entry', form_entry_id=form_entry.pk)
    #
    #     form = form_element_plugin.get_initialised_edit_form_or_404(
    #         data=request.POST,
    #         files=request.FILES
    #     )
    #
    #     form_elements = FormElementEntry._default_manager \
    #         .select_related('form_entry',
    #                         'form_entry__user') \
    #         .exclude(pk=form_element_entry_id) \
    #         .filter(form_entry=form_entry)
    #
    #     form.validate_plugin_data(form_elements, request=request)
    #
    #     if form.is_valid():
    #         # Saving the plugin form data.
    #         form.save_plugin_data(request=request)
    #
    #         # Getting the plugin data.
    #         obj.plugin_data = form.get_plugin_data(request=request)
    #
    #         # Save the object.
    #         obj.save()
    #
    #         messages.info(
    #             request,
    #             _('The form element plugin "{0}" was edited '
    #               'successfully.').format(form_element_plugin.name)
    #         )
    #
    #     return self.render_to_response(
    #         self.get_context_data(
    #             form=form,
    #             form_entry=form_entry,
    #             form_element_plugin=form_element_plugin,
    #         )
    #     )
