from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .helpers import DataExporter
from .models import SavedFormDataEntry, SavedFormWizardDataEntry

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'SavedFormDataEntryAdmin',
    'SavedFormWizardDataEntryAdmin',
)

# *****************************************************************************
# ****************************** Generic **************************************
# *****************************************************************************


class BaseSavedFormDataEntryAdmin(admin.ModelAdmin):
    """Base saved data entry admin."""

    readonly_fields = ('created', 'formatted_saved_data')

    actions = ['export_data']
    only_args = []

    class Media:
        """Media class."""

        js = (
            '{0}js/jquery-1.10.2.min.js'.format(settings.STATIC_URL),
            '{0}db_store/js/db_store.js'.format(settings.STATIC_URL),
            '{0}db_store/js/jquery.expander.min.js'.format(
                settings.STATIC_URL
            ),
        )

    def get_queryset(self, request):
        """Get queryset."""
        qs = super(BaseSavedFormDataEntryAdmin, self).get_queryset(request)
        return qs

    def export_data(self, request, queryset):
        """Export data into XLS."""
        data_exporter = DataExporter(queryset, self.only_args)

        return data_exporter.graceful_export()

    export_data.short_description = _('Export data to CSV/XLS')

# *****************************************************************************
# **************************** Form handler ***********************************
# *****************************************************************************


class SavedFormDataEntryAdmin(BaseSavedFormDataEntryAdmin):
    """Saved form data entry admin."""

    list_display = ('form_entry', 'user', 'formatted_saved_data', 'created',)
    list_filter = ('form_entry', 'user',)
    readonly_fields = ('created', 'formatted_saved_data')
    fieldsets = (
        (None, {
            'fields': ('form_entry', 'user',)
        }),
        (_("Data"), {
            'fields': ('formatted_saved_data', 'created',)
        }),
        (_("Raw"), {
            'classes': ('collapse',),
            'fields': ('form_data_headers', 'saved_data',)
        }),
    )

    actions = ['export_data']
    only_args = ['form_entry']

    class Meta:
        """Meta class."""

        app_label = _('Saved form data entry')

    # class Media:
    #     """Media class."""
    #
    #     js = (
    #         '{0}js/jquery-1.10.2.min.js'.format(settings.STATIC_URL),
    #         '{0}db_store/js/db_store.js'.format(settings.STATIC_URL),
    #         '{0}db_store/js/jquery.expander.min.js'.format(
    #             settings.STATIC_URL
    #         ),
    #     )


admin.site.register(SavedFormDataEntry, SavedFormDataEntryAdmin)

# *****************************************************************************
# ************************ Form wizard handler ********************************
# *****************************************************************************


class SavedFormWizardDataEntryAdmin(BaseSavedFormDataEntryAdmin):
    """Saved form wizard data entry admin."""

    list_display = ('form_wizard_entry', 'user', 'formatted_saved_data',
                    'created',)
    list_filter = ('form_wizard_entry', 'user',)
    readonly_fields = ('created', 'formatted_saved_data')
    fieldsets = (
        (None, {
            'fields': ('form_wizard_entry', 'user',)
        }),
        (_("Data"), {
            'fields': ('formatted_saved_data', 'created',)
        }),
        (_("Raw"), {
            'classes': ('collapse',),
            'fields': ('form_data_headers', 'saved_data',)
        }),
    )

    actions = ['export_data']
    only_args = ['form_wizard_entry']

    class Meta:
        """Meta class."""

        app_label = _('Saved form wizard data entry')


admin.site.register(SavedFormWizardDataEntry, SavedFormWizardDataEntryAdmin)
