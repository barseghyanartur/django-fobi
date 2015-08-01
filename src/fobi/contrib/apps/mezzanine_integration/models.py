__title__ = 'fobi.contrib.apps.mezzanine_integration.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiFormPage',)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

from .helpers import (
    get_form_template_choices, get_success_page_template_choices
    )

class FobiFormPage(Page, RichText):
    """
    Widget for to Mezzanine.

    :property fobi.models.FormEntry form_entry: Form entry to be rendered.
    :property str template: If given used for rendering the form.
    """
    form_entry = models.ForeignKey('fobi.FormEntry', verbose_name=_("Form"))

    form_template_name = models.CharField(
        _("Form template name"), max_length=255, null=True, blank=True,
        choices=get_form_template_choices(),
        help_text=_("Template to render the form with.")
        )

    hide_form_title = models.BooleanField(
        _("Hide form title"), default=False,
        help_text=_("If checked, no form title is shown.")
        )

    form_title = models.CharField(
        _("Form title"), max_length=255, null=True, blank=True,
        help_text=_("Overrides the default form title.")
        )

    form_submit_button_text = models.CharField(
        _("Submit button text"), max_length=255, null=True, blank=True,
        help_text=_("Overrides the default form submit button text.")
        )

    success_page_template_name = models.CharField(
        _("Success page template name"), max_length=255, null=True, blank=True,
        choices=get_success_page_template_choices(),
        help_text=_("Template to render the success page with.")
        )

    hide_success_page_title = models.BooleanField(
        _("Hide success page title"), default=False,
        help_text=_("If checked, no success page title is shown.")
        )

    success_page_title = models.CharField(
        _("Succes page title"), max_length=255, null=True, blank=True,
        help_text=_("Overrides the default success page title.")
        )

    success_page_text = models.TextField(
        _("Succes page text"), null=True, blank=True,
        help_text=_("Overrides the default success page text.")
        )

    class Meta:
        app_label = 'fobi'
        verbose_name = _("Fobi form")
        verbose_name_plural = _("Fobi forms")
        #db_table = 'fobi_fobiformpage'

    def __unicode__(self):
        return _('Fobi form')
