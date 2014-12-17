def disable_admin_tools(request):
    """
    Disable admin tools.
    """
    return {'ADMIN_TOOLS_DISABLED': True}
