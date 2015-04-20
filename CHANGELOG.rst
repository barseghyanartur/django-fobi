Release history and notes
=====================================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.5.1
-------------------------------------
2015-04-21

- DateTime picker widget added for Bootstrap 3 theme for `datetime` and `date`
  plugins.

0.5
-------------------------------------
2015-04-06

Note, that this release contains minor backwards incompatible changes. The
changes may affect your existing forms and data. Read the notes below
carefully.

- Fixed previously wrongly labeled (in `AppConf`) add-ons/plugins
  (`fobi.contrib.plugins.form_handlers.db_store`,
  `fobi.contrib.apps.feincms_integration`,
  `fobi.contrib.apps.djangocms_integration`,
  `fobi.contrib.apps.mezzanine_integration`). Due to the change, you would
  likely have to to rename a couple of database tables and update referencies
  accordingly. No migrations to solve the issue are included at the moment.

0.4.36
-------------------------------------
2015-04-03

- Handle non-ASCII characters content_text form element.

0.4.35
-------------------------------------
2015-03-28

- Fixed the issue with `allow_multiple` working incorrectly for form handler
  plugins. Fix the `db_store` plugin as well.

0.4.34
-------------------------------------
2015-03-27

- Minor fixes in the `Checkbox select multiple` and `Radio` plugins.
- Minified tox tests.

0.4.33
-------------------------------------
2015-03-26

- `Checkbox select multiple
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/checkbox_select_multiple>`_
  field added.
- Minor improvements (styling) in the Foundation 5 theme.
- Initial configuration for tox tests.
- Clean up requirements (for example setups and tests).

0.4.32
-------------------------------------
2015-03-25

- Updated missing parts in the Russian translations.
- Minor API improvements. From now on, the `run` method of form handlers
  may return a tuple (bool, mixed). In case of errors it might be (False, err).
- Minor code clean ups.

0.4.31
-------------------------------------
2015-03-23

- When path of the uploaded file (plugins) doesn't yet exist, create it,
  instaid of failing.

0.4.30
-------------------------------------
2015-03-23

- From now on submitted files are sent as attachments in the mail plugin.
- Documentation improvements. Adding information of rendering forms using
  `django-crispy-forms` or alternatives.
- Minor fixes.

0.4.29
-------------------------------------
2015-03-20

- `Decimal
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/decimal>`_
  field added.
- `Float
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/float>`_
  field added.
- `Slug
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/slug>`_
  field added.
- `IP address
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/ip_address>`_
  field added.
- `Null boolean
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/null_boolean>`_
  field added.
- `Time
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/time>`_
  field added.
- From now on using `simplejson` package in favour of `json`, since it can
  handle decimal data.
- Minor improvements of the date plugins (`datetime`, `date`).

0.4.28
-------------------------------------
2015-03-13

- Fix improperly picked configurations of the 
  `fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects`
  plugin.
- Long identifiers of models can now be safely used in foreign key plugins
  (such as
  `fobi.contrib.plugins.form_elements.fields.select_model_object_plugin` and
  `fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects`
  plugins).
- Fixed admin bulk change of the plugins.
- From now it's possible to have some control/configure the following plugins
  for the submitted value:

      * fobi.contrib.plugins.form_elements.fields.select_model_object
      * fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects

  The only thing needs to be done is to specify the appropriate variable
  in the settings module of the project (settings.py).

      * FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_SUBMIT_VALUE_AS
      * FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MODEL_OBJECTS_SUBMIT_VALUE_AS

  Allowed values are: "val", "repr", "mix".

0.4.27
-------------------------------------
2015-03-12

- Temporary allow the `fobi.contrib.plugins.form_handlers.db_store` plugin to 
  be used multiple times per form, until the bug with not being able to assign
  the `db_store` plugin to the form due to incorrect handling of restrictions
  (``allow_multiple``) introduced in previous version is properly fixed.
- From now it's possible to have some control/configure the following plugins 
  for the submitted value:

      * fobi.contrib.plugins.form_elements.fields.radio
      * fobi.contrib.plugins.form_elements.fields.select
      * fobi.contrib.plugins.form_elements.fields.select_multiple

  The only thing needs to be done is to specify the appropriate variable
  in the settings module of the project (settings.py).

      * FOBI_FORM_ELEMENT_RADIO_SUBMIT_VALUE_AS
      * FOBI_FORM_ELEMENT_SELECT_SUBMIT_VALUE_AS
      * FOBI_FORM_ELEMENT_SELECT_MULTIPLE_SUBMIT_VALUE_AS

  Allowed values are: "val", "repr", "mix".

0.4.26
-------------------------------------
2015-03-06

- Validate `fobi.contrib.plugins.form_elements.fields.email`,
  `fobi.contrib.plugins.form_elements.fields.integer` and
  `fobi.contrib.plugins.form_elements.fields.url` plugins initial values.
- Properly show field types "checkbox" and "radio" in the `input` plugin (as
  previously they showed up too large).
- It's now possible to restrict multiple usage of form handler plugins via
  ``allow_multiple`` property. In case if it's set to False, the plugin can
  be used once only (per form). Default value is True. The `db_store` plugin
  is from now on allowed to be used only once (per form).

0.4.25
-------------------------------------
2015-03-04

- Post-fix in the discover module (moved logging definition up).

0.4.24
-------------------------------------
2015-03-04

- The management command `migrate_03_to_04` intended to migrate 0.3.x branch
  data to > 0.4.x branch data, has been renamed to `fobi_migrate_03_to_04`.
- Add missing app config declaration for the `db_store` form handler plugin.
- Add missing app config for the core `fobi` package.
- Improved autodiscover for Django>=1.7. Fix exception when using a dotted
  path to an `AppConfig` in `INSTALLED_APPS` (instead of using the path to
  the app: ex. "path.to.app.apps.AppConfig" instead of "path.to.app").

0.4.23
-------------------------------------
2015-03-04

- Fix improper initial value validation for Select-like (`radio`,  `select` and
  `select_multiple`) plugins.

0.4.22
-------------------------------------
2015-03-03

- Fix replace system-specific path separator by a slash on file urls.
- Fix empty options appearing in the Select-like (`radio`,  `select` and 
  `select_multiple`) plugins and unified the processing of the raw choices
  data.
- Validate the initial value for Select-like (`radio`,  `select` and
  `select_multiple`) plugins.

0.4.21
-------------------------------------
2015-02-28

- The
  ``fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects``
  plugin added.

0.4.20
-------------------------------------
2015-02-27

- Make it possible to load initial form data from GET variables.
- Remove "button" and "submit" types from ``fobi.contrib.elements.fields.input``
  form element plugin.
- The ``fobi.contrib.plugins.form_elements.fields.select_model_object`` plugin
  no longer returns an absolute URL to the admin of the chosen model object
  instance. Instead, it contains the app label, model name, pk and the repr
  of it separated by dots. Example: "comments.comment.5.Lorem ipsum".
- Minor fixes in ``from fobi.contrib.elements.fields.file`` plugin. Use system
  path separator on ``from fobi.contrib.elements.fields.file.FILES_UPLOAD_DIR``
  default setting.
- Minor documentation improvements.

0.4.19
-------------------------------------
2015-02-15

- Some more work on future (Django 1.9) compatibility.
- Replace bits of backwards-/forwards- compatibility code with equal code 
  parts of ``django-nine``.

0.4.18
-------------------------------------
2015-02-13

- From now on it's possible to localise (translated) URLs.
- Safe way to get the user model for Django >= 1.5.* <= 1.8.*

0.4.17
-------------------------------------
2015-02-12

- Fix circular imports by proper referencing of the user model in
  foreign key and many-to-many relations (``settings.AUTH_USER_MODEL`` instead
  of ``django.contrib.auth.get_user_model``).
- Minor documentation improvements.

0.4.16
-------------------------------------
2015-02-10

- A new theme ``djangocms_admin_style_theme`` added.
- Making ``fobi.fields.NoneField`` always valid.
- Initial work on Django 1.8 and 1.9 support.
- Minor fixes.

0.4.15
-------------------------------------
2015-01-27

- Fix the "large" checkboxes in edit mode - now shown small as they should be.

0.4.14
-------------------------------------
2015-01-26

- German translations added.

0.4.13
-------------------------------------
2015-01-15

- Remove an `ipdb` statement from base integration processor
  `fobi.integration.processors.IntegrationProcessor`.
- Added information in the docs about FeinCMS demo part on heroku demo.
- Make sure values of form elements declared not to have a value (``has_value``
  property is set to False) aren't being saved in the ``db_store`` plugin.
- Remove redundant static assets (package size decreased).

0.4.12
-------------------------------------
2015-01-14

- Fix empty options appearing in the Select-like plugins and unified the
  processing of the raw choices data.
- Update the `vishap` package requirement to latest stable 0.1.3.
- Support for wheel packages.

0.4.11
-------------------------------------
2012-12-29

- Styling fixes in the ``radio`` button field of the ``bootstrap3`` theme.
- Fixed ``db_store`` issue with CSV/XLS export failing on Django 1.7.

0.4.10
-------------------------------------
2012-12-28

- Minor fixes in FeinCMS integration app.

0.4.9
-------------------------------------
2012-12-28

- Third party app integration (at the moment, FeinCMS, DjangoCMS, Mezzanine)
  had been generalised and unified.
- Mention the Heroku live demo in the docs.
- Minor CSS fixes in the ``simple`` theme.

0.4.8
-------------------------------------
2012-12-25

- More verbose debugging.

0.4.7
-------------------------------------
2012-12-24

- Temporary left out the "cloneable" column from the dashboard templates.
- Fixed broken imports in CAPTCHA plugin.
- Fixed broken imports in ReCAPTCHA plugin.

0.4.6
-------------------------------------
2012-12-23

- Updated requirements for the ``vishap`` package to avoid the ``six`` version
  conflicts.
- Minor documentation fixes.

0.4.5
-------------------------------------
2012-12-17

- ReCAPTCHA field added.
- Mezzanine integration app added.
- Remove redundant dependencies (django-tinymce).
- Minor improvements of the discover module.

0.4.4
-------------------------------------
2014-12-06

- Documentation improvements.
- Updated Dutch and Russian translations.
- Minor fixes related to lazy translations.

0.4.3
-------------------------------------
2014-12-05

- Make sure values of form elements declared not to have a value (``has_value``
  property is set to False) aren't being saved in the ``db_store`` plugin.
- Apply that to the ``honeypot`` and ``captcha`` plugins.

0.4.2
-------------------------------------
2014-12-04

- Helper script (management command) in order to migrate django-fobi==0.3.* 
  data to django-fobi==0.4.* data (caused by renaming the ``birthday`` field 
  to ``date_drop_down`` - see the release notes of 0.4 below). Follow the steps
  precisely in order to painlessly upgrade your django-fobi==0.3.* to
  django-fobi==0.4.*:

  1. Install django-fobi>=0.4.2::

         pip install django-fobi>=0.4.2

  2. In your settings change the::

         'fobi.contrib.plugins.form_elements.fields.birthday'
         
     to::

         'fobi.contrib.plugins.form_elements.fields.date_drop_down'

  3. Run the ``migrate_03_to_04`` management command. Note, that as of version
     0.4.24, the `migrate_03_to_04` command has been renamed to
     `fobi_migrate_03_to_04`.::

         ./manage.py migrate_03_to_04

0.4.1
-------------------------------------
2014-12-04

- Fixes in Foundation5 and Simple themes related to the changes in error
  validation/handling of hidden fields.

0.4
-------------------------------------
2014-12-03

Note, that this release contains minor backwards incompatible changes. The
changes may affect your existing forms and data. Read the notes below
carefully (UPDATE 2014-12-04: the django-fobi==0.4.2 contains a management 
command which makes the necessary changes in the database for safe upgrade).

- The ``captcha`` field has been moved from 
  ``fobi.contrib.plugins.form_elements.fields.captcha`` to
  ``fobi.contrib.plugins.form_elements.security.captcha``. Make sure to update
  the package paths in ``INSTALLED_APPS`` of your projects' settings module
  (settings.py) when upgrading to this version.
- The ``honeypot`` field has been added.
- The ``birthday`` field has been renamed to ``date_drop_down`` (A real
  ``birthday`` field is still to come in later releases). The change causes
  backwards incompatibility issues if you have used that ``birthday`` field.
  If you haven't - you have nothing to worry. If you have been using it,
  grab the 0.3.4 version, copy the
  ``fobi.contrib.plugins.form_elements.fields.date_drop_down`` package to
  your project apps, make necessary path changes and update the package paths
  in ``INSTALLED_APPS`` settings module (settings.py) before upgrading to this
  version. Then, in Django admin management interface, replace all the
  occurances of ``Birthday`` field with ``Date drop down`` field.
- Better error validation/handling of hidden fields. A new form snippet 
  template added for displaying the non-field and hidden fields errors. The new
  template makes a part of a standard theme as an attribute
  ``form_non_field_and_hidden_errors_snippet_template``.
- Minor fixes in generic templates.
- An additional property ``is_hidden`` added to the hidden form elements. Those
  form elements would be getting a default TextInput widget in the edit mode
  instead of the widget they come from by default. It's possible to provide an
  alternative widget for the edit mode as well. Default value of the
  ``is_hidden`` is set to False.

0.3.4
-------------------------------------
2014-11-23

- New settings ``FOBI_FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS`` and
  ``FOBI_FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS`` introduced. They do as 
  their name tells. Default value for both is False.
- Fixed exceptions raised when unicode characters were used as form names.
- Fixed exceptions raised when unicode characters were used as field labels.
- Fixes in the `db_store` and `mail` plugins related to usage of unicode
  characters.

0.3.3
-------------------------------------
2014-11-22

- Clean up the setup. Remove redundant dependencies.
- Documentation improvements.

0.3.2
-------------------------------------
2014-11-20

- DjangoCMS integration app made compatible with DjangoCMS 2.4.3.

0.3.1
-------------------------------------
2014-11-19

- DjangoCMS integration app.

0.3
-------------------------------------
2014-11-09

Note, that this release contains minor backwards incompatible changes. The
changes do not anyhow affect your existing forms or data. The only thing you
need to do is update the app paths in the ``settings`` module of your project.

- Minor core improvements related to the themeing of the form handler plugins.
- Several presentational form element plugins have been renamed.
  The ``fobi.contrib.plugins.form_elements.content.image`` plugin has been
  renamed to ``fobi.contrib.plugins.form_elements.content.content_image``.
  The ``fobi.contrib.plugins.form_elements.content.text`` plugin has been
  renamed to ``fobi.contrib.plugins.form_elements.content.content_text``.
  The ``fobi.contrib.plugins.form_elements.content.video`` plugin has been
  renamed to ``fobi.contrib.plugins.form_elements.content.content_video``.
  If you have used any of the above mentioned plugins, make sure to update 
  the app paths in the ``settings`` module of your project.
- The ``fobi.contrib.plugins.form_elements.content.dummy`` plugin has been moved
  to ``fobi.contrib.plugins.form_elements.test.dummy`` location. If you have
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
