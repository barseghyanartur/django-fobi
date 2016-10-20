from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import SavedFormDataEntryReference

__all__ = ('SavedFormDataEntryReferenceAdmin',)


class SavedFormDataEntryReferenceAdmin(admin.ModelAdmin):
    list_display = ('form',)

    class Meta:
        app_label = _('ForeignKey to db_store.SavedFormDataEntry')


admin.site.register(
    SavedFormDataEntryReference, SavedFormDataEntryReferenceAdmin
)
