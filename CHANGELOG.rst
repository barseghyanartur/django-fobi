Release history and notes
=====================================
0.3
-------------------------------------
2014-11-09

Note, that this release contains minor backwards incompatible changes. The
changed do not anyhow affect your existing forms or data. The only thing you
need to do is update the app paths in the ``settings`` module of your project.

- Minor core improvements related to the themeing of the form handler plugins.
- Several presentational form element plugins have been renamed.
  The ``fobi.contrib.plugins.form_elements.content.image`` plugin has been
  renamed to `fobi.contrib.plugins.form_elements.content.content_image`.
  The ``fobi.contrib.plugins.form_elements.content.text`` plugin has been
  renamed to ``fobi.contrib.plugins.form_elements.content.content_text``.
  The ``fobi.contrib.plugins.form_elements.content.video`` plugin has been
  renamed to ``fobi.contrib.plugins.form_elements.content.content_video``.
  If you have used any of the above mentioned plugins, make sure to update 
  the app paths in the ``settings`` module of your project.
- The ``fobi.contrib.plugins.form_elements.content.dummy`` plugin has been moved
  to ``fobi.contrib.plugins.form_elements.text.dummy`` location. If you have
  used it, make sure to update the its' path in the ``settings`` module of
  your project.
- Added readme to the following content form element plugins: ``dummy``,
  ``content_image``, ``content_text`` and ``content_video``.
- Added ``foundation5`` and ``simple`` theme widgets for ``db_store`` plugin.
- If you have been overriding the defaults of the ``db_store`` plugin, change
  the prefix from ``FOBI_PLUGIN_DB_EXPORT_`` to ``FOBI_PLUGIN_DB_STORE_``. For
  example,  ``FOBI_PLUGIN_DB_EXPORT_CSV_DELIMITER`` should become
  ``FOBI_PLUGIN_DB_STORE_CSV_DELIMITER``.
- Mentioning the ``fobi_find_broken_entries`` management command in the
  documentation, as well as improving the management command itself (more
  verbose output).
- Birthday field added.

0.2.1
-------------------------------------
2014-11-06

- Minor improvements of the ``db_store`` plugin.
- Minor improvements of the ``simple`` theme. Make sure that custom
  form handler actions are properly shown in the form handlers list.
- Make it possible to fail silently on missing form element or form
  handler plugins by setting the respected values to False: 
  ``FOBI_FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS``,
  ``FOBI_FAIL_ON_MISSING_FORM_HANDLER_PLUGINS``. Otherwise an appropriate
  exception is raised.

0.2
-------------------------------------
2014-11-05

Note, that this release contains minor backwards incompatible changes.

- Minor (backwards incompatible) changes in the form handler plugin API. 
  From now on both ``custom_actions`` and ``get_custom_actions`` methods
  accept ``form_entry`` (obligatory) and ``request`` (optional) arguments. If
  you have written your own or have changed existing form handler plugins
  with use of one of the above mentioned methods, append those arguments to
  the method declarations when upgrading to this version. If you haven't
  written your own or changed existing form handler plugins, you may just 
  upgrade to this version.
- Added data export features to the ``db_store`` plugin.
- Minor fixes in ``db_store`` plugin.
- Added missing documentation for the ``feincms_integration`` app.
- Updated translations for Dutch and Russian.

0.1.6
-------------------------------------
2014-10-25

- Minor improvements in the theming API. From now on the
  ``view_embed_form_entry_ajax_template`` template would be used
  when integrating the form rendering from other products (for example,
  a CMS page, which has a widget which references the form object. If
  that property is left empty, the ``view_form_entry_ajax_template``
  is used. For a success page the ``embed_form_entry_submitted_ajax_template``
  template would be used.
- Functional improvements of the FeinCMS integration (the widget). If you
  have used the FeinCMS widget of earlier versions, you likely want to update 
  to this one. From now on you can select a custom form title and the button
  text, as well as provide custom success page title and the success  message;
  additionally, it has been made possible to hide the form- or success-page-
  titles.

0.1.5
-------------------------------------
2014-10-23

- Minor fixes in the ``Integer`` form element plugin.
- Minor fixes in the ``Input`` form element plugin.
- Minor fixes in themes (disable HTML5 form validation in edit mode).
- Minor documentation improvements.

0.1.4
-------------------------------------
2014-10-22

- Minor core improvements.
- Django 1.5 support improvements.
- Django 1.7 support improvements.
- Added ``Captcha`` form element plugin.
- Added highly-customisable ``Input`` form element plugin - a custom input field
  with support for almost any ever existing HTML attribute.
- Documentation improvements.

0.1.3
-------------------------------------
2014-10-13

- Django 1.7 support.
- Add HTML5 "placeholder" field attribute support.

0.1.2
-------------------------------------
2014-10-11

- Simple theme fixes: Fix for making the theme work in Django 1.5.

0.1.1
-------------------------------------
2014-10-11

- Bootstrap 3 theme fixes: When tab pane has no or little content so
  that the height of the dropdown menu exceeds the height of the tab pane
  content the dropdown menu now becomes scrollable (vertically).

0.1
-------------------------------------
2014-10-11

- Initial release.
