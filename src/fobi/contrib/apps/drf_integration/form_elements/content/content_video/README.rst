fobi.contrib.apps.drf_integration.form_elements.content.content_video
#####################################################################
A ``django-fobi`` ContentVideo plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentVideo``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_video``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_video',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentVideo`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_video_41a6b951-e6f9-4f08-ada6-3b109aa9a72f": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "video",
                "content": "\n<iframe src=\"//www.youtube.com/embed/3P1qcVcs4Ik\" width=\"500\" height=\"400\" frameborder=\"0\" allowfullscreen></iframe>\n",
                "raw": {
                    "title": "Cras risus ipsum faucibus",
                    "url": "https://www.youtube.com/watch?v=3P1qcVcs4Ik",
                    "size": "500x400"
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "video" for ``ContentVideo`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentVideo`` plugin. Contains
  "title", "url" and "size" attributes.
