from fobi.constants import CALLBACK_FORM_VALID
from fobi.base import FormCallback, form_callback_registry

class SampleFooCallback(FormCallback):
    stage = CALLBACK_FORM_VALID

    def callback(self, form_entry, request, form):
        print("Great! Your form is valid!")

form_callback_registry.register(SampleFooCallback)
