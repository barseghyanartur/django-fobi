=====
TODOs
=====
Based on the MoSCoW principle. Must haves and should haves are planned to be
worked on.

* Features/issues marked with plus (+) are implemented/solved.
* Features/issues marked with minus (-) are yet to be implemented.

Must haves
==========
Regarding the form wizards
--------------------------
.. code-block:: text

    - Add support for form wizard conditions.
    - Add FeinCMS integration app for form wizards.
    - Add Django-CMS integration app for form wizards.
    - Add Mezzanine integration app for form wizards.
    - Add form wizards callbacks.
    - Update documentation (wizards API parts is almost not covered there).
    - Add selenium tests for form wizards.
    - Make `foundation5` and `django-admin-theme` themes to reflect the latest
      GUI changes (form wizards).
    - Find out if `db_store` views `view_saved_form_data_entries` and
      `view_saved_form_handler_data_entries` should be protected. Perhaps,
      in case of private forms/wizards, they should be visible to author only,
      while being visible to everyone in case of public forms/wizards.
    + Finish form wizard handler plugins.
    + Copy form handler functionality into form wizard handler functionality.
    + Change management interface to be able to add form wizard handlers to the
      form wizard. This includes all views for changes, such as add form-wizard
      handler and urls.
    + Create models for form-wizard handler models.
    + Update `fobi_update_plugin_data` module with form-wizard.
    + Make sure to update the MANIFEST.in to include all additional templates.
    + Find a way to handle duplicates in saved form data in wizards (if labels
      are same within a couple of forms of the wizard).
    + Add link/switch between forms and form wizards in the main template and
      separate listing templates.
    + Make sure to include django-formtools package in the requirements.
    + Add navigation buttons to the form wizards.
    + Make sure plugin media is collected in wizards.
    + Add data-slider-tooltip="hide" option to the `slider`.
    + Ideally, it would be great to support data-slider-handle="square" (or
      "round", "triangle") options of the bootstrap-slider plugin. See the first
      issue in "Uncategorised".
    + Rethink the new navigation of forms and form wizards.
    + Fixed broken dependencies for docs.
    + Make sure captcha plugins are usable with form wizards (at the moment they
      are being invalidated on the last step).
    + Fix bug with wizards https://django-fobi.herokuapp.com/en/fobi/wizard-view/test-wiz/
      When having a date-drop-down plugin on a page, on submit you get
      TypeError at /en/fobi/wizard-view/test-wiz/
      datetime.date(2001, 1, 1) is not JSON serializable
      Surprisingly, with date or datetime plugins we don't get such errors.
      In a normal form view, also not. It's something specific to form-wizards.

Regarding the Django REST framework integration
-----------------------------------------------
.. code-block:: text

    - Add image plugin.
    - Basic foreign key relation plugins (ForeignKey, ManyToMany, OneToMany).
    - Advanced foreign key relation plugins (MPTT).
    - Think of handling the wizards.
    + Submit form functionality.
    + Advanced plugins, such as file plugin.
    + Fix representation of the content_text plugin, as now "No image provided"
      text is rendered instead of an text.

Regarding Heroku demo
---------------------
.. code-block:: text

    - See if we can use `django-storages
      <https://github.com/jschneier/django-storages>`_ for saving the files,
      because Heroku removes uploaded media. A dedicated drop-box storage would
      do.
    - Find out what SMTP server could be used for sending emails from Heroku demo.

Roadmap
-------
.. code-block:: text

    - Reusable React app to communicate with django-rest-framework integration
      app. This is very important for SAAS solution. Make it possible to embed
      fobi forms in the site using a single <fobi> tag (with arguments).
    + django-rest-framework integration.

Uncategorised
-------------
.. code-block:: text

    + Update documentation http://django-fobi.readthedocs.io/en/0.12.12/#versions
    - Add Wagtail integration tests.
    - Add Mezzanine integration tests.
    - Add FeinCMS integration tests.
    - Add DjangoCMS integration tests.
    - Implement fobi SAAS (with use of React.js).
    - Somehow PyPy started to fail under Django 1.10 and 1.11 (invocation error),
      so it must be some package incompatibility/installation problems. Find out
      why.
    - Think of moving the translation strings from in stored-in=database level to
      lazily-translated level (so that in some plugins, for instance - in database
      translations happen lazily). For mail plugin that should not be the case,
      since it's sent instantly.
    - Update translations.
    - Implement a set of django-treebeard plugins (as an alternative to MPTT).
    - Implement the clone form functionality.
    - Implement the clone form wizard functionality.
    - Rethink templating of the integration packages (feincms_integration,
      djangocms_integration, mezzanine_integration), as now they are a bit
      of a mess. Document integration properly, if not yet done.
    - Add tests for import/export of forms.
    - Add tests for export of plugin data (db_store).
    - In the form element plugins, when handling submit_form_data, somehow
      make it possible to tell whether field returned should or should not
      overwrite cleaned form data value (that's mainly interesting for form
      wizards).
    - Possibly, make plugins (same as form field plugins) for the thanks page of
      the form wizard.
    - Solve the issue with session/post data when plugin on the next step wants
      to access data from the previous (now there should be an intermediate step
      for form data first to be written into the session).
    - Make sure form element plugin widgets allow more customisations than
      they do now. For instance, setting an additional class or additional data
      attributes should be made really easy. A must!
    - Translate German and Russian URLs.
    - See if it's possible to make the "simple" theme base template (for Django
      admin) as much generic so that change between versions doesn't cause
      styling issues.
    - Make sure the existing "simple" theme works very well (in looks) in
      Django 1.8, 1.9 and 1.10.
    - Nicer styling for the radio button (Foundation 5 theme).
    - Nicer styling for the radio button (Simple theme).
    - Make it possible to provide an alternative rendering of the form field
      in the correspondent form field plugin widget (in such a way, that it
      falls back to the default rendering when no custom is available and
      uses the custom rendering if available). This should be done on the
      widget level, so that it's not necessary to update the theme in case of
      customisations made for one or more form field plugins (the rendering
      part).
    - Split the ``FOBI_RESTRICT_PLUGIN_ACCESS`` into two: one for form elements
      and one for form handlers.
    - Improve the "simple" theme for Django 1.8, 1.9 and 1.10 (tiny bits of
      styling).
    - Edit form test.
    - Edit form element tests.
    - Edit from handler tests.
    - Delete form tests.
    - List all settings overrides in docs
      https://github.com/barseghyanartur/django-fobi#tuning
    - Move reusable parts (for example, the `get_form_field_type` and
      `get_form_hidden_fields_errors` template tags into another template tag
      library or product to reuse it in Django-dash as well. Move the permission
      code from `decorators` into a separate package.
    - Update the `djangocms_admin_style` theme, since it stopped looking nice
      with the latest versions of the packages.
    - Add support for `birthday` field of MailChimp (they are
      ignored at the moment).
    - Since tests have been made quite general, create them for all contrib
      form elements and handlers (not yet for things like CAPTCHA).
    - Properly document the form importers API.
    + Add support for `imageurl` field of MailChimp (they are
      ignored at the moment).
    + Wagtail integration.
    + django-rest-framework integration.
    + Update Mezzanine, DjangoCMS and FeinCMS integration to work with Django 1.8,
      1.9, 1.10 and 1.11.
    + Implement external image plugin.
    + Finish the NoneField.
    + At the moment, NoneField is imported in the function scope. See if that works
      already to move
      it to global scope.
    + Make a basic bootstrap2 theme.
    + Wrap cosmetic.text value in <p>.
    + Redirect to thanks page, after successful post.
    + Think of themes.
    + Use twitter bootstrap3 for default theme/gui.
    + Get several class names from the active theme.
    + Write code to obtain the active theme. This requires no extra queries.
    + In the `db_store` form handler plugin, save the form headers of that moment
      in the saved data.
    + Hidden field.
    + Maybe it will be done in uniquness already, but cosmetic filds should get
      unique names automatically.
    + Add GUI controls to edit form page and build the core functionality.
    + Add initial value to all form elements.
    + Add form handlers to the GUI.
    + Likely remove (in the form edit view) the right sidebar and place the form
      edit form instead
      in order to use as much as possible of the screen.
    + Add delete form option.
    + Finish the basic dashboard. Form (existing ones), can be shown as links
      there. This page is
      cool enough for it. Just copy. http://getbootstrap.com/examples/jumbotron/
    + Rename cosmetic to content.
    + Add ``help_text`` option to all the form field plugins.
    + Something happened to the initial position of the form elements. Fix that.
    + At the moment, cosmetic plugins do not have the delete option.
    + Validate field uniqueness in a single form.
    + Make BaseFormFieldPlugin (subclass BaseFormElementPlugin) and implement
      validation method there, which accepts the request, the form and the
      form_entry object for validation. Also, in the BaseFormFieldPlugin, there
      should be `name`, `required`, `help_text`, `label` fields to be present (
      check other fields of Django formfield). In formfield plugins, subclass
      from BaseFormFieldPlugin, instead of the BaseFormElementPlugin.
    + In the view, validate the form fields (if they are subclass of
      BaseFormFieldPlugin).
    + Actually, if plugin doesn't have a form, save it immediately. Do not wait
      for POST.
    + Minimise the number of SQL queries in edit form element view.
    + Positions for form elements.
    + Add `position` field to the edit form view. Add draggable interface from
      jQueryUI.
    + Add nice admin text representation to db_store plugin, so that instead
      of "Plugin data"
      and "Form data headers", users see just nice table with results.
    + Slugify the field name (copy some func from django).
    + Group form elements (add grouping) - http://getbootstrap.com/components/#dropdowns-headers
    + Add quick overview of the fields to the form handler plugins (use
      ``__unicode__`` method?).
    + File upload field plugin.
    + Smartly get rid of prefetch_related in some places, since it doesn't
      really optimise the queries (uses IN).
    + Implement hooks for post-processing posted data of separate plugins.
    + Rewrite the views, get rid of class based ones.
    + Base form field plugin and form.
    + Add registration templates and app to the example project.
    + Video plugin.
    + Select model object plugin.
    + Phrase "Chocolate is good" is not being well slugified (JavaScript).
    + Make sure it's possible to assign CSS and JS files to the form element
      plugins.
    + Make sure the CSS and JS files from individual form element plugins are
      properly collected in the theme.
    + Actually, it really makes sense to implement the widget system for
      rendering the form elements. Widgets are not obligatory, but if present
      are used to load assets. In that way, we can easily change the behaviour
      and presentation based on the theme selected.
    + Add priority to the file handlers. For example, the ``mail`` plugin
      should get a higher priority, than ``db_save`` plugin. A module
      ``fobi.datastructures`` with a ``SortableDict`` should be used for that.
      The ``fobi.base.run_form_handlers`` function should be changed in such a way,
      that it takes the ``SortableDict`` into consideration. Have a setting
      defined in which the order of the form handlers is specified. All handlers
      that aren't mentioned there, would be executed randomly after the
      preferred list.
    + Implement the update mechanism for the form element- and form handler
      entries (similar to what's done in ``django-dash``).
    + Make sure the CSS and JS files from individual form element plugins are
      properly collected in the theme.
    + Compact the edit form interface for both "Bootstrap 3" and
      "Foundation 5" themes, by putting the help text into a info badges (show
      on hover). Also, render checkboxes using slightly different HTML.
    + Allow to restrict certain models from appearing in the
      ``fobi.contrib.plugins.fields.select_model_object`` list. By default allow
      all models.
    + Implement drag-n-drop (ordering) for foundation 5 theme form.
    + Make sure Django 1.6 is supported.
    + Finish permissions.
    + Fix the style of the "dashboard" page for foundation 5.
    + Fix the style of the "landing" page for foundation 5.
    + Make at least 2 themes (bootstrap 3 + foundation 5).
    + As a prove of concept, write a widget for FeinCMS.
    + Custom text on the thanks page after successful form submission.
    + Add a "simple" theme, which basically has all the functionality, for
      rendering the form, but isn't really styled.
    + Either finish or temporary disable the public/private functionality of
      the form.
    + After "fixes" the main template doesn't seem to work well.
    + Simplify and improve data form handling in form handler plugins.
    + Fix strange thing happend to bootstrap3 layout (handler and form parts
      became much wider).
    + Make it possible to view data submitted to forms you own.
    + The Django admin integration (implemented as a theme). In fact, merged into
      the "simple" theme.
    + Core tests.
    + Create form tests.
    + Create form elements tests.
    + Create form handlers tests.
    + Post form data tests.
    + Improve the UI of the bootstrap 3 theme (add tabs).
    + Improve the UI of the foundation 5 theme (add tabs).
    + Improve the UI of the "simple" theme (add tabs).
    + Make sure drag-n-drop works in the "simple"  theme.
    + Add anchors to the redirected URL in case of failures (tabs issue).
    + Add anchors to the "Simple" theme template (already done for "Bootstrap 3"
      and "Foundation 5" theme.
    + Add "View entries" thingie (form handler tweak) to Foundation 5 and
      the "Simple" themes (as it is already done in Bootstrap 3 theme).
    + In the "Simple" theme add class "default" to the submitt button. Also, rename
      the button to "Save".
    + At the moment, the dashboard of the "simple" theme is not in the
      django-admin design. Make it so.
    + At the moment, the create form view of the "simple" theme is not in the
      django-admin design. Make it so.
    + Style the form handlers table in the edit form view.
    + Split view and edit URLs (place under "urls" sub-module).
    + Fix test "test_2004_submit_form" and "test_4001_add_form_handlers" as they
      produce an error now.
    + Layout issue on edit form view (add elements) when form contains no
      elements. it then looks strange, what shall be fixed.
    + Forbid adding of form elements/handlers in the admin. It should instead
      be synced using the management command ``fobi_sync_plugins``.
    + Add URL field (with configurable validation).
    + Add a date time field (with configurable date format).
    + Add date field (with configurable date format).
    + Edit form element/handler - add breadcrumbs.
    + Add HTML5 fields.
    + Customisable user model.
    + Add radio button field.
    + Add password field.
    + Add styles for radio buttons (doesn't look nice in "simple" theme) or
      make sure they are rendered in a Django way.
    + Make it possible to define a customa action.
    + Get rid of the ``django-dash`` specific code and replace it with what's
      right for the ``django-fobi``.
    + Sort form elements and handlers alphabetically.
    + Completely polish bootstrap3 theme templates.
    + Completely polish foundation5 theme templates.
    + Completely polish simple theme templates.
    + Fix bug with non-appearing plugins (in unicode locales).
    + Delete form element tests.
    + Delete form handler tests.
    + datetime.datetime and datetime.date objects are not JSON serialisable.
      Make sure they are.
    + Fix nasty bug with Bootstrap3 theme (drop-down menu for element selection
      is too short, when form contains no elements yet).
    + Style the radio buttons for Bootstrap 3 and Foundation 5 themes.
    + Clean up all themes.
    + Make a working demo (at the moment fails). NOTE: Test if this is still an
      issue!
    + Awesome documentation.
    + Awesome theming API. Change current one - make a theme to have all the
      templates.
    + Generalise themes as much as possible.
    + Make sure nothing breaks if one or another element has invalid data.
      Instead, make it possible to run `Fobi` in debug mode, where exceptions
      would be raised. With ``DEBUG`` set to False (Fobi own ``DEBUG``) no
      exceptions would be raised and broken fields would not be shown.
    + Add Captcha form element plugin.
    + Make tiny fixes in docs (see emails).
    + Disable HTML5 form validation in edit mode.
    + Add the following attribute to the forms in edit mode
      http://www.w3schools.com/tags/att_input_formnovalidate.asp
    + Add data export features for the ``db_store`` plugin into the "simpe"
      theme as well (same way as already done fore "bootstrap 3" and
      "foundation 5" themes.
    + Clean up the TODOs before first release.
    + In the ``db_store`` plugin README mention that ``xlwt`` package is
      required (optional) for XLS export. If not present, falls back to
      CSV export.
    + Make appropriate additions to the documentation reflecting the changes
      made in 0.3.5 (or 0.4).
    + Fix the CSV/XLS export in ``db_store`` for Django 1.7.
    + Nicer styling for the radio button (Bootstrap 3 theme).
    + Values of `FormElementPlugin` subclassed elements is stored in the `db_store`
      plugin. Make sure it doesn't.
    + Make sure empty lines are not treated as options in the radio or list
      plugins.
    + Django 1.8 support.
    + Add a quickstart documentation.
    + Make a Django-CMS dedicated theme (for the admin) using `djangocms-admin-style
      <https://github.com/divio/djangocms-admin-style>`_.
    + Clean up the Input plugin (some properties of it, like "type" aren't anyhow
      used, while they should be).
    + Add DecimalField.
    + Add FloatField.
    + Add SlugField.
    + NullBooleanField.
    + Add GenericIPAddressField.
    + Add TimeField.
    + See if it's reasonable to use Date and DateTime fields in initial for
      date and datetime plugins.
    + Add RegEx field.
    + At the moment not all the plugin data is nicely serialized. Check which
      plugin causes problems and make a fix.
    + In the mail plugin, send files as attachments.
    + Show how to use (or make use) of `django-crispy-forms
      <https://github.com/maraujop/django-crispy-forms>`_ package in the
      "simple"-like themes.
    + Fix the checkbox select multiple plugin (doesn't post any data).
    + Add CheckboxSelectMultiple field.
    + Make it possible to provide more than one `to` email address in the mail
      form handler plugin.
    + Take default values provided in the `plugin_data_fields` of the plugin
      form into consideration (provide as initial on in the form element creation
      form).
    + `django-mptt` fields.
    + Move the `NoneField` and `NoneWidget` into a separate package.
    + Check if `action` is a valid URL. Make `fobi.models.FormEntry.action` a URL
      field. Make sure relative URLs work as well.
    + Create a error page for the heroku demo, warning that perhaps user had
      chosen a wrong `action`.
    + In the heroku demo app, make a real error page saying - page can't e found.
      Can it be that you mistyped the action URL?
    + Make sure, that theme specific theme javascripts, css and other assets,
      are defined in the theme itself. Follow the ``django-dash``
      example as much as possible.
    + Make it possible to define dynamic values and use then in the form. Let
      developers themselves define what should be in there (some sort of
      register in global scope, maybe just a context processor).
      Make it pluggable and replaceable.
    + Check if it's safe to use the initial dynamic values.
    + In the updated GUI (bootstrap3), if form names are too long, the layout
      doesn't look nice anymore.
    + Somehow, the drag and drop of the form elements got broken. Fix ASAP.
    + Fix layout issue on step 2 of the MailChimp import (step 2 of the wizard).

Should haves
============
.. code-block:: text

    - Add `HBase store` form handler.
    - Add `Mongo store` form handler.
    - Add `Cassandra store` form handler.
    - Add `django-treebeard` field as an alternative (vs MPTT fields).
    - Make sure that all views are 100% AJAX ready.
    - Document the changes.
    - Find out why subclassing the ``select_model_object`` plugin didn't work.
    - Rename the ``simple`` theme into ``django_admin_style_theme``.
    - Make a real ``birthday`` field (with no year selection).
    - Fix the view saved form entries template (nicer look) for Foundation 5
      theme.
    - Finish form importers concept and the MailChimp form importer plugin.
    - Make sure it's possible to assign CSS and JS files to the form handler
      plugins.
    - In the widget for FeinCMS make sure to list the usernames along with
      the form names.
    - Repeat for the form callbacks the same what's already done to prioritise
      the form handlers execution order.
    - Finish the template tag ``get_form_field_type`` which should get the
      field type of the field given.
    - Think of a different URL strategy. Perhaps not a bad idea to have a
      username mentioned in the path, so that the forms are tracked by their
      unique pair (username, slug). That would make the URLs more semantic (
      "barseghyanartur/test-form-1" instead of "test-form-1-N").
    - Once the form ordering has been changed, show a message and warn if user
      is about to leave the page without saving the changes.
    - Make it possible to create fieldsets (implement as containers).
    - Make it possible (just checkbox) to set a fieldset as cloneable.
    - Think of adding hooks so that custom actions are possible without template
      changes (for example, add a new import app for importing the forms from
      MailChimp).
    - Think of making putting several actions (repair) into the management
      interface (UI).
    - Make Django's CSRF validation optional.
    - Quiz mode (randomize the ordering of the form elements).
    + Add Django 1.7 support.
    + Add `max` attribute to the date and datetime fields. Also HTML5.
    + Add an example of how to extend the existing themes with additional
      functionality. For example, how to take a Bootstrap 3 theme, extend it
      by giving it another name and actually giving a custom look to the view
      form template.
    + Make it possible to use a custom user model.
    + Improve the "Simple" theme (Django admin integration part).
    + Place a basic README.rst in each plugin.
    + As another prove of concept, write an integration app for Django-CMS.
    + Add data export features to ``db_store`` plugin.
    + Make 3 base templates for the DjangoCMS integration app. Save things in
      settings and make the template to be chosen depending on the fobi_theme (
      likely, move the declaration of the FOBI_THEME above the declaration of the
      Django-CMS templates).
    + Improve the Django-CMS integration app (make sure it works with
      Django-CMS < 3.0).
    + Add a honeypot field.
    + Move the Captcha field into a separate ``security`` sub module.
    + Rename the ``birthday`` field to ``date_drop_down`` field.
    + At the moment Captcha data is also being saved (db_store form handler).
      Think of fixing that by allowing to exclude certain fields from being
      processed by form handlers.
    + Add a property "allow_multiple" to the form handlers, for form handlers.
    + Make it possible for developers to decide (in settings) what kind of
      values do they want to have saved. By default, return the label for
      select-like fields (`radio`, `select`, `select_multiple`), the str/unicode
      for foreign keys (`select_model_object`, `select_multiple_model_objects`).
      For that, introduce a new setting `SUBMIT_VALUE_AS`. It should be a string
      which allows the following options: "val", "repr", "mixed". Default would
      be the "repr". In that case, the value would be the human readable
      representation of the chosen option. In case of "val", the actual value is
      submitted. Mix is a mix of the "val" and "repr" as "repr (val)". For foreign
      keys, it would be as follows: app.module.pk.value (mix), app.module.pk (val),
      value (repr).
    + Document the `SUBMIT_VALUE_AS` in main documentation and mention in the
      readme of all appropriate plugins.
    + In ``db_store` plugin, at the moment if labels are not unique, some data
      loss happens. Either, make the labels unique in a single form or avoid data
      loss in some other way.
    + Fix the issue with `db_store` plugin and `allow_multiple` property (if
      set to True tests fail).
    + Fix the issue with `initial` for `select_multiple` plugin. At the moment,
      setting initial doesn't seem to work.
    + Make it possible to export form to JSON format. It should be possible to
      re-created form from saved JSON sa well.

Could haves
===========
.. code-block:: text

    - Fix the ``input_format`` option in the date and datetime fields.
    - Think of making it possible to change (or even better - regenerate) the
      form slug (preferably - yes).
    - Add a management command to remove broken form elements.
    - Think of delegating the form rendering completely to third-party library
      like `django-crispy-forms`.
    - Make it possible to use something else than Django's ORM (django-mongoengine,
      SQLAlchemy).
    - Make it possible for themes to override the ``fobi.forms.FormEntryForm``
      form?
    - Make sure a better (SEO) URLs can be used in integration packages (at
      least the FeinCMS).
    - Make sure that the form view return can be overridden?
    - Add datetime range and date range fields.
    - TinyMCE form element cosmetic plugin.
    - In the cosmetic image plugin, render the sized image.
    - Add Armenian translation.
    - Add option to redirect to another page.
    - Make a Django<->Fobi list of supported fields with proper `referencies
      <https://docs.djangoproject.com/en/1.7/ref/forms/fields/>`_.
    - Kube framework integration (theme).
    - PureCSS framework integration (theme).
    - Skeleton framework integration (theme).
    - Baseline framework integration (theme).
    - Amazium framework integration (theme).
    + Configure defaults values of each plugin in projects' settings module.
    + Add Dutch translation.
    + Add Russian translation.
    + Add more HTML5 fields?
    + Finish select multiple model objects plugin (issue with processing form data
      on form submit).
    + Make a django theme for jQuery UI.

Would haves
===========
.. code-block:: text

    - Conditional inputs.
    - Perhaps, completely re-write the base template for the foundation 5 theme?
    - Make it possible to design a form based on existing models.
    + Form wizards (combine forms with each other, having one at a step, finally -
      send it all as one).
