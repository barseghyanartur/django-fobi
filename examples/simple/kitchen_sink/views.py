from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy

from .forms import KitchenSinkForm


class KitchenSinkFormView(FormView):
    template_name = "kitchen_sink/kitchen_sink.html"
    form_class = KitchenSinkForm

    def get_success_url(self):
        return f"{reverse('kitchen_sink')}?success"
