from six import python_2_unicode_compatible

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

__all__ = ('Genre',)


@python_2_unicode_compatible
class Genre(MPTTModel):
    """Genre."""

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    class MPTTMeta:
        """MPTT meta."""

        # level_attr = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
