from django.conf.urls import url

from ..views import (
    view_saved_form_data_entries, export_saved_form_data_entries,
)

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
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
    url(r'^(?P<form_entry_id>\d+)/$',
        view=view_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),

    # Form entries listing
    url(r'^$',
        view=view_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),

    # ***********************************************************************
    # ***************************** Export **********************************
    # ***********************************************************************
    # Specific form entries export
    url(r'^export/(?P<form_entry_id>\d+)/$',
        view=export_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'export_saved_form_data_entries'),

    # Form entries export
    url(r'^export/$',
        view=export_saved_form_data_entries,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'export_saved_form_data_entries'),
]
