from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'quick_start.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', include(admin.site.urls)),

    # DB Store plugin URLs
    path('fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
                #, namespace='fobi'

    # View URLs
    path('fobi/', include('fobi.urls.view')),
                           #, namespace='fobi'

    # Edit URLs
    path('fobi/', include('fobi.urls.edit')),
                           #, namespace='fobi'
]
