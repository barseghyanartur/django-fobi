===============================================
TODOs
===============================================
Based on the MoSCoW principle. Must haves and should haves are planned to be
worked on.

* Features/issues marked with plus (+) are implemented/solved.
* Features/issues marked with minus (-) are yet to be implemented.

Must haves
===============================================
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
  scheck other fields of Django formfield). In formfield plugins, subclass
  from BaseFormFieldPlugin, instead of the BaseFormElementPlugin.
+ In the view, validate the form fields (if they are sublcass of
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
+ Awesome themeing API. Change current one - make a theme to have all the
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
- Nicer styling for the radio button (Foundation 5 theme).
- Nicer styling for the radio button (Simple theme).
- Make it possible to provide an alternative rendering of the form field
  in the correspondent form field plugin widget (in such a way, that it
  falls back to the defaut rendering when no custom is available and
  uses the custom rendering if available). This should be done on the
  widget level, so that it's not necessary to update the theme in case of
  customisations made for one or more form field plugins (the rendering
  part).
- Make sure, that theme specific theme javascripts, css and other assets,
  are defined in the theme itself. Follow the ``django-dash``
  example as much as possible.
- Improve the "simple" theme for Django 1.6 and Django 1.7 (tiny bits of 
  styling).
- Finish the Input plugin (some properties of it, like "type" aren't anyhow
  used, while they should be).
- Edit form test.
- Edit form element tests.
- Edit from handler tests.
- Delete form tests.
- List all settings overrides in docs https://github.com/barseghyanartur/django-fobi#tuning
- Add tox tests.

Should haves
===============================================
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
  likely, move the declation of the FOBI_THEME above the declaration of the
  Django-CMS templates).
+ Improve the Django-CMS integration app (make sure it works with
  Django-CMS < 3.0).
+ Add a honeypot field.
+ Move the Captcha field into a separate ``security`` sub module.
+ Rename the ``birthday`` field to ``date_drop_down`` field.
+ At the moment Captcha data is also being saved (db_store form handler).
  Think of fixing that by allowing to exclude certain fields from being
  processed by form handlers.
- Make a real ``birthday`` field (with no year selection).
- Make it possible to use something else than Django's ORM (django-mongoengine,
  SQLAlchemy).
- Fix the view saved form entries template (nicer look) for Foundation 5
  theme.
- Fix the ``input_format`` option in the date and datetime fields.
- Finish form importers concept and the MailChimp form importer plugin.
- Make sure it's possible to assign CSS and JS files to the form handler
  plugins.
- Think of making it possible to change (or even better - regenerate) the
  form slug (preferrably - yes).
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
- In ``db_store` plugin, at the moment if labels are not unique, some data 
  loss happens. Either, make the labels unique in a single form or avoid data
  loss in some other way.
- Make it possible to create fieldsets (implement as containers).
- Think of adding hooks so that custom actions are possible without template
  changes (for example, add a new import app for importing the forms from
  MailChimp).
- Add a management command to remove broken form elements.
- Think of making putting several actions (repair) into the management
  interface (UI).
- Make Django's CSRF validation optional.
- Make sure a better (SEO) URLs can be used in intergration packages (at
  least the FeinCMS).

Could haves
===============================================
+ Add Dutch translation.
+ Add Russian translation.
+ Add more HTML5 fields?
- Make it possible for themes to override the ``fobi.forms.FormEntryForm``
  form?
- Make it possible to design a form based on existing models.
- Make sure that the form view return can be overridden?
- Add datetime range and date range fields.
- Add a property "allow_multiple" to the form handlers, for form handlers.
- Make a django theme for jQuery UI.
- Base fieldset. Allow users to add more than one field to a fieldset.
- Make it possible (just checkbox) to set a fieldset as clonable.
- Confugure defaults values of each plugin in projects' settings module.
- TinyMCE form element cosmetic plugin.
- In the cosmetic image plugin, render the sized image.
- Add Armenian translation.
- Finish select multiple model objects plugin (issue with processing form data
  on form submit).
- Add option to redirect to another page.
- Conditional inputs.
- Form wizards (combine forms with each other, having one at a step, finally -
  send it all as one).
- Perhaps, completely re-write the base template for the foundation 5 theme?

Would haves
===============================================
