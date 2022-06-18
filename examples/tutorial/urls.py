from django.urls import include, path

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django_nine import versions

from fobi.settings import DEFAULT_THEME

admin.autodiscover()

# Mapping.
fobi_theme_home_template_mapping = {
    'bootstrap3': 'home/bootstrap3.html',
    'foundation5': 'home/foundation5.html',
}

# Get the template to be used.
fobi_home_template = fobi_theme_home_template_mapping.get(
    DEFAULT_THEME,
    'home/base.html'
    )

urlpatterns = [
    # DB Store plugin URLs
    path('fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
                #, namespace='fobi'

    # django-fobi URLs:
    path('fobi/', include('fobi.urls')), #, namespace='fobi'

    path('admin_tools/', include('admin_tools.urls')),

    path('admin/', include(admin.site.urls)),

    # django-registration URLs:
    path('accounts/', include('django_registration.backends.one_step.urls' if versions.DJANGO_GTE_3_0 else 'registration.backends.simple.urls')),

    # foo URLs:
    path('foo/', include('foo.urls')),

    path('', TemplateView.as_view(template_name=fobi_home_template)),

    # django-fobi public forms contrib app:
    #url(r'^', include('fobi.contrib.apps.public_forms.urls')),
]

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Conditionally including FeinCMS URls in case if
# FeinCMS in installed apps.
if 'feincms' in settings.INSTALLED_APPS:
    from page.models import Page
    Page
    urlpatterns += [
        path('', include('feincms.urls')),
    ]
