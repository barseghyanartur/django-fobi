__title__ = 'fobi.contrib.plugins.form_handlers.db_store.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SavedFormDataEntryAdmin',)

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .models import SavedFormDataEntry
from .helpers import DataExporter

class SavedFormDataEntryAdmin(admin.ModelAdmin):
    """
    Saved form data entry admin.
    """
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

    class Meta:
        app_label = _('Saved form data entry')

    class Media:
        js = (
            '{0}js/jquery-1.10.2.min.js'.format(settings.STATIC_URL),
            '{0}db_store/js/db_store.js'.format(settings.STATIC_URL),
            '{0}db_store/js/jquery.expander.min.js'.format(settings.STATIC_URL),
            )

    def queryset(self, request):
        queryset = super(SavedFormDataEntryAdmin, self).queryset(request)
        #queryset = queryset.select_related('form_entry', 'user',)
        return queryset
    get_queryset = queryset

    def export_data(self, request, queryset):
        """
        Export data into XLS.
        """
        data_exporter = DataExporter(queryset)

        return data_exporter.graceful_export()

    export_data.short_description = _('Export data to CSV/XLS')


admin.site.register(SavedFormDataEntry, SavedFormDataEntryAdmin)
