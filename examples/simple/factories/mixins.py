import datetime
import random

from django.utils.text import slugify

from factory import DjangoModelFactory, LazyAttribute
from factory.fuzzy import FuzzyChoice

from .factory_faker import Faker

__all__ = (
    'FeincmsBaseMixinFactory',
    'TimeStampedMixinFactory',
    'SortableMixinFactory',
    'PublishedContentMixinFactory',
    'OrderedContentMixinFactory',
    'ContentMixinFactory',
)


class FeincmsBaseMixinFactory(DjangoModelFactory):
    """FeincmsBaseMixinFactory."""

    class Meta(object):
        """Meta class."""

        abstract = True


class TimeStampedMixinFactory(DjangoModelFactory):
    """Mixin for time stamped model."""

    created_date = Faker('date_time')
    modified_date = LazyAttribute(
        lambda __x: __x.created_date + datetime.timedelta(
            days=random.randint(1, 100)
        )
    )
    publish_date = datetime.datetime.now() - datetime.timedelta(days=1)

    class Meta(object):
        """Meta class."""

        abstract = True


class SortableMixinFactory(DjangoModelFactory):
    """Sortable mixin factory."""

    order = Faker('pyint')

    class Meta(object):
        """Meta class."""

        abstract = True


class PublishedContentMixinFactory(DjangoModelFactory):
    """Published content mixin."""

    # published = FuzzyChoice([True, False])
    published = True

    class Meta(object):
        """Meta class."""

        abstract = True


class OrderedContentMixinFactory(DjangoModelFactory):
    """Ordered content mixin."""

    order = 0

    class Meta(object):
        """Meta class."""

        abstract = True


class BaseContentMixinFactory(FeincmsBaseMixinFactory,
                              TimeStampedMixinFactory,
                              PublishedContentMixinFactory):
    """BaseContentMixinFactory."""

    title = Faker('text', max_nb_chars=100)
    slug = LazyAttribute(lambda obj: slugify(obj.title)[:100])

    class Meta(object):
        """Meta class."""

        abstract = True


class DjangoContentMixinFactory(DjangoModelFactory):
    """DjangoContentMixinFactory."""

    class Meta(object):
        """Meta class."""

        abstract = True


class ContentMixinFactory(BaseContentMixinFactory,
                          DjangoContentMixinFactory):
    """ContentMixinFactory."""

    class Meta(object):
        """Meta class."""

        abstract = True
