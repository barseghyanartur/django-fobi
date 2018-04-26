from django.utils.translation import ugettext_lazy as _

from fobi.base import theme_registry

from fobi.contrib.themes.bootstrap3.fobi_themes import Bootstrap3Theme

from . import UID

__title__ = 'fobi.contrib.themes.class_based_views.apps'
__author__ = 'Kyle Roux <jstacoder@gmail.com>'
__license__ = 'GPL 2.0/LGPL 2.1'
__copyright__ = '2018 Kyle Roux'
__all__ = ('ClassBasedViewsTheme',)

class ClassBasedViewsTheme(Bootstrap3Theme):
  """ ClassBasedViewsTheme """

  uid = UID
  name = _("Class Based Views")

  dashboard = 'fobi.class_based.dashboard'
  form_wizards_dashboard = 'fobi.class_based.form_wizards_dashboard'
  create_form_entry = 'fobi.class_based.create_form_entry'
  edit_form_entry = 'fobi.class_based.edit_form_entry'
  create_form_wizard_entry = 'fobi.class_based.create_form_wizard_entry'
  edit_form_wizard_entry =  'fobi.class_based.edit_form_wizard_entry'
  add_form_element_entry = 'fobi.class_based.add_form_element_entry'

theme_registry.register(ClassBasedViewsTheme)