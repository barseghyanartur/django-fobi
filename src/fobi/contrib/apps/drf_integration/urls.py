from rest_framework.routers import DefaultRouter
from rest_framework import VERSION
from .views import FobiFormEntryViewSet

__title__ = 'fobi.contrib.apps.drf_integration.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'urlpatterns',
    'fobi_router',
)

DRF_VERSION = [int(_v) for _v in VERSION.split('.')]
basename = 'basename'
if DRF_VERSION[:2] < [3, 10]:
    basename = 'base_name'

router_kwargs = {basename: 'fobi_form_entry'}

fobi_router = DefaultRouter()
fobi_router.register(
    r'fobi-form-entry',
    FobiFormEntryViewSet,
    **router_kwargs
)
urlpatterns = fobi_router.urls
