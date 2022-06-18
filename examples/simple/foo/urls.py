from django.urls import path

from .views import (
    endpoint as foo_views_endpoint,
    forms_list as foo_forms_list
)

__all__ = ('urlpatterns',)


urlpatterns = [
    path('endpoint/', view=foo_views_endpoint, name='foo.endpoint'),
    path('forms-list/', view=foo_forms_list, name='foo.forms_list'),
]
