from __future__ import absolute_import, unicode_literals

import os

from django.db import models
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from fobi.integration.processors import IntegrationProcessor

try:
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
    from wagtail.wagtailcore.models import Page
except ImportError: # since wagtail 2.x changes
    from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
    from wagtail.core.models import Page

from .helpers import (
    get_form_template_choices,
    get_success_page_template_choices,
)
from .settings import WIDGET_FORM_SENT_GET_PARAM

__title__ = 'fobi.contrib.apps.wagtail_integration.abstract'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('AbstractFobiFormPage',)


class FobiFormProcessor(IntegrationProcessor):
    """Form processor."""

    can_redirect = True
    form_sent_get_param = WIDGET_FORM_SENT_GET_PARAM

    def get_context_data(self, request, instance, **kwargs):
        """Get context data."""
        context_data = super(FobiFormProcessor, self).get_context_data(
            request,
            instance,
            **kwargs
        )
        page_context_data = instance.get_context(request)
        context_data.update(page_context_data)
        return context_data

    def get_form_template_name(self, request, instance):
        """Get form template name."""
        return instance.get_form_template(request)

    def get_success_page_template_name(self, request, instance):
        """Get success page template name."""
        return instance.get_success_template(request)

    def show_thanks_page(self, request, instance, **kwargs):
        """Render the result of _show_thanks_page().

        Render the result of _show_thanks_page() without having to pass
        through process() (needed to support Wagtail's preview functionality).

        :param django.http.HttpRequest request:
        :return django.http.HttpResponse | None:
        """
        return self._show_thanks_page(request, instance, **kwargs)

    def process(self, request, instance, **kwargs):
        """This is where most of the form handling happens.

        :param django.http.HttpRequest request:
        :return django.http.HttpResponse | NULL:
        """
        return self._process(request, instance, **kwargs)


class AbstractFobiFormPage(Page):
    """An abstract Fobi form page.

    Pages implementing a Fobi form should inherit from it.

    :property fobi.models.FormEntry form_entry: Form entry to be rendered.
    """

    form_entry = models.ForeignKey(
        'fobi.FormEntry',
        verbose_name=_("Form"),
        on_delete=models.PROTECT
    )

    form_template_name = models.CharField(
        _("Form template name"),
        max_length=255,
        null=True,
        blank=True,
        choices=get_form_template_choices(),
        help_text=_(
            "Choose an alternative template to render the form with. Leave "
            "blank to use the default for this page type (e.g. "
            "fobi_form_page.html)."
        )
    )

    hide_form_title = models.BooleanField(
        _("Hide form title"),
        default=False,
        help_text=_("If checked, no form title is shown.")
    )

    form_title = models.CharField(
        _("Form title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Overrides the default form title.")
    )

    form_submit_button_text = models.CharField(
        _("Submit button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Overrides the default form submit button text.")
    )

    success_page_template_name = models.CharField(
        _("Success page template name"),
        max_length=255,
        null=True,
        blank=True,
        choices=get_success_page_template_choices(),
        help_text=_(
            "Choose an alternative template to render the success page with. "
            "Leave blank to use the default for this page type (e.g. "
            "fobi_form_page_success.html)."
        )
    )

    hide_success_page_title = models.BooleanField(
        _("Hide success page title"),
        default=False,
        help_text=_("If checked, no success page title is shown.")
    )

    success_page_title = models.CharField(
        _("Success page title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Overrides the default success page title.")
    )

    success_page_text = models.TextField(
        _("Success page text"),
        null=True,
        blank=True,
        help_text=_("Overrides the default success page text.")
    )

    form_page_panels = [
        FieldPanel('hide_form_title'),
        FieldPanel('form_title'),
        FieldPanel('form_entry'),
        FieldPanel('form_submit_button_text'),
    ]

    if get_form_template_choices():
        form_page_panels.append(FieldPanel('form_template_name'))

    success_page_panels = [
        FieldPanel('hide_success_page_title'),
        FieldPanel('success_page_title'),
        FieldPanel('success_page_text'),
    ]

    if get_success_page_template_choices():
        success_page_panels.append(FieldPanel('success_page_template_name'))

    content_panels = Page.content_panels + [
        MultiFieldPanel(form_page_panels, heading=_('Form page')),
        MultiFieldPanel(success_page_panels, heading=_('Success page')),
    ]

    preview_modes = [
        ('form', _('Form page')),
        ('success', _('Success page')),
    ]

    class Meta(object):
        """Meta options."""

        verbose_name = _('Fobi form page')
        verbose_name_plural = _('Fobi form pages')
        abstract = True

    def __init__(self, *args, **kwargs):
        super(AbstractFobiFormPage, self).__init__(*args, **kwargs)

        # Some wagtail magic...
        if not hasattr(self, 'form_template'):
            name, ext = os.path.splitext(self.template)
            self.form_template = name + '_form' + ext

        if not hasattr(self, 'success_template'):
            name, ext = os.path.splitext(self.template)
            self.success_template = name + '_form_success' + ext

    def get_form_template(self, request):
        """Get an alternative template name.

        Get an alternative template name from the object's
        ``form_template_name`` field, or the ``form_template`` attr defined on
        the page type model.

        :param django.http.HttpRequest request:
        """
        return self.form_template_name or self.form_template

    def get_success_template(self, request):
        """Get an alternative template name.

        Get an alternative template name from the object's
        ``success_page_template_name`` field, or the ``success_template`` attr
        defined on the page type model.

        :param django.http.HttpRequest request:
        """
        return self.success_page_template_name or self.success_template

    def serve(self, request, *args, **kwargs):
        """Serve the page using the ``FobiFormProcessor``."""
        fobi_form_processor = FobiFormProcessor()
        response = fobi_form_processor.process(request, instance=self)

        if response:
            return response

        # TODO: Returning HttpResponse seems dirty. See if it can be
        # replaced with TemplateResponse.
        return HttpResponse(fobi_form_processor.rendered_output)

    def serve_preview(self, request, mode):
        """Serve the page in Wagtail's 'preview' mode."""
        if mode == 'success':
            fobi_form_processor = FobiFormProcessor()

            # TODO: Returning HttpResponse seems dirty. See if it can be
            # replaced with TemplateResponse.
            return HttpResponse(
                fobi_form_processor.show_thanks_page(request, self)
            )
        else:
            return super(AbstractFobiFormPage, self).serve_preview(
                request,
                mode
            )
