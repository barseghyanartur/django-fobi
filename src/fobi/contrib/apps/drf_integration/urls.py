from rest_framework.routers import DefaultRouter

from .views import FobiFormEntryViewSet

__title__ = 'fobi.contrib.apps.drf_integration.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'urlpatterns',
    'fobi_router',
)

fobi_router = DefaultRouter()
fobi_router.register(
    r'fobi-form-entry',
    FobiFormEntryViewSet,
    base_name='fobi_form_entry'
)
urlpatterns = fobi_router.urls
