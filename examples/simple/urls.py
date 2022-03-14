from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from fobi.settings import DEFAULT_THEME

from django_nine import versions

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

url_patterns_args = [
    # DB Store plugin URLs
    # namespace='fobi'
    path('fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    path('fobi/plugins/form-wizard-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls.'
                'form_wizard_handlers')),

    # django-fobi URLs:
    # namespace='fobi'
    path('fobi/', include('fobi.urls.view')),
    # namespace='fobi'
    re_path(r'^{0}fobi/'.format(FOBI_EDIT_URLS_PREFIX),
        include('fobi.urls.edit')),

    path('admin_tools/', include('admin_tools.urls')),

    path('login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='auth_login'),
]

if versions.DJANGO_GTE_2_0:
    url_patterns_args += [
        path('admin/', admin.site.urls),
    ]
else:
    url_patterns_args += [
        path('admin/', include(admin.site.urls)),
    ]

url_patterns_args += [
    # django-registration URLs:
    path('accounts/', include('django_registration.backends.one_step.urls' if versions.DJANGO_GTE_3_0 else 'registration.backends.simple.urls')),

    # foo URLs:
    path('foo/', include('foo.urls')),

    # bar URLs:
    # url(r'^bar/', include('bar.urls')),

    path('', TemplateView.as_view(template_name=fobi_home_template)),

    # django-fobi public forms contrib app:
    # url(r'^', include('fobi.contrib.apps.public_forms.urls')),
]

urlpatterns += i18n_patterns(*url_patterns_args)

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
    url_patterns_args = [
        path('pages/', include('feincms.urls')),
    ]
    urlpatterns += i18n_patterns(*url_patterns_args)

# # Conditionally include django-markdownx
# if 'markdownx' in settings.INSTALLED_APPS:
#     url_patterns_args = [
#         url(r'^markdownx/', include('markdownx.urls')),
#     ]
#     urlpatterns += list(url_patterns_args)

if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    url_patterns_args = [
        path('ckeditor/', include('ckeditor_uploader.urls')),
    ]
    urlpatterns += i18n_patterns(*url_patterns_args)

# Conditionally including DjangoCMS URls in case if
# DjangoCMS in installed apps.
if 'cms' in settings.INSTALLED_APPS:
    url_patterns_args = [
        path('cms-pages/', include('cms.urls')),
    ]
    urlpatterns += i18n_patterns(*url_patterns_args)

# Conditionally including Django REST framework integration app
if 'fobi.contrib.apps.drf_integration' in settings.INSTALLED_APPS:
    from fobi.contrib.apps.drf_integration.urls import fobi_router
    urlpatterns += [
        path('api/', include(fobi_router.urls))
    ]

# Conditionally including Captcha URls in case if
# Captcha in installed apps.
if getattr(settings, 'ENABLE_CAPTCHA', False):
    try:
        from captcha.fields import ReCaptchaField
    except ImportError:
        try:
            from captcha.fields import CaptchaField
            if 'captcha' in settings.INSTALLED_APPS:
                urlpatterns += [
                    path('captcha/', include('captcha.urls')),
                ]
        except ImportError:
            pass

if (
    getattr(settings, 'DEBUG', False)
    and getattr(settings, 'DEBUG_TOOLBAR', False)
):
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
