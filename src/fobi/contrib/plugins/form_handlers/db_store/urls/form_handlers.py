from django.urls import path

from ..views import (
    view_saved_form_data_entries, export_saved_form_data_entries,
)

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    # ***********************************************************************
    # ***********************************************************************
    # ************************* Form handlers *******************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # **************************** Listing **********************************
    # ***********************************************************************
    # Specific form entries listing
    path('<int:form_entry_id>/',
        view=view_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),

    # Form entries listing
    path('',
        view=view_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),

    # ***********************************************************************
    # ***************************** Export **********************************
    # ***********************************************************************
    # Specific form entries export
    path('export/<int:form_entry_id>/',
        view=export_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'export_saved_form_data_entries'),

    # Form entries export
    path('export/',
        view=export_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'export_saved_form_data_entries'),
]
