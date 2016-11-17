"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'admin_tools_dashboard.menu.CustomMenu'
"""

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu

from . import conf

__all__ = ('CustomMenu',)


class CustomMenu(Menu):
    """Custom Menu."""

    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
        ]

        # Foo
        self.children.append(
            items.ModelList(
                _('Foo'),
                models=conf.foo_apps
            )
        )

        # Fobi
        self.children.append(
            items.MenuItem(
                _('Fobi'),
                children=[
                    items.ModelList(_('Plugins'), models=conf.fobi_plugins),
                    items.ModelList(_('Forms'), models=conf.fobi_forms),
                    items.ModelList(_('Data'), models=conf.fobi_data),
                ]
            )
        )

        if 'feincms' in settings.INSTALLED_APPS:
            # FeinCMS pages integration
            self.children.append(
                items.AppList(
                    _('FeinCMS Pages'),
                    models=conf.feincms_pages
                )
            )

        if 'cms' in settings.INSTALLED_APPS:
            # DjangoCMS pages integration
            self.children.append(
                items.AppList(
                    _('DjangoCMS Pages'),
                    models=conf.djangocms_pages
                )
            )

        # append an app list module for "Administration"
        self.children.append(
            items.AppList(
                _('Administration'),
                models=['django.contrib.*']
            )
        )

    def init_with_context(self, context):
        """Use this method if you need to access the request context."""
        return super(CustomMenu, self).init_with_context(context)
