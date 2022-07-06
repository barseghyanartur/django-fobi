from django.urls import re_path as url
from django.utils.translation import gettext_lazy as _
from fobi.views.class_based import (
    CreateFormEntryView,
)

__title__ = 'fobi.urls.edit'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

urlpatterns = [
    # ***********************************************************************
    # **************************** Form entry CUD ***************************
    # ***********************************************************************

    # Create form entry
    url(_(r'^forms/create/$'),
        view=CreateFormEntryView.as_view(),
        name='fobi.create_form_entry'),
]