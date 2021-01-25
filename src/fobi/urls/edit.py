from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from fobi.views import (
    add_form_element_entry,
    add_form_handler_entry,
    add_form_wizard_form_entry,
    add_form_wizard_handler_entry,
    create_form_entry,
    create_form_wizard_entry,
    dashboard,
    delete_form_element_entry,
    delete_form_entry,
    delete_form_handler_entry,
    delete_form_wizard_entry,
    delete_form_wizard_form_entry,
    delete_form_wizard_handler_entry,
    edit_form_element_entry,
    edit_form_entry,
    edit_form_handler_entry,
    edit_form_wizard_entry,
    edit_form_wizard_handler_entry,
    export_form_entry,
    export_form_wizard_entry,
    form_importer,
    form_wizards_dashboard,
    import_form_entry,
    import_form_wizard_entry
)

__title__ = 'fobi.urls.edit'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    # ***********************************************************************
    # **************************** Form entry CUD ***************************
    # ***********************************************************************

    # Create form entry
    url(_(r'^forms/create/$'),
        view=create_form_entry,
        name='fobi.create_form_entry'),

    # Edit form entry
    url(_(r'^forms/edit/(?P<form_entry_id>\d+)/$'),
        edit_form_entry,
        name='fobi.edit_form_entry'),

    # Delete form entry
    url(_(r'^forms/delete/(?P<form_entry_id>\d+)/$'),
        delete_form_entry,
        name='fobi.delete_form_entry'),

    # ***********************************************************************
    # ************************ Form entry add-ons ***************************
    # ***********************************************************************

    # Export form entry
    url(_(r'^forms/export/(?P<form_entry_id>\d+)/$'),
        export_form_entry,
        name='fobi.export_form_entry'),

    # Import form entry
    url(_(r'^forms/import/$'),
        import_form_entry,
        name='fobi.import_form_entry'),

    # Form importers
    url(_(r'^forms/importer/(?P<form_importer_plugin_uid>[\w_\-]+)/$'),
        form_importer,
        name='fobi.form_importer'),

    # ***********************************************************************
    # *********************** Form element entry CUD ************************
    # ***********************************************************************

    # Add form element entry
    url(_(r'^forms/elements/add/(?P<form_entry_id>\d+)/'
          r'(?P<form_element_plugin_uid>[\w_\-]+)/$'),
        add_form_element_entry,
        name='fobi.add_form_element_entry'),

    # Edit form element entry
    url(_(r'^forms/elements/edit/(?P<form_element_entry_id>\d+)/$'),
        edit_form_element_entry,
        name='fobi.edit_form_element_entry'),

    # Delete form element entry
    url(_(r'^forms/elements/delete/(?P<form_element_entry_id>\d+)/$'),
        delete_form_element_entry,
        name='fobi.delete_form_element_entry'),

    # ***********************************************************************
    # *********************** Form handler entry CUD ************************
    # ***********************************************************************

    # Add form handler entry
    url(_(r'^forms/handlers/add/(?P<form_entry_id>\d+)/'
          r'(?P<form_handler_plugin_uid>[\w_\-]+)/$'),
        add_form_handler_entry,
        name='fobi.add_form_handler_entry'),

    # Edit form handler entry
    url(_(r'^forms/handlers/edit/(?P<form_handler_entry_id>\d+)/$'),
        edit_form_handler_entry,
        name='fobi.edit_form_handler_entry'),

    # Delete form handler entry
    url(_(r'^forms/handlers/delete/(?P<form_handler_entry_id>\d+)/$'),
        delete_form_handler_entry,
        name='fobi.delete_form_handler_entry'),

    # ***********************************************************************
    # ************************ Form wizard entry CUD ************************
    # ***********************************************************************

    # Create form wizard entry
    url(_(r'^wizard/create/$'),
        view=create_form_wizard_entry,
        name='fobi.create_form_wizard_entry'),

    # Edit form wizard entry
    url(_(r'^wizard/edit/(?P<form_wizard_entry_id>\d+)/$'),
        edit_form_wizard_entry,
        name='fobi.edit_form_wizard_entry'),

    # Delete form wizard entry
    url(_(r'^wizard/delete/(?P<form_wizard_entry_id>\d+)/$'),
        delete_form_wizard_entry,
        name='fobi.delete_form_wizard_entry'),

    # ***********************************************************************
    # ******************** Form wizard form entry CUD ***********************
    # ***********************************************************************

    # Add form wizard form entry
    url(_(r'^wizard/forms/add/(?P<form_wizard_entry_id>\d+)/'
          r'(?P<form_entry_id>[\w_\-]+)/$'),
        add_form_wizard_form_entry,
        name='fobi.add_form_wizard_form_entry'),

    # # Edit form wizard form entry
    # url(_(r'^wizard/forms/edit/(?P<form_element_entry_id>\d+)/$'),
    #     edit_form_wizard_form_entry,
    #     name='fobi.edit_form_wizard_form_entry'),
    #
    # Delete form wizard form entry
    url(_(r'^wizard/elements/delete/(?P<form_wizard_form_entry_id>\d+)/$'),
        delete_form_wizard_form_entry,
        name='fobi.delete_form_wizard_form_entry'),

    # ***********************************************************************
    # ******************* Form wizard handler entry CUD *********************
    # ***********************************************************************

    # Add form wizard handler entry
    url(_(r'^wizard/handlers/add/(?P<form_wizard_entry_id>\d+)/'
          r'(?P<form_wizard_handler_plugin_uid>[\w_\-]+)/$'),
        add_form_wizard_handler_entry,
        name='fobi.add_form_wizard_handler_entry'),

    # Edit form wizard handler entry
    url(_(r'^wizard/handlers/edit/(?P<form_wizard_handler_entry_id>\d+)/$'),
        edit_form_wizard_handler_entry,
        name='fobi.edit_form_wizard_handler_entry'),

    # Delete form wizard handler entry
    url(_(r'^wizard/handlers/delete/(?P<form_wizard_handler_entry_id>\d+)/$'),
        delete_form_wizard_handler_entry,
        name='fobi.delete_form_wizard_handler_entry'),

    # ***********************************************************************
    # *********************** Form wizard entry add-ons *********************
    # ***********************************************************************

    # Export form wizard entry
    url(_(r'^wizard/export/(?P<form_wizard_entry_id>\d+)/$'),
        export_form_wizard_entry,
        name='fobi.export_form_wizard_entry'),

    # Import form wizard entry
    url(_(r'^wizard/import/$'),
        import_form_wizard_entry,
        name='fobi.import_form_wizard_entry'),

    # ***********************************************************************
    # ****************************** Dashboard ******************************
    # ***********************************************************************

    # Forms dashboard
    url(_(r'^$'), view=dashboard, name='fobi.dashboard'),

    # Form wizards dashboard
    url(_(r'^wizards/$'),
        view=form_wizards_dashboard,
        name='fobi.form_wizards_dashboard'),
]
