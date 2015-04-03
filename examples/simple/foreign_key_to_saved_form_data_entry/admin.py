__all__ = ('SavedFormDataEntryReferenceAdmin',)

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from foreign_key_to_saved_form_data_entry.models import (
    SavedFormDataEntryReference
    )

class SavedFormDataEntryReferenceAdmin(admin.ModelAdmin):
    list_display = ('form',)

    class Meta:
        app_label = _('ForeignKey to db_store.SavedFormDataEntry')


admin.site.register(SavedFormDataEntryReference, 
                    SavedFormDataEntryReferenceAdmin)
