__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.fobi_themes'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DjangoCMSAdminStyleTheme',)

from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseTheme, theme_registry

from . import UID

class DjangoCMSAdminStyleTheme(BaseTheme):
    """
    A theme that has a native ``djangocms-admin-style`` style.
    """
    uid = UID
    name = _("DjangoCMS admin style")

    media_css = (
        #'admin/css/base.css',
        #'admin/css/forms.css',
        #'admin/css/widgets.css',
        'djangocms_admin_style_theme/css/fobi.djangocms_admin_style_theme.css',
        'jquery-ui/css/smoothness/jquery-ui-1.10.3.custom.min.css',
        #'admin_tools/css/menu.css', # TODO at least a conditional insert
    )

    media_js = (
        'js/jquery-1.10.2.min.js',
        'jquery-ui/js/jquery-ui-1.10.4.custom.min.js',
        'js/jquery.slugify.js',
        'js/fobi.core.js',
        #'js/fobi.simple.js',
    )

    #footer_text = '&copy; django-fobi example site 2014'

    # *************************************************************************
    # ********************** Form HTML specific *******************************
    # *************************************************************************
    form_element_html_class = 'vTextField'
    form_radio_element_html_class = 'radiolist'
    form_element_checkbox_html_class = 'checkbox'

    # Important
    form_edit_form_entry_option_class = 'edit'

    # Important
    form_delete_form_entry_option_class = 'deletelink'

    # Important
    form_list_container_class = 'list-inline'

    # *************************************************************************
    # ********************** Templates specific *******************************
    # *************************************************************************
    master_base_template = 'djangocms_admin_style_theme/_base.html'
    base_template = 'djangocms_admin_style_theme/base.html'
    base_view_template = 'djangocms_admin_style_theme/base_view.html'
    base_edit_template = 'djangocms_admin_style_theme/base_edit.html'

    form_ajax = 'djangocms_admin_style_theme/snippets/form_ajax.html'
    form_snippet_template_name = 'djangocms_admin_style_theme/snippets/form_snippet.html'
    form_view_snippet_template_name = 'djangocms_admin_style_theme/snippets/form_view_snippet.html'
    form_edit_ajax = 'djangocms_admin_style_theme/snippets/form_edit_ajax.html'
    form_edit_snippet_template_name = 'djangocms_admin_style_theme/snippets/form_edit_snippet.html'
    form_properties_snippet_template_name = 'djangocms_admin_style_theme/snippets/form_properties_snippet.html'
    messages_snippet_template_name = 'djangocms_admin_style_theme/snippets/messages_snippet.html'

    add_form_element_entry_template = 'djangocms_admin_style_theme/add_form_element_entry.html'
    add_form_element_entry_ajax_template = 'djangocms_admin_style_theme/add_form_element_entry_ajax.html'

    add_form_handler_entry_template = 'djangocms_admin_style_theme/add_form_handler_entry.html'
    add_form_handler_entry_ajax_template = 'djangocms_admin_style_theme/add_form_handler_entry_ajax.html'

    create_form_entry_template = 'djangocms_admin_style_theme/create_form_entry.html'
    create_form_entry_ajax_template = 'djangocms_admin_style_theme/create_form_entry_ajax.html'

    dashboard_template = 'djangocms_admin_style_theme/dashboard.html'

    edit_form_element_entry_template = 'djangocms_admin_style_theme/edit_form_element_entry.html'
    edit_form_element_entry_ajax_template = 'djangocms_admin_style_theme/edit_form_element_entry_ajax.html'

    edit_form_entry_template = 'djangocms_admin_style_theme/edit_form_entry.html'
    edit_form_entry_ajax_template = 'djangocms_admin_style_theme/edit_form_entry_ajax.html'

    edit_form_handler_entry_template = 'djangocms_admin_style_theme/edit_form_handler_entry.html'
    edit_form_handler_entry_ajax_template = 'djangocms_admin_style_theme/edit_form_handler_entry_ajax.html'

    form_entry_submitted_template = 'djangocms_admin_style_theme/form_entry_submitted.html'
    form_entry_submitted_ajax_template = 'djangocms_admin_style_theme/form_entry_submitted_ajax.html'

    view_form_entry_template = 'djangocms_admin_style_theme/view_form_entry.html'
    view_form_entry_ajax_template = 'djangocms_admin_style_theme/view_form_entry_ajax.html'

    import_form_entry_template = 'djangocms_admin_style_theme/import_form_entry.html'
    import_form_entry_ajax_template = 'djangocms_admin_style_theme/import_form_entry_ajax.html'

    @classmethod
    def edit_form_entry_edit_option_html(cls):
        """
        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
            <li><a href="{edit_url}" class="{edit_option_class}">
              <span>{edit_text}</span></a>
            </li>
            """.format(
                edit_url = "{edit_url}",
                edit_option_class = cls.form_edit_form_entry_option_class,
                edit_text = "{edit_text}",
                )

    @classmethod
    def edit_form_entry_help_text_extra(cls):
        """
        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
            <ul class="{container_class}">
              {edit_option_html}
              <li><a href="{delete_url}" class="{delete_option_class}">
                <span>{delete_text}</span></a>
              </li>
            </ul>
            <input type="hidden" value="{form_element_position}"
                   name="form-{counter}-position"
                   id="id_form-{counter}-position"
                   class="form-element-position">
            <input type="hidden" value="{form_element_pk}"
                   name="form-{counter}-id" id="id_form-{counter}-id">
            """.format(
                container_class = cls.form_list_container_class,
                edit_option_html = "{edit_option_html}",
                delete_url = "{delete_url}",
                delete_option_class = cls.form_delete_form_entry_option_class,
                delete_text = "{delete_text}",
                form_element_position = "{form_element_position}",
                counter = "{counter}",
                form_element_pk = "{form_element_pk}",
                )


theme_registry.register(DjangoCMSAdminStyleTheme)
