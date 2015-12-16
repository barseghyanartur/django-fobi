from django.conf.urls import url

from foo.views import endpoint as foo_views_endpoint

urlpatterns = [
    url(r'^endpoint/$', view=foo_views_endpoint, name='foo.endpoint'),
]
