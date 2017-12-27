from django.conf import settings

from factory import (
    DjangoModelFactory, PostGenerationMethodCall, Sequence
)

from .factory_faker import Faker

__all__ = (
    'TEST_USERNAME',
    'TEST_PASSWORD',
    'AbstractUserFactory',
    'InactiveUserFactory',
    'UserFactory',
    'StaffUserFactory',
    'SuperuserUserFactory',
    'SuperAdminUserFactory',
    'TestUsernameSuperAdminUserFactory',
)

TEST_USERNAME = 'test_user'
TEST_PASSWORD = 'test_password'


class AbstractUserFactory(DjangoModelFactory):
    """Abstract factory for creating users."""

    password = PostGenerationMethodCall('set_password', TEST_PASSWORD)
    username = Sequence(lambda n: 'user%d' % n)
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')

    is_active = False
    is_staff = False
    is_superuser = False

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)
        abstract = True


class InactiveUserFactory(AbstractUserFactory):
    """Factory for creating inactive users."""


class UserFactory(AbstractUserFactory):
    """Factory for creating active users."""

    is_active = True


class StaffUserFactory(UserFactory):
    """Factory for creating staff (admin) users."""

    is_staff = True


class SuperuserUserFactory(UserFactory):
    """Factory for creating superuser users."""

    is_superuser = True


class SuperAdminUserFactory(UserFactory):
    """Factory for creating super admin users."""

    is_staff = True
    is_superuser = True


class TestUsernameSuperAdminUserFactory(UserFactory):
    """Factory for creating super admin user test_user."""

    username = TEST_USERNAME
    is_staff = True
    is_superuser = True
