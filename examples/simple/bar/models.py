from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    class MPTTMeta:
        #level_attr = 'mptt_level'
        order_insertion_by=['name']

    def __unicode__(self):
        return self.name
