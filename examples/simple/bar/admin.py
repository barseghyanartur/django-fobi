from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Genre

admin.site.register(Genre, MPTTModelAdmin)
