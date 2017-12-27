import logging

from django.utils.text import slugify

from factory import (
    DjangoModelFactory,
    LazyAttribute,
    SubFactory,
    post_generation,
)
from factory.fuzzy import FuzzyChoice

from fobi.tests.helpers import create_form_with_entries

from page.models import Page

from .factory_faker import Faker

logger = logging.getLogger(__name__)

__all__ = (
    'TEMPLATE_KEYS',
    'PageFactory',
    'FobiFormPageFactory',
)

TEMPLATE_DEFAULT = 'page/base.html'

TEMPLATE_KEYS = (
    TEMPLATE_DEFAULT,
)


class BasePageFactory(DjangoModelFactory):
    """Base page factory."""

    title = Faker('text', max_nb_chars=200)
    slug = LazyAttribute(lambda __x: slugify(__x.title))
    active = True
    in_navigation = FuzzyChoice([True, False])
    template_key = FuzzyChoice(TEMPLATE_KEYS)
    # show_in_footer = FuzzyChoice([True, False])

    class Meta(object):
        """Meta class."""

        model = Page
        abstract = True


class PageFactory(BasePageFactory):
    """Page factory."""


class HomePageFactory(BasePageFactory):
    """Home page factory."""

    override_url = '/'
    title = "Home"
    slug = "home"

    class Meta(object):
        """Meta class."""

        model = Page
        django_get_or_create = ('slug',)


class FobiFormPageFactory(BasePageFactory):
    """Fobi form page factory."""

    title = "Fobi form"
    slug = "fobi-form"

    class Meta(object):
        """Meta class."""

        model = Page
        django_get_or_create = ('slug',)

    @post_generation
    def fobi_form_content(obj, created, extracted, **kwargs):
        """Create fobi content for the instance created."""

        if created:
            form_entry = create_form_with_entries(is_public=True)
            obj.content.item.fobiformwidget_set.model.objects.create(
                parent=obj,
                region='main',
                form_entry=form_entry
            )
