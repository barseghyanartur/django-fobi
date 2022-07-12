from fobi.base import FormCallback, form_callback_registry
from fobi.constants import CALLBACK_FORM_VALID


class SampleFooCallback(FormCallback):
    """SampleFooCallback."""

    stage = CALLBACK_FORM_VALID

    def callback(self, form_entry, request, form):
        """Callback."""
        print("Great! Your form is valid!")


form_callback_registry.register(SampleFooCallback)
