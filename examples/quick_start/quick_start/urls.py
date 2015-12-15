from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'quick_start.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
                #, namespace='fobi'

    # View URLs
    url(r'^fobi/', include('fobi.urls.view')),
                           #, namespace='fobi'

    # Edit URLs
    url(r'^fobi/', include('fobi.urls.edit')),
                           #, namespace='fobi'
]
