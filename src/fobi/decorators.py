from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

SATISFY_ANY = 'any'
SATISFY_ALL = 'all'
DEFAULT_SATISFY = SATISFY_ALL


__title__ = 'fobi.decorators'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'SATISFY_ANY',
    'SATISFY_ALL',
    'DEFAULT_SATISFY',
    'permissions_required',
    'all_permissions_required',
    'any_permission_required',
)


def permissions_required(perms, satisfy=DEFAULT_SATISFY, login_url=None,
                         raise_exception=False):
    """Check for the permissions given based on the strategy chosen.

    :param iterable perms:
    :param string satisfy: Allowed values are "all" and "any".
    :param string login_url:
    :param bool raise_exception: If set to True, the ``PermissionDenied``
        exception is raised on failures.
    :return bool:

    :example:
    >>> @login_required
    >>> @permissions_required(satisfy='any', perms=[
    >>>     'fobi.add_formentry',
    >>>     'fobi.change_formentry',
    >>>     'fobi.delete_formentry',
    >>>     'fobi.add_formelemententry',
    >>>     'fobi.change_formelemententry',
    >>>     'fobi.delete_formelemententry',
    >>> ])
    >>> def edit_dashboard(request):
    >>>     # your code
    """
    assert satisfy in (SATISFY_ANY, SATISFY_ALL)

    if SATISFY_ALL == satisfy:
        # ``SATISFY_ALL`` case
        def check_perms(user):
            # First check if the user has the permission (even anon users)
            if user.has_perms(perms):
                return True
            # In case the 403 handler should be called raise the exception
            if raise_exception:
                raise PermissionDenied
            # As the last resort, show the login form
            return False
    else:
        # ``SATISFY_ANY`` case
        def check_perms(user):
            # First check if the user has the permission (even anon users)
            for perm in perms:
                if user.has_perm(perm):
                    return True

            # In case the 403 handler should be called raise the exception
            if raise_exception:
                raise PermissionDenied
            # As the last resort, show the login form
            return False

    return user_passes_test(check_perms, login_url=login_url)


def all_permissions_required(perms, login_url=None, raise_exception=False):
    """Check for the permissions given based on SATISFY_ALL strategy chosen.

    :example:
    >>> @login_required
    >>> @all_permissions_required([
    >>>     'fobi.add_formentry',
    >>>     'fobi.change_formentry',
    >>>     'fobi.delete_formentry',
    >>>     'fobi.add_formelemententry',
    >>>     'fobi.change_formelemententry',
    >>>     'fobi.delete_formelemententry',
    >>> ])
    >>> def edit_dashboard(request):
    >>>     # your code
    """
    return permissions_required(perms, satisfy=SATISFY_ALL,
                                login_url=login_url,
                                raise_exception=raise_exception)


def any_permission_required(perms, login_url=None, raise_exception=False):
    """Check for the permissions given based on SATISFY_ANY strategy chosen.

    :example:
    >>> @login_required
    >>> @any_permission_required([
    >>>     'fobi.add_formentry',
    >>>     'fobi.change_formentry',
    >>>     'fobi.delete_formentry',
    >>>     'fobi.add_formelemententry',
    >>>     'fobi.change_formelemententry',
    >>>     'fobi.delete_formelemententry',
    >>> ])
    >>> def edit_dashboard(request):
    >>>     # your code
    """
    return permissions_required(perms, satisfy=SATISFY_ANY,
                                login_url=login_url,
                                raise_exception=raise_exception)
