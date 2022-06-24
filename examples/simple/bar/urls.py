from django.urls import include, re_path as url
from django.utils.translation import gettext_lazy as _

from .views import my_view

urlpatterns = [
    url(_(r'^$'), my_view, name='bar.my_view'),
]
