from ..decorators import DEFAULT_SATISFY, SATISFY_ALL, SATISFY_ANY
from .definitions import (
    add_form_element_entry_permission,
    add_form_handler_entry_permission,
    add_form_wizard_form_entry_permission,
    add_form_wizard_handler_entry_permission,
    create_form_entry_permissions,
    create_form_wizard_entry_permissions,
    dashboard_permissions,
    delete_form_element_entry_permission,
    delete_form_entry_permissions,
    delete_form_handler_entry_permission,
    delete_form_wizard_entry_permissions,
    delete_form_wizard_form_entry_permission,
    delete_form_wizard_handler_entry_permission,
    edit_form_element_entry_permission,
    edit_form_entry_permissions,
    edit_form_handler_entry_permission,
    edit_form_wizard_entry_permissions,
    edit_form_wizard_handler_entry_permission,
    wizards_dashboard_permissions,
)
from .generic import BasePermission

__title__ = "fobi.permissions.default"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "permissions_required_func",
    "all_permissions_required_func",
    "any_permission_required_func",
    "CreateFormEntryPermission",
    "EditFormEntryPermission",
)


def login_required(request) -> bool:
    return bool(request.user and request.user.is_authenticated)


def permissions_required_func(perms, satisfy=DEFAULT_SATISFY) -> callable:
    assert satisfy in (SATISFY_ANY, SATISFY_ALL)

    if SATISFY_ALL == satisfy:
        # ``SATISFY_ALL`` case
        def check_perms(user):
            # First check if the user has the permission (even anon users)
            if user.has_perms(perms):
                return True
            # As the last resort, show the login form
            return False

    else:
        # ``SATISFY_ANY`` case
        def check_perms(user):
            # First check if the user has the permission (even anon users)
            for perm in perms:
                if user.has_perm(perm):
                    return True

            # As the last resort, show the login form
            return False

    return check_perms


def all_permissions_required_func(perms) -> callable:
    """Check for the permissions given based on the strategy chosen.

    :param iterable perms:
    :return bool:
    """
    return permissions_required_func(perms, satisfy=SATISFY_ALL)


def any_permission_required_func(perms) -> callable:
    """Check for the permissions given based on the strategy chosen.

    :param iterable perms:
    :return bool:
    """
    return permissions_required_func(perms, satisfy=SATISFY_ANY)


class CreateFormEntryPermission(BasePermission):
    """Permission to create form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and all_permissions_required_func(
            create_form_entry_permissions
        )(request.user)


class EditFormEntryPermission(BasePermission):
    """Permission to edit form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and any_permission_required_func(
            edit_form_entry_permissions
        )(request.user)
