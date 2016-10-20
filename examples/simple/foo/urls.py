from django.conf.urls import url

from .views import (
    endpoint as foo_views_endpoint,
    forms_list as foo_forms_list
)

__all__ = ('urlpatterns',)


urlpatterns = [
    url(r'^endpoint/$', view=foo_views_endpoint, name='foo.endpoint'),
    url(r'^forms-list/$', view=foo_forms_list, name='foo.forms_list'),
]
