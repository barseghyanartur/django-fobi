from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import CreateView

from ..base import get_theme
from ..forms import FormEntryForm

__all__ = ("CreateFormEntryView",)


class CreateFormEntryView(CreateView):
    """Create form entry view."""

    template_name = None
    form_class = FormEntryForm
    theme = None

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        if self.theme:
            context.update({"fobi_theme": self.theme})
        return context

    def get_template_names(self):
        """Get template names."""
        template_name = self.template_name
        if not template_name:
            if not self.theme:
                theme = get_theme(request=self.request, as_instance=True)
            template_name = theme.create_form_entry_template
        return [template_name]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        self.object = None
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form_entry = form.save(commit=False)
            form_entry.user = request.user
            try:
                form_entry.save()
                messages.info(
                    request,
                    _("Form {0} was created successfully.").format(
                        form_entry.name
                    ),
                )
                return redirect(
                    "fobi.edit_form_entry", form_entry_id=form_entry.pk
                )
            except IntegrityError as err:
                messages.info(
                    request,
                    _("Errors occurred while saving the form: {0}.").format(
                        str(err)
                    ),
                )

        return self.render_to_response(self.get_context_data())

    def post_hook(self, form_entry):
        """Post hook."""
