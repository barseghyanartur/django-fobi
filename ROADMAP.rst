Changelog for upcoming releases
===============================
0.7
---
yyyy-mm-ddd (upcoming).

- Fieldsets.

0.6
---
yyyy-mm-ddd (upcoming).

This release contains minor backwards incompatible changes, related to the
change of the name of the "simple" theme into "django_admin_style" theme.

- Mailchimp support.
- Kube framework integration (theme).
- PureCSS framework integration (theme).
- Skeleton framework integration (theme).
- Baseline framework integration (theme).
- Amazium framework integration (theme).
- The "simple" theme has been renamed to "django_admin_style".
- Internally, make a date when form has been created. Also keep track of when
  the form has been last edited.

0.5.6
-----
yyyy-mm-dd (upcoming).

- Export/import forms saved as JSON. Validate the imports and mention that
  some plugins are not installed if there are plugins that should be installed
  first.
- `django-mptt` form- and model- fields (`select_mptt_model_object` and
  `select_multiple_mptt_model_objects`).
- Made it possible to define dynamic fields and use then in the form. Let
  developers themselves define what should be in there and the contents of it
  (pluggable and replaceable).
