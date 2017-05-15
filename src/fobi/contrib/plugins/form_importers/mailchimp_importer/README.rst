mailchimp_importer
------------------
A ``django-fobi`` integration with MailChimp.

This plugin makes it possible to import a form from a MailChimp list. A typical
list URL would be `this <https://us5.admin.mailchimp.com/lists/>`_. In the
listing you would see list names and `Stats` at the right corner. If you click
on it you would see the `Settings` link. Follow it and scroll to the bottom for
the unique id for your list. Now, if you have been successfully authenticated
to the MailChimp API using your API_KEY, you could call the `lists.merge_vars`
method for getting the form. API_KEY could be obtained from the MailChimp
in the `Account API <https://us5.admin.mailchimp.com/account/api/>`_.

For additional information on MailChimp import see the following `article
<http://kb.mailchimp.com/lists/managing-subscribers/manage-list-and-signup-form-fields>`_.

Prerequisites
~~~~~~~~~~~~~
Python wrapper for the Mailchimp:

.. code-block:: sh

   pip install mailchimp

If you are using Django 1.8 or greater, you would need `django-formtools`
package as well:

.. code-block:: sh

   pip install django-formtools

Installation
~~~~~~~~~~~~
your_project/settings.py
########################
.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'fobi.contrib.plugins.form_importers.mailchimp_importer',
    ]

How it works
~~~~~~~~~~~~
Assuming that you have configured the `mailchimp_importer` plugin properly and
have the Django running locally on port 8000, accessing the following URL would
bring you to the MailChimp form import wizard.

- http://localhost:8000/en/fobi/forms/importer/mailchimp/

On the first step you would be asked to provide your API_KEY, which is used
to authenticate to the MailChimp in order to fetch your list- and form-
information. The key isn't stored/saved/remembered. Next time you want to
import a form from the same account, you would have to provide it again.

Development status
~~~~~~~~~~~~~~~~~~
This part of code is alpha, which means it experimental and needs improvements.

See the `TODOS <https://raw.githubusercontent.com/barseghyanartur/django-fobi/master/TODOS.rst>`_
for the full list of planned-, pending- in-development- or to-be-implemented
features.

If you want to improve it or did make it working, please, make a pull request.
