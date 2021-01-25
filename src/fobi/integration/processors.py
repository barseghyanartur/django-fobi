from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from ..base import (
    fire_form_callbacks,
    get_theme,
    run_form_handlers,
    submit_plugin_form_data,
)
from ..constants import (
    CALLBACK_BEFORE_FORM_VALIDATION,
    CALLBACK_FORM_INVALID,
    CALLBACK_FORM_VALID,
    CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
    CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
)
from ..dynamic import assemble_form_class
from ..exceptions import ImproperlyConfigured
from ..settings import GET_PARAM_INITIAL_DATA

__title__ = 'fobi.integration.processors'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IntegrationProcessor',)


class IntegrationProcessor(object):
    """Generic integration processor.

    :param str form_sent_get_param:
    :param bool can_redirect: If set to True, if not authenticated
        an attempt to redirect user to a login page would be made. Otherwise,
        a message about authentication would be generated instead (in place
        of the form). Some content management systems, like Django-CMS, aren't
        able to redirect on plugin level. For those systems, the value
        of ``can_redirect`` should be set to False.
    :param str login_required_template_name: Template to be used for
        rendering the login required message. This is only important when
        ``login_required_redirect`` is set to False.
    """

    can_redirect = True
    form_sent_get_param = 'sent'
    login_required_template_name = 'fobi/integration/login_required.html'

    def integration_check(self, instance):
        """Integration check.

        Performs a simple check to identify whether the model instance
        has been implemented according to the expectations.
        """
        expected_fields = (
            ('form_entry', 'models.ForeignKey("fobi.FormEntry)'),
            ('form_template_name', 'models.CharField'),
            ('hide_form_title', 'models.BooleanField'),
            ('form_title', 'models.CharField'),
            ('form_submit_button_text', 'models.CharField'),
            ('success_page_template_name', 'models.CharField'),
            ('hide_success_page_title', 'models.BooleanField'),
            ('success_page_title', 'models.CharField'),
            ('success_page_text', 'models.CharField'),
        )

        for field_name, field_info in expected_fields:
            if not hasattr(instance, field_name):
                raise ImproperlyConfigured(
                    "You should have a field {0} in your {1} model "
                    "({2})".format(field_name, field_info, type(instance))
                )

    def get_context_data(self, request, instance, **kwargs):
        """Get context data."""
        context = {
            'form_entry': instance.form_entry,
        }
        context.update(kwargs)
        return context

    def get_form_template_name(self, request, instance):
        """Get form template name."""
        return instance.form_template_name or None

    def get_success_page_template_name(self, request, instance):
        """Get succes page template name."""
        return instance.success_page_template_name or None

    def get_login_required_template_name(self, request, instance):
        """Get login required template name."""
        return self.login_required_template_name or None

    def get_process_form_redirect_url(self, request, instance):
        """Get process form redirect URL (success).

        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry instance:
        :return str:
        """
        return "{0}?{1}={2}".format(
            request.path,
            self.form_sent_get_param,
            instance.form_entry.slug
        )

    def _process_form(self, request, instance, **kwargs):
        """Process form.

        Handle the form if no "sent" GET argument (see the
        ``WIDGET_FORM_SENT_GET_PARAM`` setting).

        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry instance: FormEntry instance.
        :return django.http.HttpResponse | str:
        """
        template_name = self.get_form_template_name(request, instance)

        user_is_authenticated = request.user.is_authenticated

        # Handle public/non-public forms. If form requires user authentication
        # redirect to login form with next parameter set to current request
        # path.
        if not user_is_authenticated \
                and not instance.form_entry.is_public:
            if self.can_redirect:
                return redirect(
                    "{0}?next={1}".format(settings.LOGIN_URL, request.path)
                )
            else:
                return self._show_login_required_page(
                    request, instance, **kwargs
                )

        form_element_entries = instance.form_entry.formelemententry_set.all(
        )[:]
        # This is where the most of the magic happens. Our form is being built
        # dynamically.
        form_cls = assemble_form_class(
            instance.form_entry,
            form_element_entries=form_element_entries,
            request=request
        )

        if request.method == 'POST':
            form = form_cls(request.POST, request.FILES)

            # Fire pre form validation callbacks
            fire_form_callbacks(
                form_entry=instance.form_entry,
                request=request,
                form=form,
                stage=CALLBACK_BEFORE_FORM_VALIDATION
            )

            if form.is_valid():
                # Fire form valid callbacks, before handling submitted plugin
                # form data
                form = fire_form_callbacks(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form,
                    stage=CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA
                )

                # Fire plugin processors
                form = submit_plugin_form_data(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form
                )

                # Fire form valid callbacks
                form = fire_form_callbacks(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form,
                    stage=CALLBACK_FORM_VALID
                )

                # Run all handlers
                run_form_handlers(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form
                )

                # Fire post handler callbacks
                fire_form_callbacks(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form,
                    stage=CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS
                )

                messages.info(
                    request,
                    _('Form {0} was submitted '
                      'successfully.').format(instance.form_entry.name)
                )

                if self.can_redirect:
                    return redirect(
                        self.get_process_form_redirect_url(request, instance)
                    )
                else:
                    return self._show_thanks_page(request, instance, **kwargs)

            else:
                # Fire post form validation callbacks
                fire_form_callbacks(
                    form_entry=instance.form_entry,
                    request=request,
                    form=form,
                    stage=CALLBACK_FORM_INVALID
                )

        else:
            # Providing initial form data by feeding entire GET dictionary
            # to the form, if ``GET_PARAM_INITIAL_DATA`` is present in the
            # GET.
            kwargs = {}
            if GET_PARAM_INITIAL_DATA in request.GET:
                kwargs = {'initial': request.GET}
            form = form_cls(**kwargs)

        theme = get_theme(request=request, as_instance=True)
        theme.collect_plugin_media(form_element_entries)

        form_title = instance.form_title \
            if instance.form_title \
            else instance.form_entry.title

        context = self.get_context_data(
            request=request,
            instance=instance,
            form=form,
            fobi_theme=theme,
            fobi_form_title=form_title,
            fobi_hide_form_title=instance.hide_form_title,
            fobi_form_submit_button_text=instance.form_submit_button_text
        )

        if not template_name:
            template_name = theme.view_embed_form_entry_ajax_template

        render_kwargs = {
            'template_name': template_name,
            'context': context,
            'request': request,
        }

        self.rendered_output = render_to_string(**render_kwargs)

    def _show_login_required_page(self, request, instance, **kwargs):
        """Displays text with login required.

        :param django.http.HttpRequest request:
        :return django.http.HttpResponse | str:
        """
        context = self.get_context_data(
            request=request,
            instance=instance,
            login_url="{0}?next={1}".format(settings.LOGIN_URL, request.path),
        )
        template_name = self.get_login_required_template_name(request,
                                                              instance)

        render_kwargs = {
            'template_name': template_name,
            'context': context,
            'request': request,
        }

        return render_to_string(**render_kwargs)

    def _show_thanks_page(self, request, instance, **kwargs):
        """Render the thanks page after successful form submission.

        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry instance: FormEntry instance.
        :return str:
        """
        template_name = self.get_success_page_template_name(request, instance)

        theme = get_theme(request=request, as_instance=True)

        context = self.get_context_data(
            request=request,
            instance=instance,
            fobi_theme=theme,
            fobi_hide_success_page_title=instance.hide_success_page_title,
            fobi_success_page_title=instance.success_page_title,
            fobi_success_page_text=instance.success_page_text,
        )

        if not template_name:
            template_name = theme.embed_form_entry_submitted_ajax_template

        render_kwargs = {
            'template_name': template_name,
            'context': context,
            'request': request,
        }

        self.rendered_output = render_to_string(**render_kwargs)

    def _process(self, request, instance, **kwargs):
        """This is where most of the form handling happens.

        :param django.http.HttpRequest request:
        :param fobi.models.FormEntry instance: FormEntry instance.
        :return django.http.HttpResponse | str:
        """
        self.integration_check(instance)

        if self.form_sent_get_param in request.GET:
            return self._show_thanks_page(request, instance, **kwargs)
        else:
            return self._process_form(request, instance, **kwargs)
