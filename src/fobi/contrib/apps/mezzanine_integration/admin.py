__title__ = 'fobi.contrib.apps.mezzanine_integration.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
#__all__ = ('FobiFormPage',)

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin

from .models import FobiFormPage

admin.site.register(FobiFormPage, PageAdmin)
