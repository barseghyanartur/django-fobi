from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from .views import my_view

urlpatterns = [
    url(_(r'^$'), my_view, name='bar.my_view'),
]
