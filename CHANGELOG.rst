Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.13.7
------
2018-10-01

- Make fobi wagtail integration work with wagtail 2.

0.13.6
------
2018-08-16

- Completely wiping out ``django-autoslug`` in requirements (for now it has
  been replaced with ``django-autoslug-iplweb``).

0.13.5
------
2018-08-12

- Minor fixes in code, tests and docs.

0.13.4
------
2018-08-11

- Django 2.1 support (initial).
- Upgrade test suite.

0.13.3
------
2018-07-10

- Minor fixes admin export of form entries (Postgres).

0.13.2
------
2018-03-12

- Choices are now required fields for `checkbox_select_multiple`, `radio`,
  `select`, `select_multiple` and `select_multiple_with_max` form elements.
- The `active_date_from`, `active_date_to`, `inactive_page_title`,
  `inactive_page_message` added to forms the import/export flow.

0.13.1
------
2018-02-28

- Minor fixes in recaptcha plugin.
- Add `max_length` to textarea plugin.

0.13
----
2018-02-25

.. note::

    This release contains minor backwards incompatible changes.
    A number of new database fields have been added to the `FormEntry`
    model (`active_date_from`, `active_date_to`, `inactive_page_title`,
    `inactive_page_message`). You will need to migrate your database.

- Implement disabling forms based on dates. Note, that although the feature
  is landed into the core, contrib packages (such as Foundation 5 theme,
  Simple theme, Django CMS admin style theme, DRF integration app,
  FeinCMS integration app, Mezzanine integration app, DjangoCMS integration app
  and Wagtail app) are not yet updated to reflect these changes. It's a work
  in progress to be done in the nearest minor releases. Check the
  `issue #143 <https://github.com/barseghyanartur/django-fobi/issues/143>`_
  for state of the progress.

0.12.20
-------
2018-02-24

- Minor Python 2 fixes.

0.12.19
-------
2018-02-21

- Make it possible to sort on plugin ``name`` instead of ``uid``.

0.12.18
-------
2018-02-19

- Improved form element add drop-down order.
- Add initial migrations for DjangoCMS integration app.
- Add French translations.
- Implemented styles for ``bleach`` within ``content_richtext`` plugin.
- Documentation improvements.

0.12.17
-------
2018-02-14

- Security fixes in db_store plugin.
- Minor fixes and cleanups.
- If CKEditor is installed, use it (rich text) for success page message.

0.12.16
-------
2018-01-21

.. note::

    Note, that this release contains minor backwards incompatible changes, that
    may slightly break your JS and/or styling.

    The `form-horizontal` class attribute on the main form with elements (in
    templates) has been replaced with `fobi-form` id attribute.

    Affected files:

    - src/fobi/templates/fobi/generic/add_form_element_entry_ajax.html
    - src/fobi/templates/fobi/generic/edit_form_element_entry_ajax.html
    - src/fobi/templates/fobi/generic/snippets/form_ajax.html

    If you have modified any of these, you might want to check and update
    your code.

- Invisible reCAPTCHA form plugin (security) added.
- Clean up templates.
- Introduce a form_id block. The following templates were affected.

0.12.15
-------
2018-01-17

- Minor clean up of HTML templates (in some templates
  ``hidden_form_element_wrapper_html_class`` was used while others
  ``form_element_wrapper_hidden_html_class``). Now
  ``form_element_wrapper_hidden_html_class`` is used everywhere. Some HTML
  files have been re-indented (2 spaces).
- Minor clean up of JS.
- Optionally limit file extensions for file upload element

0.12.14
-------
2018-01-10

- Minor clean up of HTML templates (unused classes removed).
- Nicer captcha (simple captcha) for bootstrap3 and foundation5 themes.

0.12.13
-------
2018-01-09

.. note::

    Note, that this release contains minor backwards incompatible changes, that may
    slightly break your JS and/or styling.

    The `form-horizontal` class attribute on the main form with elements (in
    templates) has been replaced with `fobi-form` id attribute.

    Affected files:

    - /src/fobi/contrib/themes/djangocms_admin_style_theme/static/djangocms_admin_style_theme/js/fobi.djangocms_admin_style_theme.edit.js
    - /src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/edit_form_entry_ajax.html
    - /src/fobi/contrib/themes/foundation5/static/foundation5/js/foundation5_fobi_extras.js
    - /src/fobi/contrib/themes/foundation5/templates/foundation5/edit_form_entry_ajax.html
    - /src/fobi/contrib/themes/foundation5/templates/foundation5/edit_form_wizard_entry_ajax.html
    - /src/fobi/contrib/themes/simple/static/simple/js/fobi.simple.edit.js
    - /src/fobi/contrib/themes/simple/templates/simple/edit_form_entry_ajax.html
    - /src/fobi/contrib/themes/simple/templates/simple/edit_form_wizard_entry_ajax.html
    - /src/fobi/contrib/themes/bootstrap3/static/bootstrap3/js/bootstrap3_fobi_extras.js
    - /src/fobi/templates/fobi/generic/edit_form_entry_ajax.html

    If you have modified any of these, please double check that your edit views
    work and look properly.

- Fixes in simple and django-cms-admin-style themes (assets being loaded
  incorrectly since 0.12.6).
- Base template, as well as templates of all the themes have been made a
  little bit more flexible.
- Minor documentation fixes.

0.12.12
-------
2018-01-03

- More consistent loading of assets (JS, CSS) in add- and
  edit-form-element-entry templates.
- Copyright and licenses year update.
- Minor fixes in the widgets.
- Clean up.

0.12.11
-------
2017-12-27

- Clean up Django < 1.8 code.
- Clean up old code.

0.12.10
-------
2017-12-24

- Django 2.0 support (experimental).
- (Temporary) replace ``django-autoslug`` package with
  ``django-autoslug-iplweb``, which works fine for Django versions >=1.8,<=2.0.

0.12.9
------
2017-12-21

- Added content markdown plugin.

0.12.8
------
2017-12-19

- Added common form callback ``AutoFormMail`` for auto mailing the form
  data (without need to add the mail plugin to the form).

0.12.7
------
2017-12-17

- Minor fixes (in the add form element entry bootstrap3 template).
- Add content rich text plugin (based on CKEditor).
- Added common form callback ``AutoFormDbStore`` for auto saving the form
  data (without need to add the db_store plugin to the form).

0.12.6
------
2017-12-12

- Clean up.
- Minor documentation fixes.
- Minor plugin clean-up/fixes (``captcha``, ``recaptcha``, ``content_text``).
- Minor Python 3 fixes.
- Minor fixes in FormWizard ``get_absolute_url`` method.

0.12.5
------
2017-09-27

- Documentation fixes.

0.12.4
------
2017-09-27

- Documentation fixes.

0.12.3
------
2017-09-27

- Minor fixes.
- Reflect form-wizards support changes in the `foundation5` theme.
- Documentation fixes.

0.12.2
------
2017-08-02

- Some work on full form-wizards support in the `foundation5` theme.
- Django 1.11 fixes for customised widgets.
- Update example project requirements.

0.12.1
------
2017-07-31

- Reflect form-wizards support changes in the `simple` theme.
- Fixes in docs.

0.12
----
2017-06-28

- Wagtail integration (yet experimental).

0.11.13
-------
2017-06-10

- Updated docs for DjangoCMS, FeinCMS and Mezzanine.
- Updated outdated Dutch translations.
- Improvements of the DRF integration app documentation.
- Duration field added.
- Support ``DurationField`` in ``drf_integration`` integration app.
- Minor fixes in docs.

0.11.12
-------
2017-05-31

- Added a lot of field metadata to the OPTIONS call of ``drf_integration`` app.
- Appended a lot of sub-module README files to the main documentation.

0.11.11
-------
2017-05-29

- Minor fixes in ``content_text`` ``drf_integration`` plugin.
- Added ``imageurl`` support to the ``mailchimp_importer`` plugin.

0.11.10
-------
2017-05-26

- Minor fixes in form-wizards on Django 1.11.

0.11.9
------
2017-05-24

- Mezzanine integration updated to work with Mezzanine 4.2.3.
- Fixes in date-drop-down plugin when using form wizards.

0.11.8
------
2017-05-17

- ``ContentImageURL`` plugin added.
- Minor Python3 fixes in ``db_store`` plugin (related to export of forms to
  ``xls`` format).

0.11.7
------
2017-05-16

- Fixed in ``fobi.integration`` package related to Django 1.10 and higher.
- FeinCMS integration updated (only migrations added) to work with
  FeinCMS 1.13.2.
- DjangoCMS integration updated to work with DjangoCMS 3.4.3.

0.11.6
------
2017-05-15

- Minor fixes in ``drf_integration`` app, added GET/detail actions tests.

0.11.5
------
2017-05-15

- Added ``date_drop_down`` to ``drf_integration`` app.
- Fixed dependencies issue.
- Added dedicated requirements for specific Django versions.

0.11.4
------
2017-05-12

- Minor fixes in integration callbacks of the ``drf_integration`` sub-package.
- Added support for ``content_image``, ``content_text`` and ``content_video``
  plugins.
- Fixes in installable demo.

0.11.3
------
2017-05-10

- Concept of integration callbacks introduced and implemented for the
  ``drf_integration`` sub-package.

0.11.2
------
2017-05-09

- Minor fixes in ``drf_integration`` app.

0.11.1
------
2017-05-08

- Minor fixes in ``decimal`` plugin.
- Minor documentation improvements.

0.11
----
2017-05-07

This release is dedicated to my beloved `wife <https://github.com/anagardi>`_
for all the love and support she gave me through years. If you are a company
looking for (female) developers in Groningen area (the Netherlands),  do not
hesitate to `contact her <mailto:anahit.gardishyan@gmail.com>`_.

- Django REST framework integration. Check the Heroku demo `here
  <https://django-fobi.herokuapp.com/api/>`_.
- Documentation fixes.
- PEP8 code fixes.
- Minor setup fixes related to moved screen-shots file.
- Added helper scripts to test with Firefox in headless mode. Describe
  testing with Firefox in headless mode in documentation.
- Validate the ``decimal`` field plugin - quantize the decimal value to the
  configured precision.
- Minor fixes in the ``float`` field plugin.
- Minor improvements in complex form element plugins (``select``, ``file``) and
  form handler plugins (``db_store``, ``mail``, ``http_respost``) in order to
  simplify integration plugins and reduce code duplication.
- Minor Python3 fixes in ``range_select`` and ``slider`` form element plugins.
- Minor Python3 fixes in ``http_repost`` and ``mail`` form handler plugins.

0.10.7
------
2017-03-13

- Several Django deprecation/moves fixes for better future compatibility.

0.10.6
------
2017-02-14

- Minor Python 3 fixes for integer, float and decimal fields.

0.10.5
------
2017-02-13

- Tested against Python 3.6.
- Initial (experimental) Django 1.11 support.

0.10.4
------
2017-01-11

- Minor fixes in Django admin.
- Various pep8 fixes.
- Fixes additions and improvements in/of docs.
- Add options to test with PhantomJS instead of Firefox.

0.10.3
------
2016-11-24

- Minor fixes.

0.10.2
------
2016-11-24

- Minor fixes.

0.10.1
------
2016-11-17

- Fixed captcha and re-captcha issues in form wizards.

0.10
----
2016-11-16

.. note::

    Note, that this release contains minor backwards incompatible changes, that may
    break your code. Two additional arguments have been added to the
    `submit_plugin_form_data` method of the form element plugins. If you have
    written custom form element plugins - update your code.

- Added `form_entry_elements` and `kwargs` to the `submit_plugin_form_data`
  method of the form element plugins. Make sure to update your custom
  plugins if you have written any.
- Added tests for mailchimp integration plugin.
- Moving all plugins to base submodules of the correspondent sub
  packages.
- Add missing whitespace to the ``help_text`` of the ``title`` field of
  ``FormEntry`` and ``FormWizardEntry`` models.
- Disable GoogleAnalytics while testing (guess what - this change speeds up
  selenium tests twice).
- Docs updated.
- Helper scripts updated.
- Multiple pep8 fixes.

0.9.17
------
2016-11-13

.. note::

    Announcing dropping support of Python 2.6 and Django 1.7. As of 0.9.17
    everything is still backwards compatible with Django 1.7, but in future
    versions it will be wiped out.

- Value validations for Integer and Text Fields.
- Hide previous button in form wizard template for bootstrap3 on first step.

0.9.16
------
2016-11-10

- Introduced form titles (shown in view templates).
- Improved navigation of the form wizards.

0.9.15
------
2016-11-07

- Minor fixes.

0.9.14
------
2016-11-07

- Minor fixes.

0.9.13
------
2016-11-05

.. note::

    Announcing dropping support of Django 1.5 and 1.6. As of 0.9.13 everything is
    still backwards compatible with versions 1.5 and 1.6, but in future versions
    compatibility with these versions will be wiped out.

- Fix backwards compatibility of `slider` and `range_select` plugins with
  Django versions 1.5 and 1.6.

0.9.12
------
2016-11-02

- Better debugging.
- Upgrade example FeinCMS integration to work with 1.12.

0.9.11
------
2016-11-01

- Fixes.

0.9.10
------
2016-11-01

- Fixed issue with custom labels in the `slider` plugin.
- Made `slider` plugin compatible with Django <= 1.6.
- Fixes `get_absolute_url` methods on `FormEntry` and `FormWizardEntry`
  models. #48

0.9.9
-----
2016-10-31

- Make it possible to add custom ticks to the `slider` plugin.

0.9.8
-----
2016-10-27

- Support multiple sliders in one form.

0.9.7
-----
2016-10-27

- Improvements in the generic integration processor. #47
- Improved form wizard interface and navigation.
- Fixed a broken test.
- Added import/export functionality for form wizards.

0.9.6
-----
2016-10-25

- Fixed InvalidQuery exception raised when attempting to export entry from a
  'DB store' handler. #44
- Fixed ProgrammingError raised when using the 'Export data to CSV/XLS'
  action. #45

0.9.5
-----
2016-10-25

- Minor fixes in `slider` and `select_range` plugins.

0.9.4
-----
2016-10-24

- Fix issue with `select_multiple`, `select_multiple_model_objects` and
  `select_multiple_mptt_model_objects` being invalidated on the last step
  of the form wizard.

0.9.3
-----
2016-10-24

- Change to `NumberInput` widget for all number inputs.
- Fixed issue with `slider` plugin missing labels if `Show endpoints as` is
  set to `Labeled ticks`.
- Link to edit form entry added to edit form wizard entry view.

0.9.2
-----
2016-10-24

- Minor fixes.

0.9.1
-----
2016-10-24

- Minor fixes.

0.9
---
2016-10-24

.. note::

    Note, that this release contain minor backwards incompatible changes, that
    may break your existing code (your data is left intact). If you have written
    custom form element plugins you should update your code!

- The :method:`get_form_field_instances`
  and :method:`_get_form_field_instances` of
  the :class:`fobi.base.FormElementPlugin` both accept two new optional
  arguments: `form_entry` and `form_element_entries` as well as `**kwargs`.
  Make sure to update your custom plugins if you have written any.
- Minor fixes in the form wizards: forms in intermediate steps do receive
  updates from the `submit_plugin_form_data` of the plugins.
- Fixed issue in the `base_bulk_change_plugins` function on Django 1.10.

0.8.10
------
2016-10-22

- Minor CSS improvements of the `slider` plugin.
- Fixed broken readthedocs requirements.

0.8.9
-----
2016-10-22

- Simplified debugging (never set `FOBI_DEBUG` to True in production!).
- Major `slider` plugin improvements.

0.8.8
-----
2016-10-21

- Minor `slider` plugin improvements (JavaScript).

0.8.7
-----
2016-10-21

- Fixed issue of plugin media not being collected in the form wizard.

0.8.6
-----
2016-10-21

- Functional improvements of `slider` plugin.

0.8.5
-----
2016-10-20

- Add `range_select` and `slider` form field plugins.
- Fixed custom CSS classes not appearing in the rendered HTML of the field
  plugin/widget.
- Fixed issue with undefined file storage for form wizards. From now on
  the `FileSystemStorage` storage is used for wizard uploads.
- Fixed too much of extreme data view/export security of the `db_store`
  plugin.
- Backwards compatibility fixes for Django < 1.7.

0.8.4
-----
2016-10-19

- Fix broken export (to JSON) of form entries.
- Fix broken import (from JSON) of form entries.

0.8.3
-----
2016-10-18

- Minor fixes.

0.8.2
-----
2016-10-18

- Minor fixes.

0.8.1
-----
2016-10-17

- Minor fixes.

0.8
---
2016-10-17

Release supported by `Lund University Cognitive Science
<http://www.lucs.lu.se/choice-blindness-group/>`_.

- Adding form-wizards functionality. Note, that at the moment only
  `bootstrap3` theme was updated to fully support the form wizards. Although,
  all other themes would by default support form-wizard functionality, they
  may not look as nice as they should be (to be fixed in 0.8.x releases
  shortly).
- The `six` package requirements increased to >= 1.8.
- Tests comply with pep8.
- Fixed recently broken drag-and-drop ordering of the form elements.
- Fixed typo for HTML id "tab-form-elemenets" -> "tab-form-elements". You
  may need to update your custom CSS/JS/HTML accordingly. See the listing
  0.8.a for the files affected.
- An additional property `form_view_form_entry_option_class` has been added
  to all the themes. Change your custom CSS/JS/HTML accordingly. See the
  listing 0.8.b for the files affected.
- Fixed drag-and-drop not working for ordering of form elements. #43
- Fixed issue with non-proper rendering of the form-importer templates.

.. note::

    Although this release does not contain backwards incompatible changes, there
    have been several changes in GUI and some parts of the generic HTML and themes
    were updated. If you have custom themes implemented, you should likely make
    some minor updates to the HTML in order to reflect the latest GUI changes.
    The following templates have been affected:

New files
~~~~~~~~~
- src/fobi/contrib/plugins/form_handlers/db_store/templates/db_store/view_saved_form_wizard_data_entries.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/add_form_wizard_handler_entry.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/add_form_wizard_handler_entry_ajax.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/create_form_wizard_entry.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/create_form_wizard_entry_ajax.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/edit_form_wizard_entry.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/edit_form_wizard_entry_ajax.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/form_wizards_dashboard.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/snippets/form_wizard_ajax.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/snippets/form_wizard_properties_snippet.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/snippets/form_wizard_snippet.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/view_form_wizard_entry.html
- src/fobi/contrib/themes/bootstrap3/templates/bootstrap3/view_form_wizard_entry_ajax.html
- src/fobi/templates/fobi/generic/add_form_wizard_handler_entry.html
- src/fobi/templates/fobi/generic/add_form_wizard_handler_entry_ajax.html
- src/fobi/templates/fobi/generic/create_form_wizard_entry.html
- src/fobi/templates/fobi/generic/create_form_wizard_entry_ajax.html
- src/fobi/templates/fobi/generic/edit_form_wizard_entry.html
- src/fobi/templates/fobi/generic/edit_form_wizard_entry_ajax.html
- src/fobi/templates/fobi/generic/form_wizard_entry_submitted.html
- src/fobi/templates/fobi/generic/form_wizard_entry_submitted_ajax.html
- src/fobi/templates/fobi/generic/form_wizards_dashboard.html
- src/fobi/templates/fobi/generic/snippets/form_wizard_ajax.html
- src/fobi/templates/fobi/generic/snippets/form_wizard_properties_snippet.html
- src/fobi/templates/fobi/generic/snippets/form_wizard_snippet.html
- src/fobi/templates/fobi/generic/snippets/form_wizard_view_ajax.html
- src/fobi/templates/fobi/generic/view_form_wizard_entry.html
- src/fobi/templates/fobi/generic/view_form_wizard_entry_ajax.html

Existing files
~~~~~~~~~~~~~~
- src/fobi/contrib/plugins/form_importers/mailchimp_importer/templates/mailchimp_importer/1.html
- src/fobi/contrib/plugins/form_importers/mailchimp_importer/views.py
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/edit_form_entry_ajax.html
- src/fobi/contrib/themes/foundation5/templates/foundation5/edit_form_entry_ajax.html
- src/fobi/templates/fobi/generic/edit_form_entry_ajax.html

Additional listings
~~~~~~~~~~~~~~~~~~~
Listing 0.8.a "tab-form-elemenets" -> "tab-form-elements"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- src/fobi/contrib/themes/djangocms_admin_style_theme/static/djangocms_admin_style_theme/css/fobi.djangocms_admin_style_theme.edit.css
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/edit_form_entry_ajax.html
- src/fobi/contrib/themes/foundation5/templates/foundation5/edit_form_entry_ajax.html
- src/fobi/contrib/themes/simple/static/simple/css/fobi.simple.edit.css
- src/fobi/contrib/themes/simple/templates/simple/edit_form_entry_ajax.html
- src/fobi/templates/fobi/generic/edit_form_entry_ajax.html
- src/fobi/templates/fobi/generic/edit_form_wizard_entry_ajax.html

Listing 0.8.b `form_view_form_entry_option_class` property
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- src/fobi/contrib/themes/bootstrap3/fobi_themes.py
- src/fobi/contrib/themes/djangocms_admin_style_theme/fobi_themes.py
- src/fobi/contrib/themes/foundation5/fobi_themes.py
- src/fobi/contrib/themes/simple/fobi_themes.py
- src/fobi/templates/fobi/generic/edit_form_wizard_entry_ajax.html

0.7.1
-----
2016-09-22

Release sponsored by `Goldmund, Wyldebeast & Wunderliebe
<https://www.goldmund-wyldebeast-wunderliebe.nl/>`_.

- Code comply with pep8.
- Minor fixes in selenium tests.

0.7
---
2016-09-13

Release sponsored by `Goldmund, Wyldebeast & Wunderliebe
<https://www.goldmund-wyldebeast-wunderliebe.nl/>`_.

- Initial Django 1.10 support.
- `django-localeurl` has been replaced with `i18n_patterns` in sample project.
- Minor fixes.

0.6.10
------
2016-09-11

- Moved `plugin_uid` field choices from model level to form level for
  `FormHandler` and `FormHandlerEntry` models. #37

0.6.9
-----
2016-09-08

- Moved `plugin_uid` field choices from model level to form level for
  `FormElement` and `FormElementEntry` models. #37
- Fixed element "name" field stripping underscores issue. #33

0.6.8
-----
2016-09-06

- Fixed changing order of the `FormElement`, `FormElementEntry`, `FormHandler`
  and `FormHandlerEntry` models.

0.6.7
-----
2016-08-30

- Minor fixes in `db_store` plugin (Django 1.6 compatibility issue).
- Added __str__ methods to models.
- Restrict queryset to form element entries related to the form entry in
  position calculation.

0.6.6
-----
2016-05-12

- Fixed broken dependencies in demos.
- Minor fixes.
- Adding a new `Select multiple with max` plugin, which restricts max number
  of choices allowed to be chosen.

0.6.5
-----
2015-12-24

- Minor fixes.

0.6.4
-----
2015-12-24

- Minor fixes.

0.6.3
-----
2015-12-23

- Minor fixes.

0.6.2
-----
2015-12-22

- Make it possible to render a list of forms using custom template tag (not
  only on the dashboard page).

0.6.1
-----
2015-12-21

- Documentation fixes.

0.6
---
2015-12-18

- Form importers (and as a part of it - MailChimp integration,
  which would allow to import forms from MailChimp into `django-fobi` using
  a user-friendly wizard).
- Improved Django 1.9 support.

0.5.19
------
2015-12-15

- New style urls everywhere.

0.5.18
------
2015-12-08

- Minor improvements. Adding request to the `get_form_field_instances` method
  of the `FormElementPlugin`.

0.5.17
------
2015-10-22

- Increased `easy-thumbnails` requirement to >= 2.1 for Python 3, since it was
  causing installation errors.
- Increased the `django-nine` requirement to >=0.1.6, since it has better
  Python 3 support.

0.5.16
------
2015-10-05

- Fixes in migrations on Django 1.7.

0.5.15
------
2015-09-17

- Minor fixes.

0.5.14
------
2015-09-13

- Add create/update dates to the forms. Adding initial migrations.

0.5.13
------
2015-09-01

- Translation fixes.
- Updating Dutch and Russian translations.

0.5.12
------
2015-08-29

- Export/import forms into/from JSON.
- Minor UI improvements. Adding "Service" tab in the edit view which contains
  links to export form to JSON and delete form.

.. note::

    Although this release does not contain backwards incompatible changes, there
    have been several changes in GUI and some parts of the generic HTML and themes
    were updated. If you have custom themes implemented, you should likely make
    some minor updates to the HTML in order to reflect the latest GUI changes.
    The following templates have been affected:

New files
~~~~~~~~~
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/import_form_entry.html
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/import_form_entry_ajax.html

- src/fobi/contrib/themes/foundation5/templates/foundation5/import_form_entry.html
- src/fobi/contrib/themes/foundation5/templates/foundation5/import_form_entry_ajax.html

- src/fobi/contrib/themes/simple/templates/simple/import_form_entry.html
- src/fobi/contrib/themes/simple/templates/simple/import_form_entry_ajax.html

- src/fobi/templates/fobi/generic/import_form_entry.html
- src/fobi/templates/fobi/generic/import_form_entry_ajax.html

Existing files
~~~~~~~~~~~~~~
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/dashboard.html
- src/fobi/contrib/themes/djangocms_admin_style_theme/templates/djangocms_admin_style_theme/edit_form_entry_ajax.html

- src/fobi/contrib/themes/foundation5/templates/foundation5/dashboard.html
- src/fobi/contrib/themes/foundation5/templates/foundation5/edit_form_entry_ajax.html

- src/fobi/contrib/themes/simple/templates/simple/dashboard.html
- src/fobi/contrib/themes/simple/templates/simple/edit_form_entry_ajax.html

- src/fobi/templates/fobi/generic/dashboard.html
- src/fobi/templates/fobi/generic/edit_form_entry_ajax.html

0.5.11
------
2015-08-20

- Minor improvements of the dynamic values feature. Forbid usage of django
  template tags in initial values.

0.5.10
------
2015-08-18

- Minor improvements of the initial dynamic values feature.

0.5.9
-----
2015-08-17

- Minor fixes in the initial dynamic values feature.

0.5.8
-----
2015-08-16

- Made it possible to define dynamic initials for form fields. Example initial
  dynamic values in the form (like {{ request.path }}).
- Minor fixes/improvements.

0.5.7
-----
2015-08-03

- Minor Python 3 improvements.

0.5.6
-----
2015-07-31

- `django-mptt` support through `select_mptt_model_object` and
  `select_multiple_mptt_model_objects` plugins.
- Python 3 fixes.

0.5.5
-----
2015-06-30

- Change the `action` field of the FormEntry into a URL field; check if
  action exists.
- `captcha`, `recaptcha` and `honeypot` plugins have been made required
  in the form.
- Fix: take default values provided in the `plugin_data_fields` of the plugin
  form into consideration.

0.5.4
-----
2015-05-21

- Minor Django 1.8 fixes.
- Improved texts/translations.

0.5.3
-----
2015-05-02

- Minor fixes in the `mail
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_handlers/mail>`_
  form handler plugin.

0.5.2
-----
2015-04-26

- Make it possible to provide multiple `to` email addresses in the `mail
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_handlers/mail>`_
  form handler plugin.
- DateTime picker widget added for Foundation5 theme for `date
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_elements/fields/date>`_
  and `datetime
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_elements/fields/datetime>`_
  plugins.
- Added more tests (more plugins tested).

0.5.1
-----
2015-04-21

- DateTime picker widget added for Bootstrap 3 theme for `date
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_elements/fields/date>`_
  and `datetime
  <https://github.com/barseghyanartur/django-fobi/tree/0.5.2/src/fobi/contrib/plugins/form_elements/fields/datetime>`_
  plugins.

0.5
---
2015-04-06

.. note::

    Note, that this release contains minor backwards incompatible changes. The
    changes may affect your existing forms and data. Read the notes below
    carefully.

- Fixed previously wrongly labeled (in `AppConf`) add-ons/plugins
  (`fobi.contrib.plugins.form_handlers.db_store`,
  `fobi.contrib.apps.feincms_integration`,
  `fobi.contrib.apps.djangocms_integration`,
  `fobi.contrib.apps.mezzanine_integration`). Due to the change, you would
  likely have to rename a couple of database tables and update references
  accordingly. No migrations to solve the issue are included at the moment.

0.4.36
------
2015-04-03

- Handle non-ASCII characters content_text form element.

0.4.35
------
2015-03-28

- Fixed the issue with `allow_multiple` working incorrectly for form handler
  plugins. Fix the `db_store` plugin as well.

0.4.34
------
2015-03-27

- Minor fixes in the `Checkbox select multiple` and `Radio` plugins.
- Minified tox tests.

0.4.33
------
2015-03-26

- `Checkbox select multiple
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/checkbox_select_multiple>`_
  field added.
- Minor improvements (styling) in the Foundation 5 theme.
- Initial configuration for tox tests.
- Clean up requirements (for example setups and tests).

0.4.32
------
2015-03-25

- Updated missing parts in the Russian translations.
- Minor API improvements. From now on, the `run` method of form handlers
  may return a tuple (bool, mixed). In case of errors it might be (False, err).
- Minor code clean ups.

0.4.31
------
2015-03-23

- When path of the uploaded file (plugins) doesn't yet exist, create it,
  instead of failing.

0.4.30
------
2015-03-23

- From now on submitted files are sent as attachments in the mail plugin.
- Documentation improvements. Adding information of rendering forms using
  `django-crispy-forms` or alternatives.
- Minor fixes.

0.4.29
------
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
------
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
------
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
------
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
------
2015-03-04

- Post-fix in the discover module (moved logging definition up).

0.4.24
------
2015-03-04

- The management command `migrate_03_to_04` intended to migrate 0.3.x branch
  data to > 0.4.x branch data, has been renamed to `fobi_migrate_03_to_04`.
- Add missing app config declaration for the `db_store` form handler plugin.
- Add missing app config for the core `fobi` package.
- Improved autodiscover for Django>=1.7. Fix exception when using a dotted
  path to an `AppConfig` in `INSTALLED_APPS` (instead of using the path to
  the app: ex. "path.to.app.apps.AppConfig" instead of "path.to.app").

0.4.23
------
2015-03-04

- Fix improper initial value validation for Select-like (`radio`,  `select` and
  `select_multiple`) plugins.

0.4.22
------
2015-03-03

- Fix replace system-specific path separator by a slash on file urls.
- Fix empty options appearing in the Select-like (`radio`,  `select` and
  `select_multiple`) plugins and unified the processing of the raw choices
  data.
- Validate the initial value for Select-like (`radio`,  `select` and
  `select_multiple`) plugins.

0.4.21
------
2015-02-28

- The
  ``fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects``
  plugin added.

0.4.20
------
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
------
2015-02-15

- Some more work on future (Django 1.9) compatibility.
- Replace bits of backwards-/forwards- compatibility code with equal code
  parts of ``django-nine``.

0.4.18
------
2015-02-13

- From now on it's possible to localise (translated) URLs.
- Safe way to get the user model for Django >= 1.5.* <= 1.8.*

0.4.17
------
2015-02-12

- Fix circular imports by proper referencing of the user model in
  foreign key and many-to-many relations (``settings.AUTH_USER_MODEL`` instead
  of ``django.contrib.auth.get_user_model``).
- Minor documentation improvements.

0.4.16
------
2015-02-10

- A new theme ``djangocms_admin_style_theme`` added.
- Making ``fobi.fields.NoneField`` always valid.
- Initial work on Django 1.8 and 1.9 support.
- Minor fixes.

0.4.15
------
2015-01-27

- Fix the "large" checkboxes in edit mode - now shown small as they should be.

0.4.14
------
2015-01-26

- German translations added.

0.4.13
------
2015-01-15

- Remove an `ipdb` statement from base integration processor
  `fobi.integration.processors.IntegrationProcessor`.
- Added information in the docs about FeinCMS demo part on heroku demo.
- Make sure values of form elements declared not to have a value (``has_value``
  property is set to False) aren't being saved in the ``db_store`` plugin.
- Remove redundant static assets (package size decreased).

0.4.12
------
2015-01-14

- Fix empty options appearing in the Select-like plugins and unified the
  processing of the raw choices data.
- Update the `vishap` package requirement to latest stable 0.1.3.
- Support for wheel packages.

0.4.11
------
2014-12-29

- Styling fixes in the ``radio`` button field of the ``bootstrap3`` theme.
- Fixed ``db_store`` issue with CSV/XLS export failing on Django 1.7.

0.4.10
------
2014-12-28

- Minor fixes in FeinCMS integration app.

0.4.9
-----
2014-12-28

- Third party app integration (at the moment, FeinCMS, DjangoCMS, Mezzanine)
  had been generalised and unified.
- Mention the Heroku live demo in the docs.
- Minor CSS fixes in the ``simple`` theme.

0.4.8
-----
2014-12-25

- More verbose debugging.

0.4.7
-----
2014-12-24

- Temporary left out the "cloneable" column from the dashboard templates.
- Fixed broken imports in CAPTCHA plugin.
- Fixed broken imports in ReCAPTCHA plugin.

0.4.6
-----
2014-12-23

- Updated requirements for the ``vishap`` package to avoid the ``six`` version
  conflicts.
- Minor documentation fixes.

0.4.5
-----
2014-12-17

- ReCAPTCHA field added.
- Mezzanine integration app added.
- Remove redundant dependencies (django-tinymce).
- Minor improvements of the discover module.

0.4.4
-----
2014-12-06

- Documentation improvements.
- Updated Dutch and Russian translations.
- Minor fixes related to lazy translations.

0.4.3
-----
2014-12-05

- Make sure values of form elements declared not to have a value (``has_value``
  property is set to False) aren't being saved in the ``db_store`` plugin.
- Apply that to the ``honeypot`` and ``captcha`` plugins.

0.4.2
-----
2014-12-04

- Helper script (management command) in order to migrate django-fobi==0.3.*
  data to django-fobi==0.4.* data (caused by renaming the ``birthday`` field
  to ``date_drop_down`` - see the release notes of 0.4 below). Follow the steps
  precisely in order to painlessly upgrade your django-fobi==0.3.* to
  django-fobi==0.4.*:

  1. Install django-fobi>=0.4.2:

     .. code-block:: sh

         pip install django-fobi>=0.4.2

  2. In your settings change the:

     .. code-block:: python

         'fobi.contrib.plugins.form_elements.fields.birthday'

     to:

     .. code-block:: python

         'fobi.contrib.plugins.form_elements.fields.date_drop_down'

  3. Run the ``migrate_03_to_04`` management command. Note, that as of version
     0.4.24, the `migrate_03_to_04` command has been renamed to
     `fobi_migrate_03_to_04`.:

     .. code-block:: sh

         ./manage.py migrate_03_to_04

0.4.1
-----
2014-12-04

- Fixes in Foundation5 and Simple themes related to the changes in error
  validation/handling of hidden fields.

0.4
---
2014-12-03

.. note::

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
  occurrences of ``Birthday`` field with ``Date drop down`` field.
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
-----
2014-11-23

- New settings ``FOBI_FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS`` and
  ``FOBI_FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS`` introduced. They do as
  their name tells. Default value for both is False.
- Fixed exceptions raised when unicode characters were used as form names.
- Fixed exceptions raised when unicode characters were used as field labels.
- Fixes in the `db_store` and `mail` plugins related to usage of unicode
  characters.

0.3.3
-----
2014-11-22

- Clean up the setup. Remove redundant dependencies.
- Documentation improvements.

0.3.2
-----
2014-11-20

- DjangoCMS integration app made compatible with DjangoCMS 2.4.3.

0.3.1
-----
2014-11-19

- DjangoCMS integration app.

0.3
---
2014-11-09

.. note::

    Note, that this release contains minor backwards incompatible changes. The
    changes do not anyhow affect your existing forms or data. The only thing you
    need to do is update the app paths in the ``settings`` module of your project.

- Minor core improvements related to the theming of the form handler plugins.
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
-----
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
---
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
-----
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
-----
2014-10-23

- Minor fixes in the ``Integer`` form element plugin.
- Minor fixes in the ``Input`` form element plugin.
- Minor fixes in themes (disable HTML5 form validation in edit mode).
- Minor documentation improvements.

0.1.4
-----
2014-10-22

- Minor core improvements.
- Django 1.5 support improvements.
- Django 1.7 support improvements.
- Added ``Captcha`` form element plugin.
- Added highly-customisable ``Input`` form element plugin - a custom input field
  with support for almost any ever existing HTML attribute.
- Documentation improvements.

0.1.3
-----
2014-10-13

- Django 1.7 support.
- Add HTML5 "placeholder" field attribute support.

0.1.2
-----
2014-10-11

- Simple theme fixes: Fix for making the theme work in Django 1.5.

0.1.1
-----
2014-10-11

- Bootstrap 3 theme fixes: When tab pane has no or little content so
  that the height of the dropdown menu exceeds the height of the tab pane
  content the dropdown menu now becomes scrollable (vertically).

0.1
---
2014-10-11

- Initial release.