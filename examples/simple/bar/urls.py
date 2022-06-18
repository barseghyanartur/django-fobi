from django.urls import include, re_path
from django.utils.translation import gettext_lazy as _

from .views import my_view

urlpatterns = [
    re_path(_(r'^$'), my_view, name='bar.my_view'),
]
