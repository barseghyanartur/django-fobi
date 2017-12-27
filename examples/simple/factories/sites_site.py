from factory import DjangoModelFactory

from django.conf import settings
from django.contrib.sites.models import Site

from .factory_faker import Faker

__all__ = ('SiteFactory', 'DefaultSiteFactory',)


class SiteFactory(DjangoModelFactory):
    """Factory for creating a site."""

    domain = Faker('domain_name')
    name = Faker('domain_name')

    class Meta:
        model = Site


class DefaultSiteFactory(SiteFactory):
    """Factory for creating a default site."""

    id = settings.SITE_ID

    class Meta:
        """Meta class."""

        model = Site
        django_get_or_create = ('id',)
