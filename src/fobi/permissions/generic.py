"""
Provides a set of pluggable permission policies.

Inspired by Django REST Framework class-based permissions.

`BasePermissions` forbids everything by default.
"""

__title__ = "fobi.permissions.generic"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "SAFE_METHODS",
    "OperationHolderMixin",
    "SingleOperandHolder",
    "AND",
    "OR",
    "NOT",
    "BasePermissionMetaclass",
    "BasePermission",
    "AllowAnyPermission",
    "DenyAnyPermission",
    "IsAuthenticatedPermission",
    "IsAdminUserPermission",
    "IsAuthenticatedOrReadOnlyPermission",
    "IsSuperUserPermission",
)

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class OperationHolderMixin:
    def __and__(self, other):
        return OperandHolder(AND, self, other)

    def __or__(self, other):
        return OperandHolder(OR, self, other)

    def __rand__(self, other):
        return OperandHolder(AND, other, self)

    def __ror__(self, other):
        return OperandHolder(OR, other, self)

    def __invert__(self):
        return SingleOperandHolder(NOT, self)


class SingleOperandHolder(OperationHolderMixin):
    def __init__(self, operator_class, op1_class):
        self.operator_class = operator_class
        self.op1_class = op1_class

    def __call__(self, *args, **kwargs):
        op1 = self.op1_class(*args, **kwargs)
        return self.operator_class(op1)


class OperandHolder(OperationHolderMixin):
    def __init__(self, operator_class, op1_class, op2_class):
        self.operator_class = operator_class
        self.op1_class = op1_class
        self.op2_class = op2_class

    def __call__(self, *args, **kwargs):
        op1 = self.op1_class(*args, **kwargs)
        op2 = self.op2_class(*args, **kwargs)
        return self.operator_class(op1, op2)


class AND:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def has_permission(self, request, view):
        return self.op1.has_permission(
            request, view
        ) and self.op2.has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return self.op1.has_object_permission(
            request, view, obj
        ) and self.op2.has_object_permission(request, view, obj)


class OR:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def has_permission(self, request, view):
        return self.op1.has_permission(
            request, view
        ) or self.op2.has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return self.op1.has_object_permission(
            request, view, obj
        ) or self.op2.has_object_permission(request, view, obj)


class NOT:
    def __init__(self, op1):
        self.op1 = op1

    def has_permission(self, request, view):
        return not self.op1.has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return not self.op1.has_object_permission(request, view, obj)


class BasePermissionMetaclass(OperationHolderMixin, type):
    pass


class BasePermission(metaclass=BasePermissionMetaclass):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return False


class AllowAnyPermission(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class DenyAnyPermission(BasePermission):
    """
    Deny any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


class IsAuthenticatedPermission(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAdminUserPermission(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsSuperUserPermission(BasePermission):
    """
    Allows access only to super-users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAuthenticatedOrReadOnlyPermission(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
