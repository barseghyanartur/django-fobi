from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseTheme, theme_registry

from . import UID

__title__ = 'fobi.contrib.themes.foundation5.fobi_themes'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Foundation5Theme',)


class Foundation5Theme(BaseTheme):
    """Foundation5 theme.

    Based on the "Workspace" example of the Foundation 5.
    Click `here <http://foundation.zurb.com/templates/contact.html>`_ for
    more.
    """
    uid = UID
    name = _("Foundation 5")

    media_css = (
        'foundation5/css/foundation.min.css',
        'foundation5/css/foundation_fobi_extras.css',
        'foundation5/icons/3/icons/foundation-icons.css',
        # 'foundation5/icons/2/accessibility/stylesheets/'
        # 'accessibility_foundicons.css',
        # 'foundation5/css/foundation_template-4.css', # Foundation Template 4
        # 'foundation5/css/normalize.css',
        # 'css/fobi.core.css',
    )

    media_js = (
        'foundation5/js/vendor/modernizr.js',
        # 'foundation5/js/foundation.min.js',
        # 'js/jquery-1.10.2.min.js',
        'foundation5/js/vendor/jquery.js',
        # 'foundation5/js/vendor/fastclick.js',
        'jquery-ui/js/jquery-ui-1.10.4.custom.min.js',
        # 'foundation5/js/foundation_template-4.js', # Foundation Template 4
        'foundation5/js/foundation.min.js',
        'js/fobi.core.js',
        'js/jquery.slugify.js',
        'foundation5/js/foundation5_fobi_extras.js',  # Theme specific scripts
    )

    # footer_text = '&copy; django-fobi example site 2014'

    # ***********************************************************************
    # ***********************************************************************
    # ********************** Form HTML specific *****************************
    # ***********************************************************************
    form_element_html_class = 'form-control'
    form_element_checkbox_html_class = 'checkbox'

    # Important
    form_view_form_entry_option_class = 'fi-list'

    # Important
    form_edit_form_entry_option_class = 'fi-page-edit'

    # Important
    form_delete_form_entry_option_class = 'fi-page-delete'

    # Important
    form_list_container_class = 'inline-list'

    # ***********************************************************************
    # ***********************************************************************
    # **************************** Templates ********************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # *************************** Base templates ****************************
    # ***********************************************************************
    master_base_template = 'foundation5/_base.html'
    base_template = 'foundation5/base.html'

    # ***********************************************************************
    # ***************************** Snippets ********************************
    # ***********************************************************************
    form_snippet_template_name = 'foundation5/snippets/form_snippet.html'

    form_properties_snippet_template_name = \
        'foundation5/snippets/form_properties_snippet.html'

    messages_snippet_template_name = \
        'foundation5/snippets/messages_snippet.html'

    form_non_field_and_hidden_errors_snippet_template = \
        'foundation5/snippets/form_non_field_and_hidden_errors_snippet.html'

    form_ajax = 'foundation5/snippets/form_ajax.html'

    form_wizard_ajax = 'foundation5/snippets/form_wizard_ajax.html'  # TODO

    form_wizard_snippet_template_name = \
        'foundation5/snippets/form_wizard_snippet.html'  # TODO

    form_wizard_properties_snippet_template_name = \
        'foundation5/snippets/form_wizard_properties_snippet.html'

    # ***********************************************************************
    # **************************** Form entry CRUD **************************
    # ***********************************************************************
    create_form_entry_template = 'foundation5/create_form_entry.html'
    create_form_entry_ajax_template = \
        'foundation5/create_form_entry_ajax.html'

    edit_form_entry_template = 'foundation5/edit_form_entry.html'
    edit_form_entry_ajax_template = 'foundation5/edit_form_entry_ajax.html'

    form_entry_submitted_template = 'foundation5/form_entry_submitted.html'
    form_entry_submitted_ajax_template = \
        'foundation5/form_entry_submitted_ajax.html'

    view_form_entry_template = 'foundation5/view_form_entry.html'
    view_form_entry_ajax_template = 'foundation5/view_form_entry_ajax.html'

    # ***********************************************************************
    # *********************** Form element entry CUD ************************
    # ***********************************************************************
    add_form_element_entry_template = \
        'foundation5/add_form_element_entry.html'
    add_form_element_entry_ajax_template = \
        'foundation5/add_form_element_entry_ajax.html'

    edit_form_element_entry_template = \
        'foundation5/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = \
        'foundation5/edit_form_element_entry_ajax.html'

    # ***********************************************************************
    # *********************** Form handler entry CUD ************************
    # ***********************************************************************
    add_form_handler_entry_template = \
        'foundation5/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = \
        'foundation5/add_form_handler_entry_ajax.html'

    edit_form_handler_entry_template = \
        'foundation5/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = \
        'foundation5/edit_form_handler_entry_ajax.html'

    # ***********************************************************************
    # ******************* Form wizard handler entry CUD *********************
    # ***********************************************************************

    # ***********************************************************************
    # ***************************** Dashboard *******************************
    # ***********************************************************************
    dashboard_template = 'foundation5/dashboard.html'
    form_wizards_dashboard_template = 'foundation5/form_wizards_dashboard.html'
    forms_list_template = 'foundation5/forms_list.html'

    # ***********************************************************************
    # ************************ Form wizard entry CUD ************************
    # ***********************************************************************
    create_form_wizard_entry_template = \
        'foundation5/create_form_wizard_entry.html'
    create_form_wizard_entry_ajax_template = \
        'foundation5/create_form_wizard_entry_ajax.html'

    edit_form_wizard_entry_template = \
        'foundation5/edit_form_wizard_entry.html'
    edit_form_wizard_entry_ajax_template = \
        'foundation5/edit_form_wizard_entry_ajax.html'

    view_form_wizard_entry_template = \
        'foundation5/view_form_wizard_entry.html'
    view_form_wizard_entry_ajax_template = \
        'foundation5/view_form_wizard_entry_ajax.html'

    # ***********************************************************************
    # ************************* Form importer templates *********************
    # ***********************************************************************

    import_form_entry_template = 'foundation5/import_form_entry.html'
    import_form_entry_ajax_template = \
        'foundation5/import_form_entry_ajax.html'


theme_registry.register(Foundation5Theme)
