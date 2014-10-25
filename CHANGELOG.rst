Release history
=====================================
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

- Minor fixes in the `Integer` form element plugin.
- Minor fixes in the `Input` form element plugin.
- Minor fixes in themes (disable HTML5 form validation in edit mode).
- Minor documentation improvements.

0.1.4
-------------------------------------
2014-10-22

- Minor core improvements.
- Django 1.5 support improvements.
- Django 1.7 support improvements.
- Added `Captcha` form element plugin.
- Added highly-customisable `Input` form element plugin - a custom input field
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
