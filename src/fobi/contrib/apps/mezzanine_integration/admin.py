from django.contrib import admin

from mezzanine.pages.admin import PageAdmin

from .models import FobiFormPage

__title__ = 'fobi.contrib.apps.mezzanine_integration.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'


admin.site.register(FobiFormPage, PageAdmin)
