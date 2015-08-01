__title__ = 'fobi.contrib.themes.bootstrap3.fobi_themes'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Bootstrap3Theme',)

from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseTheme, theme_registry

from . import UID

class Bootstrap3Theme(BaseTheme):
    """
    Bootstrap3 theme.
    """
    uid = UID
    name = _("Bootstrap 3")

    media_css = (
        'bootstrap3/css/bootstrap.css',
        'bootstrap3/css/bootstrap3_fobi_extras.css',
        'css/fobi.core.css',
    )

    media_js = (
        'js/jquery-1.10.2.min.js',
        'jquery-ui/js/jquery-ui-1.10.4.custom.min.js',
        'bootstrap3/js/bootstrap.min.js',
        'js/jquery.slugify.js',
        'js/fobi.core.js',
        'bootstrap3/js/bootstrap3_fobi_extras.js', # Theme-specific scripts
    )

    #footer_text = '&copy; django-fobi example site 2014'

    # *************************************************************************
    # ********************** Form HTML specific *******************************
    # *************************************************************************
    form_element_html_class = 'form-control'
    form_element_checkbox_html_class = 'checkbox'

    # Important!
    form_edit_form_entry_option_class = 'glyphicon glyphicon-edit'

    # Important!
    form_delete_form_entry_option_class = 'glyphicon glyphicon-remove'

    # Important!
    form_list_container_class = 'list-inline'

    # *************************************************************************
    # ********************** Templates specific *******************************
    # *************************************************************************
    master_base_template = 'bootstrap3/_base.html'
    base_template = 'bootstrap3/base.html'

    form_ajax = 'bootstrap3/snippets/form_ajax.html'
    form_snippet_template_name = 'bootstrap3/snippets/form_snippet.html'
    form_properties_snippet_template_name = \
        'bootstrap3/snippets/form_properties_snippet.html'
    messages_snippet_template_name = 'bootstrap3/snippets/messages_snippet.html'
    form_non_field_and_hidden_errors_snippet_template = \
        'bootstrap3/snippets/form_non_field_and_hidden_errors_snippet.html'

    add_form_element_entry_template = 'bootstrap3/add_form_element_entry.html'
    add_form_element_entry_ajax_template = \
        'bootstrap3/add_form_element_entry_ajax.html'

    add_form_handler_entry_template = 'bootstrap3/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = \
        'bootstrap3/add_form_handler_entry_ajax.html'

    create_form_entry_template = 'bootstrap3/create_form_entry.html'
    create_form_entry_ajax_template = 'bootstrap3/create_form_entry_ajax.html'

    dashboard_template = 'bootstrap3/dashboard.html'

    edit_form_element_entry_template = 'bootstrap3/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = \
        'bootstrap3/edit_form_element_entry_ajax.html'

    edit_form_entry_template = 'bootstrap3/edit_form_entry.html'
    edit_form_entry_ajax_template = 'bootstrap3/edit_form_entry_ajax.html'

    edit_form_handler_entry_template = 'bootstrap3/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = \
        'bootstrap3/edit_form_handler_entry_ajax.html'

    form_entry_submitted_template = 'bootstrap3/form_entry_submitted.html'
    form_entry_submitted_ajax_template = \
        'bootstrap3/form_entry_submitted_ajax.html'
    embed_form_entry_submitted_ajax_template = \
        'bootstrap3/embed_form_entry_submitted_ajax.html'

    view_form_entry_template = 'bootstrap3/view_form_entry.html'
    view_form_entry_ajax_template = 'bootstrap3/view_form_entry_ajax.html'
    view_embed_form_entry_ajax_template = \
        'bootstrap3/view_embed_form_entry_ajax.html'


theme_registry.register(Bootstrap3Theme)
