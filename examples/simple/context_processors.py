from django.conf import settings

__all__ = ('disable_admin_tools', 'testing',)


def disable_admin_tools(request):
    """Disable admin tools."""
    return {'ADMIN_TOOLS_DISABLED': True}


def testing(request):
    """Put `testing` into context."""
    return {'testing': settings.TESTING}
