from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags

from nine.versions import DJANGO_LTE_1_5

from .constants import ACTION_CHOICE_REPLACE
from .forms import (
    BulkChangeFormElementPluginsForm,
    BulkChangeFormHandlerPluginsForm,
    BulkChangeFormWizardHandlerPluginsForm,
    FormElementEntryForm,
    FormHandlerEntryForm,
    FormWizardHandlerEntryForm
)
from .models import (
    FormElement,
    FormHandler,
    FormWizardHandler,
    FormEntry,
    FormElementEntry,
    FormHandlerEntry,
    FormWizardEntry,
    FormWizardFormEntry,
    FormWizardHandlerEntry
)

__title__ = 'fobi.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'base_bulk_change_plugins',
    'bulk_change_form_element_plugins',
    'bulk_change_form_handler_plugins',
    'bulk_change_form_wizard_handler_plugins',

    'FormElementEntryInlineAdmin',
    'FormHandlerEntryInlineAdmin',
    'FormWizardFormEntryInlineAdmin',

    'FormWizardHandlerEntryInlineAdmin',
    'FormEntryAdmin',
    'FormWizardEntryAdmin',
    'FormFieldsetEntryAdmin',

    'FormElementEntryAdmin',
    'FormHandlerEntryAdmin',

    'BasePluginModelAdmin',

    'FormElementAdmin',
    'FormHandlerAdmin',
    'FormWizardHandlerAdmin',
)

staff_member_required_m = method_decorator(staff_member_required)

# *****************************************************************************
# *****************************************************************************
# ******************************* Admin helpers *******************************
# *****************************************************************************
# *****************************************************************************


def base_bulk_change_plugins(PluginForm, named_url, modeladmin, request,
                             queryset):
    """Bulk change of plugins action additional view."""

    opts = modeladmin.model._meta
    app_label = opts.app_label

    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    post = dict(request.POST)
    if selected:
        post['selected_plugins'] = ','.join(selected)
    if 'POST' == request.method:
        form = PluginForm(
            data=post,
            files=request.FILES,
            initial={'selected_plugins': ','.join(selected)}
        )
    else:
        form = PluginForm(initial={'selected_plugins': ','.join(selected)})

    context = {
        'form': form,
        'app_label': app_label,
        'opts': opts,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        'named_url': named_url,
    }
    return render_to_response(
        'fobi/admin/bulk_change_plugins.html',
        context,
        context_instance=RequestContext(request)
    )


def bulk_change_form_element_plugins(modeladmin, request, queryset):
    """Bulk change FormElement plugins."""
    return base_bulk_change_plugins(
        BulkChangeFormElementPluginsForm,
        'admin:bulk_change_form_element_plugins',
        modeladmin,
        request,
        queryset
    )


def bulk_change_form_handler_plugins(modeladmin, request, queryset):
    """Bulk change FormHandler plugins."""
    return base_bulk_change_plugins(
        BulkChangeFormHandlerPluginsForm,
        'admin:bulk_change_form_handler_plugins',
        modeladmin,
        request,
        queryset
    )


def bulk_change_form_wizard_handler_plugins(modeladmin, request, queryset):
    """Bulk change FormWizardHandler plugins."""
    return base_bulk_change_plugins(
        BulkChangeFormWizardHandlerPluginsForm,
        'admin:bulk_change_form_wizard_handler_plugins',
        modeladmin,
        request,
        queryset
    )

# *****************************************************************************
# *****************************************************************************
# ******************************* Entry admin *********************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# ******************************* Form entry admin ****************************
# *****************************************************************************


class FormElementEntryInlineAdmin(admin.TabularInline):
    """FormElementEntry inline admin."""

    model = FormElementEntry
    form = FormElementEntryForm
    fields = ('form_entry', 'plugin_uid', 'plugin_data', 'position',)
    extra = 0


class FormHandlerEntryInlineAdmin(admin.TabularInline):
    """FormHandlerEntry inline admin."""

    model = FormHandlerEntry
    form = FormHandlerEntryForm
    fields = ('form_entry', 'plugin_uid', 'plugin_data',)
    extra = 0


class FormEntryAdmin(admin.ModelAdmin):
    """FormEntry admin."""

    list_display = ('name', 'slug', 'user', 'is_public', 'created', 'updated',
                    'is_cloneable',)
    list_editable = ('is_public', 'is_cloneable',)
    list_filter = ('is_public', 'is_cloneable',)
    readonly_fields = ('slug',)
    radio_fields = {"user": admin.VERTICAL}
    fieldsets = (
        (_("Form"), {
            'fields': ('name', 'is_public', 'is_cloneable',)
        }),
        (_("Custom"), {
            'classes': ('collapse',),
            'fields': ('success_page_title', 'success_page_message', 'action',)
        }),
        # (_("Wizard"), {
        #     'classes': ('collapse',),
        #     'fields': ('form_wizard_entry', 'position',)
        # }),
        (_("User"), {
            'classes': ('collapse',),
            'fields': ('user',)
        }),
        (_('Additional'), {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
    inlines = [FormElementEntryInlineAdmin, FormHandlerEntryInlineAdmin]

    class Meta:
        """Meta."""

        app_label = _('Fobi')


admin.site.register(FormEntry, FormEntryAdmin)


# *****************************************************************************
# *************************** Form wizard entry admin *************************
# *****************************************************************************


class FormWizardFormEntryInlineAdmin(admin.TabularInline):
    """FormWizardFormEntry inline admin."""

    model = FormWizardFormEntry
    # form = FormElementEntryForm
    fields = ('form_entry', 'position',)
    extra = 0


class FormWizardHandlerEntryInlineAdmin(admin.TabularInline):
    """FormWizardHandlerEntry inline admin."""

    model = FormWizardHandlerEntry
    form = FormWizardHandlerEntryForm
    fields = ('plugin_uid', 'plugin_data',)
    extra = 0


class FormWizardEntryAdmin(admin.ModelAdmin):
    """FormWizardEntry admin."""

    list_display = ('name', 'slug', 'user', 'is_public', 'created', 'updated',
                    'is_cloneable',)
    list_editable = ('is_public', 'is_cloneable',)
    list_filter = ('is_public', 'is_cloneable',)
    readonly_fields = ('slug',)
    radio_fields = {"user": admin.VERTICAL}
    fieldsets = (
        (_("Form"), {
            'fields': ('name', 'is_public', 'is_cloneable',)
        }),
        (_("Custom"), {
            'classes': ('collapse',),
            'fields': ('success_page_title', 'success_page_message',)
        }),
        # (_("Wizard"), {
        #     'classes': ('collapse',),
        #     'fields': ('form_wizard_entry', 'position',)
        # }),
        (_("User"), {
            'classes': ('collapse',),
            'fields': ('user',)
        }),
        (_('Additional'), {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
    inlines = [FormWizardFormEntryInlineAdmin,
               FormWizardHandlerEntryInlineAdmin]

    class Meta:
        """Meta."""

        app_label = _('Fobi')


admin.site.register(FormWizardEntry, FormWizardEntryAdmin)

# *****************************************************************************
# ************************* Form fieldset entry admin *************************
# *****************************************************************************


class FormFieldsetEntryAdmin(admin.ModelAdmin):
    """FormEieldsetEntry admin."""

    list_display = ('form_entry', 'name', 'is_repeatable')
    list_editable = ('is_repeatable',)
    list_filter = ('is_repeatable',)
    # readonly_fields = ('slug',)
    fieldsets = (
        (None, {
            'fields': ('form_entry', 'name', 'is_repeatable')
        }),
    )

    class Meta:
        app_label = _('Fobi')


# admin.site.register(FormFieldsetEntry, FormFieldsetEntryAdmin)

# *****************************************************************************
# ************************** Form element entry admin *************************
# *****************************************************************************

class FormElementEntryAdmin(admin.ModelAdmin):
    """FormElementEntry admin."""

    list_display = ('plugin_uid', 'plugin_uid_code', 'plugin_data', 'position',
                    'form_entry',)
    list_filter = ('form_entry', 'plugin_uid')
    list_editable = ('position',)
    readonly_fields = ('plugin_uid_code',)
    fieldsets = (
        (_("Plugin"), {
            'fields': ('plugin_uid', 'plugin_data',)
        }),
        (_("Form"), {
            'fields': ('form_entry', 'form_fieldset_entry', 'position',)
        }),
    )

    class Meta:
        """Meta."""
        app_label = _('Fobi')

    def __queryset(self, request):
        """Internal method used in get_queryset or queryset methods."""
        if DJANGO_LTE_1_5:
            queryset = super(FormElementEntryAdmin, self).queryset(request)
        else:
            queryset = super(FormElementEntryAdmin, self).get_queryset(request)

        queryset = queryset.select_related('form_entry', 'form_fieldset_entry')
        return queryset
    get_queryset = __queryset
    if DJANGO_LTE_1_5:
        queryset = __queryset

# admin.site.register(FormElementEntry, FormElementEntryAdmin)


# *****************************************************************************
# ************************** Form element entry admin *************************
# *****************************************************************************

class FormHandlerEntryAdmin(admin.ModelAdmin):
    """FormHandlerEntry admin."""

    list_display = ('plugin_uid', 'plugin_uid_code', 'plugin_data',
                    'form_entry',)
    list_filter = ('form_entry', 'plugin_uid')
    readonly_fields = ('plugin_uid_code',)
    fieldsets = (
        (_("Plugin"), {
            'fields': ('plugin_uid', 'plugin_data',)
        }),
        (_("Form"), {
            'fields': ('form_entry',)
        }),
    )

    class Meta:
        """Meta."""
        app_label = _('Form handler entry')

    def __queryset(self, request):
        """Internal method used in get_queryset or queryset methods."""
        if DJANGO_LTE_1_5:
            queryset = super(FormHandlerEntryAdmin, self).queryset(request)
        else:
            queryset = super(FormHandlerEntryAdmin, self).get_queryset(request)

        queryset = queryset.select_related('form_entry',)
        return queryset
    get_queryset = __queryset
    if DJANGO_LTE_1_5:
        queryset = __queryset

# admin.site.register(FormHandlerEntry, FormHandlerEntryAdmin)

# *****************************************************************************
# *****************************************************************************
# ******************************* Plugin admin ********************************
# *****************************************************************************
# *****************************************************************************

# *****************************************************************************
# ********************************** Abstract *********************************
# *****************************************************************************


class BasePluginModelAdmin(admin.ModelAdmin):
    """Base plugin admin."""

    list_display = ('plugin_uid_admin', 'users_list', 'groups_list')
    readonly_fields = ('plugin_uid', 'plugin_uid_admin')
    fieldsets = (
        (None, {
            'fields': ('plugin_uid', 'users', 'groups')
        }),
    )
    filter_horizontal = ('users', 'groups',)

    class Meta:
        """Meta."""
        app_label = _('Fobi')

    def has_add_permission(self, request):
        """Has add permissions.

        We don't want to allow to add form elements/handlers manually. It
        should happen using the management command ``fobi_sync_plugins``
        instead.
        """
        return False

    def __queryset(self, request):
        """Internal method used in get_queryset or queryset methods."""
        if DJANGO_LTE_1_5:
            queryset = super(BasePluginModelAdmin, self).queryset(request)
        else:
            queryset = super(BasePluginModelAdmin, self).get_queryset(request)

        queryset = queryset.prefetch_related('users', 'groups')
        return queryset
    get_queryset = __queryset
    if DJANGO_LTE_1_5:
        queryset = __queryset

    def _get_bulk_change_form_class(self):
        """Get change form class for bulk actions."""
        raise NotImplemented("You should implement "
                             "`get_bulk_change_form_class`")

    def _get_model(self):
        """Get model."""
        raise NotImplemented("You should implement `_get_model`")

    def _get_changelist_named_url(self):
        """Get changelist named URL."""
        raise NotImplemented("You should implement "
                             "`_get_changelist_named_url`")

    @staff_member_required_m
    def bulk_change_plugins(self, request):
        """Bulk change plugins.

        This is where the data is actually processed.
        """
        changelist_named_url = self._get_changelist_named_url()
        if 'POST' == request.method:
            form_cls = self._get_bulk_change_form_class()
            form = form_cls(
                data=request.POST,
                files=request.FILES
            )

            if form.is_valid():
                ids = form.cleaned_data.pop('selected_plugins').split(',')
                users = form.cleaned_data.pop('users')
                groups = form.cleaned_data.pop('groups')
                users_action = form.cleaned_data.pop('users_action')
                groups_action = form.cleaned_data.pop('groups_action')
                cleaned_data = dict(
                    (key, val)
                    for (key, val) in form.cleaned_data.iteritems()
                    if val is not None
                )

                # Queryset to work with
                PluginModel = self._get_model()
                queryset = PluginModel._default_manager.filter(pk__in=ids)

                # Update simple fields
                updated = queryset.update(**cleaned_data)

                # Update groups
                for plugin_model_entry in queryset:
                    # If groups action chose is ``replace``, clearing
                    # the groups first.
                    if groups_action == ACTION_CHOICE_REPLACE:
                        plugin_model_entry.groups.clear()

                    # If users action chose is ``replace``, clearing
                    # the users first.
                    if users_action == ACTION_CHOICE_REPLACE:
                        plugin_model_entry.users.clear()

                    plugin_model_entry.groups.add(*groups)  # Adding groups
                    plugin_model_entry.users.add(*users)  # Adding users

                messages.info(
                    request,
                    _('{0} plugins were changed '
                      'successfully.').format(len(ids))
                )
                return redirect(changelist_named_url)
            else:
                messages.warning(
                    request,
                    _('Form contains '
                      'errors: {}').format(strip_tags(form.errors))
                )
                return redirect(changelist_named_url)
        else:
            messages.warning(
                request,
                _('POST required when changing in bulk!')
            )
            return redirect(changelist_named_url)

# *****************************************************************************
# ********************************** Form element *****************************
# *****************************************************************************


class FormElementAdmin(BasePluginModelAdmin):
    """FormElement admin."""

    actions = [bulk_change_form_element_plugins]

    def _get_bulk_change_form_class(self):
        """Get bulk change form class."""
        return BulkChangeFormElementPluginsForm

    def _get_model(self):
        """Get model."""
        return FormElement

    def _get_changelist_named_url(self):
        """Get changelist named URL."""
        return 'admin:fobi_formelement_changelist'

    def get_urls(self):
        """Get URLs."""
        my_urls = [
            # Bulk change plugins
            url(r'^bulk-change-form-element-plugins/$',
                self.bulk_change_plugins,
                name='bulk_change_form_element_plugins'),
        ]
        return my_urls + super(FormElementAdmin, self).get_urls()


admin.site.register(FormElement, FormElementAdmin)

# *****************************************************************************
# *********************************** Form handler ****************************
# *****************************************************************************


class FormHandlerAdmin(BasePluginModelAdmin):
    """FormHandler admin."""

    actions = [bulk_change_form_handler_plugins]

    def _get_bulk_change_form_class(self):
        """Get bulk change form class."""
        return BulkChangeFormHandlerPluginsForm

    def _get_model(self):
        """Get model."""
        return FormHandler

    def _get_changelist_named_url(self):
        """Get changelist named URL."""
        return 'admin:fobi_formhandler_changelist'

    def get_urls(self):
        """Get URLs."""
        my_urls = [
            # Bulk change plugins
            url(r'^bulk-change-form-handler-plugins/$',
                self.bulk_change_plugins,
                name='bulk_change_form_handler_plugins'),
        ]
        return my_urls + super(FormHandlerAdmin, self).get_urls()


admin.site.register(FormHandler, FormHandlerAdmin)

# *****************************************************************************
# ****************************** Form wizard handler **************************
# *****************************************************************************


class FormWizardHandlerAdmin(BasePluginModelAdmin):
    """FormHandler admin."""

    actions = [bulk_change_form_wizard_handler_plugins]

    def _get_bulk_change_form_class(self):
        """Get bulk change form class."""
        return BulkChangeFormWizardHandlerPluginsForm

    def _get_model(self):
        """Get model."""
        return FormHandler

    def _get_changelist_named_url(self):
        """Get changelist named URL."""
        return 'admin:fobi_formwizardhandler_changelist'

    def get_urls(self):
        """Get URLs."""
        my_urls = [
            # Bulk change plugins
            url(r'^bulk-change-form-wizard-handler-plugins/$',
                self.bulk_change_plugins,
                name='bulk_change_form_wizard_handler_plugins'),
        ]
        return my_urls + super(FormWizardHandlerAdmin, self).get_urls()


admin.site.register(FormWizardHandler, FormWizardHandlerAdmin)
