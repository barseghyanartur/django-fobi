__title__ = 'fobi.urls.edit'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

from django.conf.urls import url #patterns, include

from fobi.views import (
    dashboard, create_form_entry, edit_form_entry, delete_form_entry,
    add_form_element_entry, edit_form_element_entry, delete_form_element_entry,
    add_form_handler_entry, edit_form_handler_entry, delete_form_handler_entry,
)

#urlpatterns = patterns('fobi.views',
urlpatterns = [
    # Form submitted success page
    #url(r'^view/submitted/$', view='form_entry_submitted', name='fobi.form_entry_submitted'),

    # View form entry
    #url(r'^view/(?P<form_entry_slug>[\w_\-]+)/$', 'view_form_entry', name='fobi.view_form_entry'),

    # Form submitted success page
    #url(r'^view/(?P<form_entry_slug>[\w_\-]+)/submitted/$', view='form_entry_submitted', name='fobi.form_entry_submitted'),

    # Create form entry
    url(r'^forms/create/$', view=create_form_entry, name='fobi.create_form_entry'),

    # Edit form entry
    url(r'^forms/edit/(?P<form_entry_id>\d+)/$', edit_form_entry, name='fobi.edit_form_entry'),

    # Delete form entry
    url(r'^forms/delete/(?P<form_entry_id>\d+)/$', delete_form_entry, name='fobi.delete_form_entry'),

    # Add form element entry
    url(r'^forms/elements/add/(?P<form_entry_id>\d+)/(?P<form_element_plugin_uid>[\w_\-]+)/$',
        add_form_element_entry, name='fobi.add_form_element_entry'),

    # Edit form element entry
    url(r'^forms/elements/edit/(?P<form_element_entry_id>\d+)/$',
        edit_form_element_entry, name='fobi.edit_form_element_entry'),

    # Delete form element entry
    url(r'^forms/elements/delete/(?P<form_element_entry_id>\d+)/$',
        delete_form_element_entry, name='fobi.delete_form_element_entry'),

    # Add form handler entry
    url(r'^forms/handlers/add/(?P<form_entry_id>\d+)/(?P<form_handler_plugin_uid>[\w_\-]+)/$',
        add_form_handler_entry, name='fobi.add_form_handler_entry'),

    # Edit form handler entry
    url(r'^forms/handlers/edit/(?P<form_handler_entry_id>\d+)/$',
        edit_form_handler_entry, name='fobi.edit_form_handler_entry'),

    # Delete form handler entry
    url(r'^forms/handlers/delete/(?P<form_handler_entry_id>\d+)/$',
        delete_form_handler_entry, name='fobi.delete_form_handler_entry'),

    # Dashboard
    url(r'^$', view=dashboard, name='fobi.dashboard'),
#)
]
