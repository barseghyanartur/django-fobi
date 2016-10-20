from django.db import models

__all__ = ('FileTest',)


class FileTest(models.Model):
    """File test."""

    file = models.FileField(upload_to='foo/')
