from factory import DjangoModelFactory

from fobi.models import FormEntry

from .factory_faker import Faker

__all__ = ('FormEntryFactory',)


class BaseFormEntryFactory(DjangoModelFactory):
    """Factory for creating a site."""

    domain = Faker('domain_name')
    name = Faker('domain_name')

    class Meta(object):
        """Options."""

        model = FormEntry


class FormEntryFactory(BaseFormEntryFactory):
    """Form entry factory."""
