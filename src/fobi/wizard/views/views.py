from formtools.wizard.views import (
    WizardView as OriginalWizardView,
    SessionWizardView as OriginalSessionWizardView,
    CookieWizardView as OriginalCookieWizardView,

)

__all__ = (
    'WizardView',
    'SessionWizardView',
    'CookieWizardView',
)


class PatchGetMixin(object):
    """Patch GET mixin."""

    def _patched_get(self, request, *args, **kwargs):
        # TODO: Don't know if I should leave it like this. Perhaps, just
        # never reset on this step.
        if self.storage.current_step == self.steps.first:
            self.storage.reset()

        # reset the current step to the first step.
        self.storage.current_step = self.steps.first
        return self.render(self.get_form())


class WizardView(OriginalWizardView, PatchGetMixin):
    """Patched version of the original WizardView."""

    def get(self, request, *args, **kwargs):
        """GET requests.

        This method handles GET requests.

        If a GET request reaches this point, the wizard assumes that the user
        just starts at the first step or wants to restart the process.
        The data of the wizard will be resetted before rendering the first
        step.
        """
        return self._patched_get(request, *args, **kwargs)


class SessionWizardView(OriginalSessionWizardView, PatchGetMixin):
    """A WizardView with pre-configured SessionStorage backend."""

    def get(self, request, *args, **kwargs):
        """GET requests.

        This method handles GET requests.

        If a GET request reaches this point, the wizard assumes that the user
        just starts at the first step or wants to restart the process.
        The data of the wizard will be resetted before rendering the first
        step.
        """
        return self._patched_get(request, *args, **kwargs)


class CookieWizardView(OriginalCookieWizardView, PatchGetMixin):
    """A WizardView with pre-configured CookieStorage backend."""

    def get(self, request, *args, **kwargs):
        """GET requests.

        This method handles GET requests.

        If a GET request reaches this point, the wizard assumes that the user
        just starts at the first step or wants to restart the process.
        The data of the wizard will be resetted before rendering the first
        step.
        """
        return self._patched_get(request, *args, **kwargs)
