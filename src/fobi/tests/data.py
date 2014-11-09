__title__ = 'fobi.tests.data'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TEST_FORM_ELEMENT_PLUGIN_DATA', 'TEST_FORM_FIELD_DATA',
    'TEST_FORM_HANDLER_PLUGIN_DATA',
    )

from django.utils.text import force_text

from fobi.contrib.plugins.form_elements.content.content_text.fobi_form_elements \
    import ContentTextPlugin
from fobi.contrib.plugins.form_elements.content.content_image.fobi_form_elements \
    import ContentImagePlugin

from fobi.contrib.plugins.form_elements.fields.boolean.fobi_form_elements \
    import BooleanSelectPlugin
from fobi.contrib.plugins.form_elements.fields.email.fobi_form_elements \
    import EmailPlugin
from fobi.contrib.plugins.form_elements.fields.file.fobi_form_elements \
    import FileInputPlugin
from fobi.contrib.plugins.form_elements.fields.hidden.fobi_form_elements \
    import HiddenInputPlugin
from fobi.contrib.plugins.form_elements.fields.integer.fobi_form_elements \
    import IntegerInputPlugin
from fobi.contrib.plugins.form_elements.fields.select.fobi_form_elements \
    import SelectInputPlugin
from fobi.contrib.plugins.form_elements.fields.select_model_object.fobi_form_elements \
    import SelectModelObjectInputPlugin
from fobi.contrib.plugins.form_elements.fields.select_multiple.fobi_form_elements \
    import SelectMultipleInputPlugin
from fobi.contrib.plugins.form_elements.fields.text.fobi_form_elements \
    import TextInputPlugin
from fobi.contrib.plugins.form_elements.fields.textarea.fobi_form_elements \
    import TextareaPlugin

from fobi.contrib.plugins.form_handlers.db_store.fobi_form_handlers \
    import DBStoreHandlerPlugin
from fobi.contrib.plugins.form_handlers.mail.fobi_form_handlers \
    import MailHandlerPlugin
from fobi.contrib.plugins.form_handlers.http_repost.fobi_form_handlers \
    import HTTPRepostHandlerPlugin

TEST_FORM_ELEMENT_PLUGIN_DATA = {
    force_text(BooleanSelectPlugin.name): {
        'label': "Test boolean",
        'help_text': "Lorem ipsum boolean",
        'required': False,
    },
    force_text(EmailPlugin.name): {
        'label': "Test email input",
        'help_text': "Lorem ipsum email",
        'required': True,
    },

    # TODO: Add file test.
    # Add a "File" (file) form elelement
    # force_text(FileInputPlugin.name): {
    #     'label': "Test file input",
    #     #'name': "test_file_input",
    #     'help_text': "Lorem ipsum hidden",
    #     'required': False,
    #     },

    # TODO: Find out why selenium fails here!
    # Add a "Hidden" (boolean) form elelement
    # force_text(HiddenInputPlugin.name): {
    #     'label': "Test hidden input",
    #     #'name': "test_hidden_input",
    #     'help_text': "Lorem ipsum hidden",
    #     'required': True,
    #     },

    # Add a "Integer" (text input) form elelement
    force_text(IntegerInputPlugin.name): {
        'label': "Test integer",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },
    # Add a "Select Input" (select input) form elelement
    force_text(SelectInputPlugin.name): {
        'label': "Test select",
        'help_text': "Lorem ipsum text input",
        'required': False,
    },

    # Add a "Select model object" (select input) form elelement
    force_text(SelectModelObjectInputPlugin.name): {
        'label': "Test select model object",
        'help_text': "Lorem ipsum select model object input",
        'required': False,
    },

    # Add a "Select multiple" (select multiple input) form elelement
    force_text(SelectMultipleInputPlugin.name): {
        'label': "Test select multiple input",
        'help_text': "Lorem ipsum select multiple input",
        'required': False,
    },

    # Add a "Text" (text input) form elelement
    force_text(TextInputPlugin.name): {
        'label': "Test text",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },

    # Add a "Textarea" (text area) form elelement
    force_text(TextareaPlugin.name): {
        'label': "Test text area",
        'help_text': "Lorem ipsum text area",
        'required': True,
    }
}

TEST_FORM_FIELD_DATA = {
    'test_boolean': True,
    'test_email_input': 'john@doe.net',
    #'test_file_input': '',
    #'test_hidden_input': '',
    'test_integer': 2014,
    'test_select': '',
    'test_select_model_object': '',
    'test_select_multiple_input': '',
    'test_text': 'Lorem ipsum',
    'test_text_area': 'Dolor sit amet',
}

TEST_FORM_HANDLER_PLUGIN_DATA = {
    force_text(DBStoreHandlerPlugin.name): None,
    force_text(MailHandlerPlugin.name): {
        'from_name': "From me",
        'from_email': "from@example.com",
        'to_name': "To you",
        'to_email': "to@example.com",
        'subject': "Test email subject",
        'body': "Test email body",
    },
    force_text(HTTPRepostHandlerPlugin.name): {
        'endpoint_url': 'http://dev.example.com'
    }
}
