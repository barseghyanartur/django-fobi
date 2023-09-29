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
        "bootstrap5/css/bootstrap5_fobi_extras.css",
        # "css/fobi.core.css",
    )

    media_js = (
        "bootstrap5/js/bootstrap.min.js",
        "js/jquery-1.10.2.min.js",
        "js/jquery.slugify.js",
        "js/fobi.core.js",
        "bootstrap5/js/bootstrap5_fobi_extras.js",  # Theme-specific scripts
    )

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

    messages_snippet_template_name = "bootstrap3/snippets/messages_snippet.html"

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

    edit_form_entry_template = "bootstrap3/edit_form_entry.html"
    edit_form_entry_ajax_template = "bootstrap3/edit_form_entry_ajax.html"

    form_entry_submitted_template = "bootstrap3/form_entry_submitted.html"
    form_entry_submitted_ajax_template = (
        "bootstrap3/form_entry_submitted_ajax.html"
    )

    embed_form_entry_submitted_ajax_template = (
        "bootstrap3/embed_form_entry_submitted_ajax.html"
    )

    view_form_entry_template = "bootstrap3/view_form_entry.html"
    view_form_entry_ajax_template = "bootstrap3/view_form_entry_ajax.html"

    view_embed_form_entry_ajax_template = (
        "bootstrap3/view_embed_form_entry_ajax.html"
    )

    def __init__(self, user=None):
        """Constructor."""
        super(Bootstrap5Theme, self).__init__(user=user)
    
    # ***********************************************************************
    # ***************************** Dashboard *******************************
    # ***********************************************************************
    dashboard_template = "bootstrap5/dashboard.html"
    form_wizards_dashboard_template = "bootstrap3/form_wizards_dashboard.html"
    forms_list_template = "bootstrap3/forms_list.html"


theme_registry.register(Bootstrap5Theme)