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
from .generic import (
    AllowAnyPermission,
    BasePermission,
    IsAuthenticatedPermission,
)
from .helpers import (
    all_permissions_required_func,
    any_permission_required_func,
    login_required,
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
    "AddFormHandlerEntryPermission",
    "EditFormHandlerEntryPermission",
    "DeleteFormHandlerEntryPermission",
    "ViewFormEntryPermission",
    "ViewDashboardPermission",
)


class CreateFormEntryPermission(BasePermission):
    """Permission to create form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and all_permissions_required_func(
            create_form_entry_permissions
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return self.has_permission(request, view)


class EditFormEntryPermission(BasePermission):
    """Permission to edit form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and any_permission_required_func(
            edit_form_entry_permissions
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and any_permission_required_func(edit_form_entry_permissions)(
                request.user
            )
            and obj.user == request.user
        )


class DeleteFormEntryPermission(BasePermission):
    """Permission to delete form entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and all_permissions_required_func(
            delete_form_entry_permissions
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and any_permission_required_func(delete_form_entry_permissions)(
                request.user
            )
            and obj.user == request.user
        )


class AddFormElementEntryPermission(BasePermission):
    """Permission to add form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            add_form_element_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return self.has_permission(request, view)


class EditFormElementEntryPermission(BasePermission):
    """Permission to edit form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            edit_form_element_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and permissions_required_func(edit_form_element_entry_permission)(
                request.user
            )
            and obj.form_entry.user == request.user
        )


class DeleteFormElementEntryPermission(BasePermission):
    """Permission to delete form element entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            delete_form_element_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and permissions_required_func(delete_form_element_entry_permission)(
                request.user
            )
            and obj.form_entry.user == request.user
        )


class AddFormHandlerEntryPermission(BasePermission):
    """Permission to add form handler entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            add_form_handler_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return self.has_permission(request, view)


class EditFormHandlerEntryPermission(BasePermission):
    """Permission to edit form handler entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            edit_form_handler_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and permissions_required_func(edit_form_handler_entry_permission)(
                request.user
            )
            and obj.form_entry.user == request.user
        )


class DeleteFormHandlerEntryPermission(BasePermission):
    """Permission to delete form handler entries."""

    def has_permission(self, request, view) -> bool:
        return login_required(request) and permissions_required_func(
            delete_form_handler_entry_permission
        )(request.user)

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            login_required(request)
            and permissions_required_func(delete_form_handler_entry_permission)(
                request.user
            )
            and obj.form_entry.user == request.user
        )


class ViewFormEntryPermission(AllowAnyPermission):
    """Permission to view form entries."""


class ViewDashboardPermission(IsAuthenticatedPermission):
    """Permission to view the dashboard."""
