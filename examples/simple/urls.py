from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from fobi.settings import DEFAULT_THEME

admin.autodiscover()

# Mapping.
fobi_theme_home_template_mapping = {
    'bootstrap3': 'home/bootstrap3.html',
    'foundation5': 'home/foundation5.html',
    'simple': 'home/simple.html',
}

# Get the template to be used.
fobi_home_template = fobi_theme_home_template_mapping.get(
    DEFAULT_THEME,
    'home/base.html'
)

FOBI_EDIT_URLS_PREFIX = ''
if DEFAULT_THEME in ('simple', 'djangocms_admin_style_theme'):
    FOBI_EDIT_URLS_PREFIX = 'admin/'

urlpatterns = []

urlpatterns += i18n_patterns(
    # DB Store plugin URLs
    # namespace='fobi'
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    url(r'^fobi/plugins/form-wizard-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls.'
                'form_wizard_handlers')),

    # django-fobi URLs:
    # namespace='fobi'
    url(r'^fobi/', include('fobi.urls.view')),
    # namespace='fobi'
    url(r'^{0}fobi/'.format(FOBI_EDIT_URLS_PREFIX),
        include('fobi.urls.edit')),

    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # django-registration URLs:
    url(r'^accounts/', include('registration.backends.default.urls')),

    # foo URLs:
    url(r'^foo/', include('foo.urls')),

    url(r'^$', TemplateView.as_view(template_name=fobi_home_template)),

    # django-fobi public forms contrib app:
    # url(r'^', include('fobi.contrib.apps.public_forms.urls')),
)

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Conditionally including FeinCMS URls in case if
# FeinCMS in installed apps.
if 'feincms' in settings.INSTALLED_APPS:
    from page.models import Page
    Page
    urlpatterns += i18n_patterns(
        url(r'^pages/', include('feincms.urls')),

    )

# Conditionally including DjangoCMS URls in case if
# DjangoCMS in installed apps.
if 'cms' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns(
        url(r'^cms-pages/', include('cms.urls')),
    )

# Conditionally including Captcha URls in case if
# Captcha in installed apps.
try:
    from captcha.fields import ReCaptchaField
except ImportError as e:
    if 'captcha' in settings.INSTALLED_APPS:
        urlpatterns += [
            url(r'^captcha/', include('captcha.urls')),
        ]
