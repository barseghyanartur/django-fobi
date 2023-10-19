from django.utils.translation import gettext_lazy as _

from fobi.base import BaseTheme, theme_registry

from . import UID

__title__ = "fobi.contrib.themes.bootstrap5.theme"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("Bootstrap5Theme",)


class Bootstrap5Theme(BaseTheme):
    """Bootstrap5 theme."""

    uid = UID
    name = _("Bootstrap 5")

    media_css = (
        "bootstrap5/css/bootstrap.min.css",
        "bootstrap5/css/bootstrap-icons.min.css",
        # "bootstrap5/css/bootstrap5_fobi_extras.css",
        # "css/fobi.core.css",
    )

    media_js = (
        "bootstrap5/js/bootstrap.bundle.min.js",
        "js/jquery-1.10.2.min.js",
        "js/jquery.slugify.js",
        "js/fobi.core.js",
        # "bootstrap5/js/bootstrap5_fobi_extras.js",  # Theme-specific scripts
    )

    # ***********************************************************************
    # ***********************************************************************
    # ********************** Form HTML specific *****************************
    # ***********************************************************************
    # ***********************************************************************
    form_element_html_class = "form-control"
    form_element_checkbox_html_class = "form-check-input"

    # Important!
    form_view_form_entry_option_class = "bi bi-list"

    # Important!
    form_edit_form_entry_option_class = "bi bi-pencil"

    # Important!
    form_delete_form_entry_option_class = "bi bi-trash"

    # Important!
    form_list_container_class = "btn-group"

    # ***********************************************************************
    # ***********************************************************************
    # **************************** Templates ********************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # *************************** Base templates ****************************
    # ***********************************************************************
    master_base_template = "bootstrap5/_base.html"
    base_template = "bootstrap5/base.html"

    # ***********************************************************************
    # ***************************** Snippets ********************************
    # ***********************************************************************
    form_snippet_template_name = "bootstrap5/snippets/form_snippet.html"

    form_properties_snippet_template_name = (
        "bootstrap5/snippets/form_properties_snippet.html"
    )

    messages_snippet_template_name = "bootstrap5/snippets/messages_snippet.html"

    form_non_field_and_hidden_errors_snippet_template = (
        "bootstrap5/snippets/form_non_field_and_hidden_errors_snippet.html"
    )

    form_ajax = "bootstrap5/snippets/form_ajax.html"

    form_wizard_ajax = "bootstrap5/snippets/form_wizard_ajax.html"

    form_wizard_snippet_template_name = (
        "bootstrap5/snippets/form_wizard_snippet.html"
    )

    form_wizard_properties_snippet_template_name = (
        "bootstrap5/snippets/form_wizard_properties_snippet.html"
    )

    # ***********************************************************************
    # **************************** Form entry CRUD **************************
    # ***********************************************************************
    create_form_entry_template = "bootstrap5/create_form_entry.html"
    create_form_entry_ajax_template = "bootstrap3/create_form_entry_ajax.html"

    edit_form_entry_template = "bootstrap5/edit_form_entry.html"
    edit_form_entry_ajax_template = "bootstrap5/edit_form_entry_ajax.html"

    form_entry_submitted_template = "bootstrap5/form_entry_submitted.html"
    form_entry_submitted_ajax_template = (
        "bootstrap5/form_entry_submitted_ajax.html"
    )

    embed_form_entry_submitted_ajax_template = (
        "bootstrap3/embed_form_entry_submitted_ajax.html"
    )

    view_form_entry_template = "bootstrap5/view_form_entry.html"
    view_form_entry_ajax_template = "bootstrap3/view_form_entry_ajax.html"

    view_embed_form_entry_ajax_template = (
        "bootstrap3/view_embed_form_entry_ajax.html"
    )

    # ***********************************************************************
    # *********************** Edit form element entry ***********************
    # ***********************************************************************
    edit_form_element_entry_template = (
        "bootstrap5/edit_form_element_entry.html"
    )
    edit_form_element_entry_ajax_template = (
        "bootstrap5/edit_form_element_entry_ajax.html"
    )

    # ***********************************************************************
    # ***************************** Dashboard *******************************
    # ***********************************************************************
    dashboard_template = "bootstrap5/dashboard.html"
    form_wizards_dashboard_template = "bootstrap5/form_wizards_dashboard.html"
    forms_list_template = "bootstrap3/forms_list.html"

    # ***********************************************************************
    # ************************ Form wizard entry CUD ************************
    # ***********************************************************************
    create_form_wizard_entry_template = (
        "bootstrap5/create_form_wizard_entry.html"
    )
    create_form_wizard_entry_ajax_template = (
        "bootstrap5/create_form_wizard_entry_ajax.html"
    )

    edit_form_wizard_entry_template = "bootstrap5/edit_form_wizard_entry.html"
    edit_form_wizard_entry_ajax_template = (
        "bootstrap5/edit_form_wizard_entry_ajax.html"
    )

    view_form_wizard_entry_template = "bootstrap5/view_form_wizard_entry.html"
    view_form_wizard_entry_ajax_template = (
        "bootstrap5/view_form_wizard_entry_ajax.html"
    )

    def __init__(self, user=None):
        """Constructor."""
        super(Bootstrap5Theme, self).__init__(user=user)
    

    @classmethod
    def edit_form_entry_edit_option_html(cls):
        """Edit FormEntry edit option HTML.

        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
        <a class="btn btn-outline-secondary btn-sm" href="{edit_url}">
          <i class="{edit_option_class}"></i> {edit_text}
        </a>
        """.format(
            edit_url="{edit_url}",
            edit_option_class=cls.form_edit_form_entry_option_class,
            edit_text="{edit_text}",
        )


    @classmethod
    def edit_form_entry_help_text_extra(cls):
        """Edit FormEntry help_text extra.

        For adding the edit link to edit form entry view.

        :return str:
        """
        return """
        <div class="{container_class}">
          {edit_option_html}
          <a class="btn btn-outline-secondary btn-sm" href="{delete_url}">
            <i class="{delete_option_class}"></i> {delete_text}
          </a>
        </div>
        <input type="hidden" value="{form_element_position}"
               name="form-{counter}-position"
               id="id_form-{counter}-position"
               class="form-element-position">
        <input type="hidden" value="{form_element_pk}"
               name="form-{counter}-id" id="id_form-{counter}-id">
        """.format(
            container_class=cls.form_list_container_class,
            edit_option_html="{edit_option_html}",
            delete_url="{delete_url}",
            delete_option_class=cls.form_delete_form_entry_option_class,
            delete_text="{delete_text}",
            form_element_position="{form_element_position}",
            counter="{counter}",
            form_element_pk="{form_element_pk}",
        )


theme_registry.register(Bootstrap5Theme)