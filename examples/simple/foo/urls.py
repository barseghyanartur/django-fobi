from django.conf.urls import patterns, url

urlpatterns = patterns('foo.views',
    url(r'^endpoint/$', view='endpoint', name='foo.endpoint'),
    )
