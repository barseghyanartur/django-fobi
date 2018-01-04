from .....form_importers import form_importer_plugin_registry
from .base import MailChimpImporter

__title__ = 'fobi.contrib.plugins.form_importers.mailchimp_importer.' \
            'fobi_form_importers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailChimpImporter',)


form_importer_plugin_registry.register(MailChimpImporter)
