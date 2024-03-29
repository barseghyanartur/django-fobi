from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ("MyUser",)


class MyUser(AbstractUser):
    """My user."""

    date_of_birth = models.DateField(null=True, blank=True)
