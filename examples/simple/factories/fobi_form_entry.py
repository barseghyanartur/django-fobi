from factory.django import DjangoModelFactory

from .factory_faker import Faker

from fobi.models import FormEntry

__all__ = ("FormEntryFactory",)


class BaseFormEntryFactory(DjangoModelFactory):
    """Factory for creating a site."""

    domain = Faker("domain_name")
    name = Faker("domain_name")

    class Meta(object):
        """Options."""

        model = FormEntry


class FormEntryFactory(BaseFormEntryFactory):
    """Form entry factory."""
