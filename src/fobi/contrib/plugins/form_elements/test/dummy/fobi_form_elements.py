__title__ = 'fobi.contrib.plugins.form_elements.test.dummy.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DummyPlugin',)

from uuid import uuid4

from django.utils.translation import ugettext, ugettext_lazy as _

from nonefield.fields import NoneField

from fobi.base import FormElementPlugin, form_element_plugin_registry
from fobi.helpers import safe_text

from . import UID

class DummyPlugin(FormElementPlugin):
    """
    Dummy plugin.
    """
    uid = UID
    name = _("Dummy")
    group = _("Testing")

    def post_processor(self):
        """
        Always the same.
        """
        self.data.name = "{0}_{1}".format(self.uid, uuid4())

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        kwargs = {
            'initial': "<p>{0}</p>".format(safe_text(ugettext("Dummy content"))),
            'required': False,
            'label': '',
        }

        form_field_instances = []

        form_field_instances.append((self.data.name, NoneField, kwargs))
        return form_field_instances


form_element_plugin_registry.register(DummyPlugin)
