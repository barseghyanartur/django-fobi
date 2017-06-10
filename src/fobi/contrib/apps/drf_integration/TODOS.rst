TODOS
=====
Based on MoSCoW principle.

* Features/issues marked with plus (+) are implemented/solved.
* Features/issues marked with minus (-) are yet to be implemented.

Must haves
----------
.. code-block:: text

    - Improve documentation.
    - Add more meta options for special fields, such as ``slider``.
    - Move DRF NoneField to the ``django-nonefield`` package (contrib).
    - Add PhoneNumberField plugin. Most of the work on
      (serializer) has already been done in the
      `django-phonenumber-field
      <https://github.com/stefanfoulis/django-phonenumber-field>`_, so just make
      use of it.
    + Correct OPTIONS call.
    + Add custom field instance handler for handling data of the custom field
      instances. Do it this way and not the other way, since things get
      complicated when we start to deal with wizards.
    + Find out how to handle further the submitted data? It should be in
      accordance with ``fobi`` concepts of loosely couple parts. After successful
      submission, the ``fobi`` form callbacks, handlers and that kind of things
      should be fired for the given form entry. Thus, it should likely be the
      same in this case. Probably each CustomFieldInstancePlugin should get
      a method ``drf_submit_plugin_form_data``, which should mimic the
      ``submit_plugin_form_data` of the ``fobi.base``. It should also contain
      code for ``drf_fire_form_callbacks`` (mimic ``fire_form_callbacks``).
    + Find out why setting initial values for integer field breaks.
    + Write some basic tests for DRF integration.
    + Finish existing core fields (without relation- and presentational- fields
      yet).
    + Add ``mail`` and ``http_repost`` DRF handler plugins.
    + Add/finish documentation.
    + In DRF listing view, if user isn't authenticated, show only public forms.
    + Fix Python3 issues with ``slider`` and ``range`` select plugins.
    + Fixed Python3 issues with max_length for text fields.
    + In decimal plugin, if any of the values are None, don't try to cast them
      into Decimal.
    + Fix this https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/apps/drf_integration/views.py#L151
      It should not be form = ... but serializer = ...

Should haves
------------
.. code-block:: text

    - Somehow, the ``file`` plugin data, when submitted, isn't shown properly in
      the posted data (by DRF), although is posted 100% correctly.
    - In the API form view, use memoize technique or cache the value somehow to
      reduce the number of queries.
    - Add more fields (relation fields: at least ``select_model_object`` and
      ``select_multiple_model_objects``).
    + Find why HiddenInput tests fail (in terms of Django REST framework it's
      a read-only field).
    + Add Integration form callbacks for handling data of the integration plugins.
    + Add ``date_drop_down`` plugin.
    + Think of what to do with presentational fields (perhaps just display?)

Could haves
-----------
.. code-block:: text

    - Finally implement DRF integration for form-wizards as well.

Would haves
-----------
.. code-block:: text

    + Remove codebin.py at the end.
