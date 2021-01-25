from django.utils.translation import gettext_lazy as _

from fobi.base import BaseTheme, theme_registry
from fobi.contrib.themes.simple import UID

__title__ = 'fobi.contrib.themes.simple.fobi_themes'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SimpleTheme',)


class SimpleTheme(BaseTheme):
    """Simple theme that has a native Django style."""

    uid = UID
    name = _("Django admin style")

    media_css = (
        # 'admin/css/base.css',
        # 'admin/css/forms.css',
        # 'admin/css/widgets.css',
        'simple/css/fobi.simple.css',
        'jquery-ui/css/django-admin-theme/jquery-ui-1.10.4.custom.min.css',
        # 'admin_tools/css/menu.css', # TODO at least a conditional insert
    )

    media_js = (
        'js/jquery-1.10.2.min.js',
        'jquery-ui/js/jquery-ui-1.10.4.custom.min.js',
        'js/jquery.slugify.js',
        'js/fobi.core.js',
        # 'js/fobi.simple.js',
    )

    # footer_text = '&copy; django-fobi example site 2014'

    # ***********************************************************************
    # ***********************************************************************
    # ********************** Form HTML specific *****************************
    # ***********************************************************************
    # ***********************************************************************
    form_element_html_class = 'vTextField'
    form_radio_element_html_class = 'radiolist'
    form_element_checkbox_html_class = 'checkbox'

    # Important
    form_view_form_entry_option_class = 'glyphicon glyphicon-list'

    # Important
    form_edit_form_entry_option_class = 'glyphicon glyphicon-edit'

    # Important
    form_delete_form_entry_option_class = 'glyphicon glyphicon-remove'

    # Important
    form_list_container_class = 'list-inline'

    # ***********************************************************************
    # ***********************************************************************
    # **************************** Templates ********************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # *************************** Base templates ****************************
    # ***********************************************************************

    master_base_template = 'simple/_base.html'
    base_template = 'simple/base.html'
    base_view_template = 'simple/base_view.html'
    base_edit_template = 'simple/base_edit.html'

    # ***********************************************************************
    # ***************************** Snippets ********************************
    # ***********************************************************************
    form_snippet_template_name = 'simple/snippets/form_snippet.html'
    form_properties_snippet_template_name = \
        'simple/snippets/form_properties_snippet.html'
    messages_snippet_template_name = 'simple/snippets/messages_snippet.html'
    form_ajax = 'simple/snippets/form_ajax.html'
    form_view_snippet_template_name = 'simple/snippets/form_view_snippet.html'

    form_edit_ajax = 'simple/snippets/form_edit_ajax.html'
    form_edit_snippet_template_name = 'simple/snippets/form_edit_snippet.html'

    form_wizard_snippet_template_name = \
        'simple/snippets/form_wizard_snippet.html'

    form_wizard_properties_snippet_template_name = \
        'simple/snippets/form_wizard_properties_snippet.html'

    # ***********************************************************************
    # **************************** Form entry CRUD **************************
    # ***********************************************************************
    create_form_entry_template = 'simple/create_form_entry.html'
    create_form_entry_ajax_template = 'simple/create_form_entry_ajax.html'

    edit_form_entry_template = 'simple/edit_form_entry.html'
    edit_form_entry_ajax_template = 'simple/edit_form_entry_ajax.html'

    form_entry_submitted_template = 'simple/form_entry_submitted.html'
    form_entry_submitted_ajax_template = \
        'simple/form_entry_submitted_ajax.html'

    view_form_entry_template = 'simple/view_form_entry.html'
    view_form_entry_ajax_template = 'simple/view_form_entry_ajax.html'
    # ***********************************************************************
    # *********************** Form element entry CUD ************************
    # ***********************************************************************
    add_form_element_entry_template = 'simple/add_form_element_entry.html'
    add_form_element_entry_ajax_template = \
        'simple/add_form_element_entry_ajax.html'

    edit_form_element_entry_template = 'simple/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = \
        'simple/edit_form_element_entry_ajax.html'
    # ***********************************************************************
    # *********************** Form handler entry CUD ************************
    # ***********************************************************************
    add_form_handler_entry_template = 'simple/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = \
        'simple/add_form_handler_entry_ajax.html'

    edit_form_handler_entry_template = 'simple/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = \
        'simple/edit_form_handler_entry_ajax.html'

    # ***********************************************************************
    # ******************* Form wizard handler entry CUD *********************
    # ***********************************************************************

    # ***********************************************************************
    # ***************************** Dashboard *******************************
    # ***********************************************************************
    dashboard_template = 'simple/dashboard.html'
    forms_list_template = 'simple/forms_list.html'

    # ***********************************************************************
    # ************************ Form wizard entry CUD ************************
    # ***********************************************************************
    create_form_wizard_entry_template = \
        'simple/create_form_wizard_entry.html'
    create_form_wizard_entry_ajax_template = \
        'simple/create_form_wizard_entry_ajax.html'

    edit_form_wizard_entry_template = \
        'simple/edit_form_wizard_entry.html'
    edit_form_wizard_entry_ajax_template = \
        'simple/edit_form_wizard_entry_ajax.html'

    view_form_wizard_entry_template = \
        'simple/view_form_wizard_entry.html'
    view_form_wizard_entry_ajax_template = \
        'simple/view_form_wizard_entry_ajax.html'

    # ***********************************************************************
    # ************************* Form importer templates *********************
    # ***********************************************************************

    import_form_entry_template = 'simple/import_form_entry.html'
    import_form_entry_ajax_template = 'simple/import_form_entry_ajax.html'


theme_registry.register(SimpleTheme)
