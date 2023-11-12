from django.urls import path
from .views import KitchenSinkFormView

urlpatterns = [
    path("", KitchenSinkFormView.as_view(), name="kitchen_sink"),
]
