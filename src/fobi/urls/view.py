__title__ = 'fobi.urls.view'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

from django.conf.urls import url #patterns, include
from django.utils.translation import ugettext_lazy as _
from fobi.views import (
    form_entry_submitted, view_form_entry, form_entry_submitted
    )

#urlpatterns = patterns('fobi.views',
urlpatterns = [
    # Form submitted success page
    url(_(r'^view/submitted/$'),
        view=form_entry_submitted,
        name='fobi.form_entry_submitted'),

    # View form entry
    url(_(r'^view/(?P<form_entry_slug>[\w_\-]+)/$'),
        view_form_entry,
        name='fobi.view_form_entry'),

    # Form submitted success page
    url(_(r'^view/(?P<form_entry_slug>[\w_\-]+)/submitted/$'),
        view=form_entry_submitted,
        name='fobi.form_entry_submitted'),
#)
]
