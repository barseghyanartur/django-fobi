import copy
import datetime
import os
from collections import OrderedDict

from django.conf import settings
from django.utils.encoding import force_str
from faker import Faker

from fobi.contrib.plugins.form_elements.content.content_image.fobi_form_elements import (
    ContentImagePlugin,
)
from fobi.contrib.plugins.form_elements.content.content_text.fobi_form_elements import (
    ContentTextPlugin,
)
from fobi.contrib.plugins.form_elements.fields.boolean.fobi_form_elements import (
    BooleanSelectPlugin,
)
from fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple.fobi_form_elements import (
    CheckboxSelectMultipleInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.date.fobi_form_elements import (
    DateInputPlugin,
)
# from fobi.contrib.plugins.form_elements.fields \
#          .date_drop_down.fobi_form_elements import DateDropDownInputPlugin
from fobi.contrib.plugins.form_elements.fields.datetime.fobi_form_elements import (
    DateTimeInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.decimal.fobi_form_elements import (
    DecimalInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.email.fobi_form_elements import (
    EmailInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.file.fobi_form_elements import (
    FileInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.float.fobi_form_elements import (
    FloatInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.hidden.fobi_form_elements import (
    HiddenInputPlugin,
)
# from fobi.contrib.plugins.form_elements.fields.hidden_model_object \
#          .fobi_form_elements import HiddenModelObjectInputPlugin
from fobi.contrib.plugins.form_elements.fields.integer.fobi_form_elements import (
    IntegerInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.ip_address.fobi_form_elements import (
    IPAddressInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.null_boolean.fobi_form_elements import (
    NullBooleanSelectPlugin,
)
from fobi.contrib.plugins.form_elements.fields.select.fobi_form_elements import (
    SelectInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.select_model_object.fobi_form_elements import (
    SelectModelObjectInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.select_multiple.fobi_form_elements import (
    SelectMultipleInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.select_multiple_with_max.fobi_form_elements import (
    SelectMultipleWithMaxInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.slug.fobi_form_elements import (
    SlugInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.text.fobi_form_elements import (
    TextInputPlugin,
)
from fobi.contrib.plugins.form_elements.fields.textarea.fobi_form_elements import (
    TextareaPlugin,
)
from fobi.contrib.plugins.form_elements.fields.url.fobi_form_elements import (
    URLInputPlugin,
)
from fobi.contrib.plugins.form_handlers.db_store.fobi_form_handlers import (
    DBStoreHandlerPlugin,
)
from fobi.contrib.plugins.form_handlers.http_repost.fobi_form_handlers import (
    HTTPRepostHandlerPlugin,
)
from fobi.contrib.plugins.form_handlers.mail.fobi_form_handlers import (
    MailHandlerPlugin,
)
from fobi.contrib.plugins.form_handlers.mail_sender.fobi_form_handlers import (
    MailSenderHandlerPlugin,
)

# from decimal import Decimal


# from fobi.contrib.plugins.form_elements.content \
#          .content_video.fobi_form_elements import ContentVideoPlugin


__title__ = "fobi.tests.data"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2019 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = (
    "TEST_DYNAMIC_FORMS_DEFINITION_DATA",
    "TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF",
    # 'TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF_NEGATIVE',
    "TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE",
    "TEST_DYNAMIC_FORMS_PUT_DATA",
    "TEST_DYNAMIC_FORMS_PUT_DATA_ALL",
    "TEST_FORM_ELEMENT_PLUGIN_DATA",
    "TEST_FORM_FIELD_DATA",
    "TEST_FORM_HANDLER_PLUGIN_DATA",
    "TEST_MAILCHIMP_IMPORTER_FORM_DATA",
)

TEST_FORM_ELEMENT_PLUGIN_DATA = {
    # Add a "Boolean (checkbox)" plugin.
    force_str(BooleanSelectPlugin.name): {
        "label": "Test boolean",
        "help_text": "Lorem ipsum boolean",
        "required": False,
    },
    # Add a "Date" input form element
    force_str(DateInputPlugin.name): {
        "label": "Test date input",
        "help_text": "Lorem ipsum select multiple input",
        "required": False,
    },
    # Add a "DateTime" input form element
    force_str(DateTimeInputPlugin.name): {
        "label": "Test datetime input",
        "help_text": "Lorem ipsum select multiple input",
        "required": False,
    },
    # Add an decimal input plugin
    force_str(DecimalInputPlugin.name): {
        "label": "Test decimal input",
        "help_text": "Lorem ipsum email",
        "required": True,
    },
    # Add an email input plugin
    force_str(EmailInputPlugin.name): {
        "label": "Test email input",
        "help_text": "Lorem ipsum email",
        "required": True,
    },
    # Add a "File" (file) form element
    force_str(FileInputPlugin.name): {
        "label": "Test file input",
        # 'name': "test_file_input",
        "help_text": "Lorem ipsum file",
        "required": False,
    },
    # Add an float input plugin
    force_str(FloatInputPlugin.name): {
        "label": "Test float input",
        "help_text": "Lorem ipsum email",
        "required": True,
    },
    # TODO: Find out why selenium fails here!
    # Add a "Hidden" (boolean) form element
    # force_str(HiddenInputPlugin.name): {
    #     'label': "Test hidden input",
    #     #'name': "test_hidden_input",
    #     'help_text': "Lorem ipsum hidden",
    #     'required': True,
    #     },
    # Add a "Integer" (text input) form element
    force_str(IntegerInputPlugin.name): {
        "label": "Test integer",
        "help_text": "Lorem ipsum text input",
        "required": True,
    },
    # Add a "IP address" (text input) form element
    force_str(IPAddressInputPlugin.name): {
        "label": "Test IP address",
        "help_text": "Lorem ipsum text input",
        "required": True,
    },
    # Add a "null boolean" form element
    force_str(NullBooleanSelectPlugin.name): {
        "label": "Test null boolean",
        "help_text": "Lorem ipsum text input",
        "required": True,
    },
    # Add a "Select Input" (select input) form element
    force_str(SelectInputPlugin.name): {
        "label": "Test select",
        "help_text": "Lorem ipsum text input",
        "required": False,
        "choices": "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },
    # Add a "Select model object" (select input) form element
    force_str(SelectModelObjectInputPlugin.name): {
        "label": "Test select model object",
        "help_text": "Lorem ipsum select model object input",
        "required": False,
    },
    # Add a "Select multiple" (select multiple input) form element
    force_str(SelectMultipleInputPlugin.name): {
        "label": "Test select multiple input",
        "help_text": "Lorem ipsum select multiple input",
        "required": False,
        "choices": "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },
    # Add a "Select multiple with max" (select multiple with max input) form
    # element
    force_str(SelectMultipleWithMaxInputPlugin.name): {
        "label": "Test select multiple with max input",
        "help_text": "Lorem ipsum select multiple with max input",
        "required": False,
        "choices": "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },
    # Add a "Checkbox select multiple" (checkbox select multiple input) form
    # element
    force_str(CheckboxSelectMultipleInputPlugin.name): {
        "label": "Test checkbox select multiple input",
        "help_text": "Lorem ipsum checkbox select multiple input",
        "required": False,
        "choices": "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },
    # Add a "Slug" (slug input) form element
    force_str(SlugInputPlugin.name): {
        "label": "Test slug input",
        "help_text": "Lorem ipsum select multiple input",
        "required": False,
    },
    # Add a "Text" (text input) form element
    force_str(TextInputPlugin.name): {
        "label": "Test text",
        "help_text": "Lorem ipsum text input",
        "required": True,
    },
    # Add a "Textarea" (text area) form element
    force_str(TextareaPlugin.name): {
        "label": "Test text area",
        "help_text": "Lorem ipsum text area",
        "required": True,
    },
    # Add a "URL input" form element
    force_str(URLInputPlugin.name): {
        "label": "Test URL input",
        "help_text": "Lorem ipsum text area",
        "required": True,
    },
    # Add a "Text" (text input) form element
    # force_str(TextInputPlugin.name): {
    #     'label': u"Անուն",
    #     'help_text': u"Անուն",
    #     'required': True,
    # },
}

TEST_FORM_FIELD_DATA = {
    "test_boolean": True,
    # 'test_checkbox_select_multiple_input': '',
    "test_date_input": datetime.date.today().strftime("%d-%m-%Y"),
    "test_datetime_input": datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "test_decimal_input": "10.01",  # Decimal(10.01),
    "test_email_input": "john@doe.net",
    "test_file_input": os.path.join(
        settings.MEDIA_ROOT,
        "testing",
        "delusional_insanity_-_karima_van_der_voort.jpg",
    ),
    "test_float_input": "10.01",
    # 'test_hidden_input': '',
    "test_integer": "2014",
    "test_null_boolean": False,
    "test_ip_address": "127.0.0.1",
    "test_select": "",
    "test_select_model_object": "",
    "test_select_multiple_input": "",
    "test_slug_input": "lorem-ipsum",
    "test_text": "Lorem ipsum",
    "test_text_area": "Dolor sit amet",
    "test_url_input": "http://dev.example.com",
    # 'test_unicode_text': u'Անուն',
}

# Order of the elements matters a lot, since `Mail` and `Mail the sender`
# both share the `Mail` word. If order isn't taken into consideration,
# it may happen that the wrong plugin is detected (occasional on Python2).
# Therefore, an ordered dict. Note that `MailSenderHandlerPlugin` shall
# be placed before the `MailHandlerPlugin`.
TEST_FORM_HANDLER_PLUGIN_DATA = OrderedDict(
    [
        (force_str(DBStoreHandlerPlugin.name), None),
        (
            force_str(MailSenderHandlerPlugin.name),
            {
                "from_name": "From me",
                "from_email": "from@example.com",
                "to_name": "To you",
                "form_field_name_to_email": "test_email_input",
                "subject": "Test email subject",
                "body": "Test email body",
            },
        ),
        (
            force_str(MailHandlerPlugin.name),
            {
                "from_name": "From me",
                "from_email": "from@example.com",
                "to_name": "To you",
                "to_email": "to@example.com",
                "subject": "Test email subject",
                "body": "Test email body",
            },
        ),
        (
            force_str(HTTPRepostHandlerPlugin.name),
            {"endpoint_url": "http://dev.example.com"},
        ),
    ]
)

TEST_MAILCHIMP_IMPORTER_FORM_DATA = [
    {
        "default": "",
        "field_type": "email",
        "helptext": "",
        "id": 0,
        "name": "Email Address",
        "order": "1",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "EMAIL",
    },
    {
        "default": "",
        "field_type": "text",
        "helptext": "",
        "id": 1,
        "name": "First Name",
        "order": "2",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "FNAME",
    },
    {
        "default": "",
        "field_type": "text",
        "helptext": "",
        "id": 2,
        "name": "Last Name",
        "order": "3",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "LNAME",
    },
    {
        "default": "",
        "field_type": "text",
        "helptext": "",
        "id": 3,
        "name": "Organisation",
        "order": "4",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "ORG",
    },
    {
        "default": "Type Text Default Value",
        "field_type": "text",
        "helptext": "Type Text Help Text",
        "id": 4,
        "name": "type_text",
        "order": "5",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_TEXT",
    },
    {
        "default": "1",
        "field_type": "number",
        "helptext": "Type Number Help Text",
        "id": 5,
        "name": "type_number",
        "order": "6",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "TYPE_NUMBE",
    },
    {
        "choices": ["First Choice", "Second Choice", "Third Choice"],
        "default": "Second Choice",
        "field_type": "radio",
        "helptext": "Type Radio Buttons Help Text",
        "id": 6,
        "name": "type_radio_buttons",
        "order": "7",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_RADIO",
    },
    {
        "choices": ["First Choice", "Second Choice", "Third Choice"],
        "default": "Third Choice",
        "field_type": "dropdown",
        "helptext": "Drop Down Help Text",
        "id": 7,
        "name": "type_drop_down",
        "order": "9",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_DROPD",
    },
    {
        "dateformat": "MM/DD/YYYY",
        "default": "",
        "field_type": "date",
        "helptext": "Type Date Help Text",
        "id": 8,
        "name": "type_date",
        "order": "10",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_DATE",
    },
    {
        "dateformat": "MM/DD",
        "default": "",
        "field_type": "birthday",
        "helptext": "Type Birthday Help Text",
        "id": 9,
        "name": "type_birthday",
        "order": "11",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_BIRTH",
    },
    {
        "default": "",
        "defaultcountry": "109",
        "defaultcountry_cc": "NL",
        "defaultcountry_name": "Netherlands",
        "field_type": "address",
        "helptext": "Type Address Help Text",
        "id": 10,
        "name": "type_address",
        "order": "12",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "TYPE_ADDRE",
    },
    {
        "default": "",
        "field_type": "zip",
        "helptext": "Type Zip Code Help Text",
        "id": 11,
        "name": "type_zip_code",
        "order": "13",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "TYPE_ZIP_C",
    },
    {
        "default": "",
        "field_type": "phone",
        "helptext": "Type Phone Help Text",
        "id": 12,
        "name": "type_phone",
        "order": "14",
        "phoneformat": "none",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "TYPE_PHONE",
    },
    {
        "default": "",
        "field_type": "url",
        "helptext": "Type Website Help Text",
        "id": 13,
        "name": "type_website",
        "order": "15",
        "public": True,
        "req": True,
        "show": True,
        "size": "25",
        "tag": "TYPE_WEBSI",
    },
    {
        "default": "",
        "field_type": "imageurl",
        "helptext": "Type Image Help Text",
        "id": 14,
        "name": "type_image",
        "order": "16",
        "public": True,
        "req": False,
        "show": True,
        "size": "25",
        "tag": "TYPE_IMAGE",
    },
]

TEST_DYNAMIC_FORMS_DEFINITION_DATA = OrderedDict(
    [
        (
            "username",
            (
                TextInputPlugin.uid,
                "{"
                '"name": "username", '
                '"required": true, '
                '"max_length": 200, '
                '"label": "Username", '
                '"placeholder": "delusionalinsanity"'
                "}",
            ),
        ),
        (
            "email",
            (
                EmailInputPlugin.uid,
                "{"
                '"name": "email", '
                '"required": true, '
                '"label": "E-mail"'
                "}",
            ),
        ),
        (
            "age",
            (
                IntegerInputPlugin.uid,
                "{"
                '"name": "age", '
                '"required": true, '
                '"max_value": 200, '
                '"label": "Age"'
                "}",
            ),
        ),
        (
            "drivers_license",
            (
                BooleanSelectPlugin.uid,
                "{"
                '"name": "drivers_license", '
                '"required": false, '
                '"label": "Drivers license?"'
                "}",
            ),
        ),
        (
            "special_fields",
            (
                HiddenInputPlugin.uid,
                "{"
                '"name": "special_fields", '
                '"required": false, '
                '"label": "Special fields"'
                "}",
            ),
        ),
        (
            "ignore_01",
            (
                ContentImagePlugin.uid,
                "{"
                '"fit_method": "center", '
                '"file": "fobi_plugins/content_plugin_images/'
                '04.jpg", '
                '"alt": "Cute girl"'
                "}",
            ),
        ),
        (
            "number_of_children",
            (
                IntegerInputPlugin.uid,
                "{"
                '"name": "number_of_children", '
                '"required": false, '
                '"label": "Number of children"'
                "}",
            ),
        ),
        # (
        #     'sample_decimal',
        #     (
        #         DecimalInputPlugin.uid,
        #         '{'
        #         '"name": "sample_decimal", '
        #         '"required": false, '
        #         '"label": "Sample decimal"'
        #         '}'
        #     )
        # ),
        (
            "bio",
            (
                TextareaPlugin.uid,
                "{" '"name": "bio", ' '"required": true, '
                # '"max_length": null',
                '"label": "Biography"' "}",
            ),
        ),
        (
            "ignore_02",
            (
                ContentTextPlugin.uid,
                "{"
                '"text": "Suspendisse potenti. Etiam in nunc '
                "sodales, congue lectus ut, suscipit massa. In "
                "commodo fringilla orci, in varius eros gravida "
                "a! Aliquam erat volutpat. Donec sodales orci nec "
                "massa aliquam bibendum. Aenean sed condimentum "
                "velit. Mauris luctus bibendum nulla vel tempus. "
                "Integer tempor condimentum ligula sed feugiat. "
                "Aenean scelerisque ultricies vulputate. Donec "
                'semper lorem rhoncus sem cras amet."'
                "}",
            ),
        ),
        # (
        #     'unicode_name',
        #     (
        #         TextInputPlugin.uid,
        #         '{'
        #         '"name": "unicode_name", '
        #         '"required": true, '
        #         '"max_length": 200, '
        #         '"label": u"Անուն", '
        #         '"placeholder": u"Անուն"'
        #         '}'
        #     )
        # ),
    ]
)

TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF = copy.deepcopy(
    TEST_DYNAMIC_FORMS_DEFINITION_DATA
)
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop("ignore_01")
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop("ignore_02")
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop("special_fields")

# TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF_NEGATIVE = copy.copy(
#     TEST_DYNAMIC_FORMS_DEFINITION_DATA
# )
#
# for __key, __value
#         in TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF_NEGATIVE.items():
#     if __key not in ('special_fields',):
#         TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF_NEGATIVE.pop(__key)

FAKER = Faker()

TEST_DYNAMIC_FORMS_PUT_DATA_ALL = {
    "username": FAKER.user_name(),
    "email": FAKER.email(),
    "age": FAKER.random_int(min=0, max=200),
    "drivers_license": FAKER.pybool(),
    "special_fields": FAKER.pystr(),
    "number_of_children": FAKER.pyint(),
    # 'sample_decimal': "%.5f" % FAKER.pydecimal(
    #     left_digits=3,
    #     right_digits=5,
    #     positive=True
    # ),
    "bio": FAKER.text(),
    # 'unicode_name': u'Անուն',
}

TEST_DYNAMIC_FORMS_PUT_DATA = copy.copy(TEST_DYNAMIC_FORMS_PUT_DATA_ALL)
TEST_DYNAMIC_FORMS_PUT_DATA.pop("special_fields")

TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE = OrderedDict(
    [
        (
            "username",
            OrderedDict(
                [
                    ("type", "string"),
                    ("required", True),
                    ("read_only", False),
                    ("label", "Username"),
                    ("max_length", 200),
                    ("placeholder", "delusionalinsanity"),
                ]
            ),
        ),
        (
            "email",
            OrderedDict(
                [
                    ("type", "email"),
                    ("required", True),
                    ("read_only", False),
                    ("label", "E-mail"),
                    ("max_length", 255),
                ]
            ),
        ),
        (
            "age",
            OrderedDict(
                [
                    ("type", "integer"),
                    ("required", True),
                    ("read_only", False),
                    ("label", "Age"),
                    ("max_value", 200),
                ]
            ),
        ),
        (
            "drivers_license",
            OrderedDict(
                [
                    ("type", "boolean"),
                    ("required", False),
                    ("read_only", False),
                    ("label", "Drivers license?"),
                ]
            ),
        ),
        # (u'special_fields', OrderedDict([(u'type', u'field'),
        #                                  (u'required', False),
        #                                  (u'read_only', False),
        #                                  (u'label', u'Special fields')])),
        (
            "number_of_children",
            OrderedDict(
                [
                    ("type", "integer"),
                    ("required", False),
                    ("read_only", False),
                    ("label", "Number of children"),
                ]
            ),
        ),
        # (u'sample_decimal', OrderedDict([(u'type', u'decimal'),
        #                                  (u'required', False),
        #                                  (u'read_only', False),
        #                                  (u'label', u'Sample decimal'),
        #                                  ('max_digits', 10),
        #                                  ('decimal_places', 5)])),
        (
            "bio",
            OrderedDict(
                [
                    ("type", "string"),
                    ("required", True),
                    ("read_only", False),
                    ("label", "Biography"),
                ]
            ),
        ),
        # (u'unicode_name', OrderedDict([(u'type', u'string'),
        #                                (u'required', True),
        #                                (u'read_only', False),
        #                                (u'label', u'Անուն'),
        #                                (u'max_length', 200),
        #                                (u'placeholder', u'Անուն')])),
    ]
)
