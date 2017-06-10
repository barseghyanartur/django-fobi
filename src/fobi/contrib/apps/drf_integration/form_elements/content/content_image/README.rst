fobi.contrib.apps.drf_integration.form_elements.content.content_image
#####################################################################
A ``django-fobi`` ContentImage plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentImage``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_image``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_image',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentImage`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_image_89c8c319-195b-487a-a44d-f59ef14a5d44": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "image",
                "content": "\n<p>\n\n\n\n\n<img src=\"/media/fobi_plugins/content_image/test-image-thumbnail.jpg\" alt=\"Lorem ipsum\"/>\n\n\n</p>\n",
                "raw": {
                    "file": "/media/fobi_plugins/content_image/test-image.jpg",
                    "alt": "Lorem ipsum",
                    "fit_method": "center",
                    "size": "500x500"
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "image" for ``ContentImage`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentImage`` plugin. Contains
  "file", "alt", "fit_method" and "size" attributes.
