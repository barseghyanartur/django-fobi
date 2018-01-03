from __future__ import absolute_import

from uuid import uuid4

from django.utils.translation import ugettext, ugettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin
from fobi.helpers import safe_text

from . import UID

__title__ = 'fobi.contrib.plugins.form_elements.test.dummy.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DummyPlugin',)


class DummyPlugin(FormElementPlugin):
    """Dummy plugin."""

    uid = UID
    name = _("Dummy")
    group = _("Testing")

    def post_processor(self):
        """Post process data.

        Always the same.
        """
        self.data.name = "{0}_{1}".format(self.uid, uuid4())

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        field_kwargs = {
            'initial': "<p>{0}</p>".format(
                safe_text(ugettext("Dummy content"))
            ),
            'required': False,
            'label': '',
        }

        return[(self.data.name, NoneField, field_kwargs)]
