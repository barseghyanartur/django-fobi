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
from .helpers import (
    login_required,
    all_permissions_required_func,
    any_permission_required_func,
    permissions_required_func,
)

__title__ = "fobi.permissions.default"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "CreateFormEntryPermission",
    "EditFormEntryPermission",
    "DeleteFormEntryPermission",
    "AddFormElementEntryPermission",
    "EditFormElementEntryPermission",
    "DeleteFormElementEntryPermission",
)


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


class DeleteFormEntryPermission(BasePermission):
    """Permission to delete form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and all_permissions_required_func(
            delete_form_entry_permissions
        )(request.user)


class AddFormElementEntryPermission(BasePermission):
    """Permission to add form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            add_form_element_entry_permission
        )(request.user)


class EditFormElementEntryPermission(BasePermission):
    """Permission to edit form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            edit_form_element_entry_permission
        )(request.user)


class DeleteFormElementEntryPermission(BasePermission):
    """Permission to delete form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            delete_form_element_entry_permission
        )(request.user)
