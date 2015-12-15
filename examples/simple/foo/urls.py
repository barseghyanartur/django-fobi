from django.conf.urls import url

urlpatterns = [
    url(r'^endpoint/$', view='foo.views.endpoint', name='foo.endpoint'),
    ]
