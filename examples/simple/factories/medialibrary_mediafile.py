from factory import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from feincms.module.medialibrary.models import MediaFile

from .factory_faker import Faker

__all__ = (
    'ImageMediaFileFactory',
    'MediaFileFactory',
    'TextMediaFileFactory',
    'VideoMediaFileFactory',
)


class MediaFileFactory(DjangoModelFactory):
    """MediaFile factory."""

    file = Faker('django_file')
    type = FuzzyChoice(
        [
            'image',
            'video',
            'pdf',
            'audio',
            'swf',
            'txt',
            'rtf',
            'zip',
            'doc',
            'xls',
            'ppt',
            'other',
        ]
    )
    created = Faker('date_time_ad')
    copyright = Faker('name')
    file_size = Faker('pyint')

    class Meta(object):
        """Meta options."""

        model = MediaFile


class VideoMediaFileFactory(MediaFileFactory):
    """Video."""

    file = Faker('django_file', extension='video')
    type = 'video'


class ImageMediaFileFactory(MediaFileFactory):
    """Image."""

    file = Faker('django_file', extension='image')
    type = 'image'


class TextMediaFileFactory(MediaFileFactory):
    """Text."""

    file = Faker('django_file', extension='text')
    type = 'txt'
