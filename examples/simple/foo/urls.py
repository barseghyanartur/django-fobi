from django.conf.urls import url

from foo.views import (
    endpoint as foo_views_endpoint, forms_list as foo_forms_list,
)

urlpatterns = [
    url(r'^endpoint/$', view=foo_views_endpoint, name='foo.endpoint'),
    url(r'^forms-list/$', view=foo_forms_list, name='foo.forms_list'),
]
