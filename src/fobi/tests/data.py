# from __future__ import unicode_literals
import copy
from collections import OrderedDict
import datetime
import os
# from decimal import Decimal

from django.conf import settings
from django.utils.encoding import force_text

from faker import Faker

from fobi.contrib.plugins.form_elements.content \
         .content_image.fobi_form_elements import ContentImagePlugin
from fobi.contrib.plugins.form_elements.content \
         .content_text.fobi_form_elements import ContentTextPlugin
# from fobi.contrib.plugins.form_elements.content \
#          .content_video.fobi_form_elements import ContentVideoPlugin

from fobi.contrib.plugins.form_elements.fields \
         .boolean.fobi_form_elements import BooleanSelectPlugin
from fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple \
         .fobi_form_elements import CheckboxSelectMultipleInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .date.fobi_form_elements import DateInputPlugin
# from fobi.contrib.plugins.form_elements.fields \
#          .date_drop_down.fobi_form_elements import DateDropDownInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .datetime.fobi_form_elements import DateTimeInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .decimal.fobi_form_elements import DecimalInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .email.fobi_form_elements import EmailInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .file.fobi_form_elements import FileInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .float.fobi_form_elements import FloatInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .hidden.fobi_form_elements import HiddenInputPlugin
# from fobi.contrib.plugins.form_elements.fields.hidden_model_object \
#          .fobi_form_elements import HiddenModelObjectInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .integer.fobi_form_elements import IntegerInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .ip_address.fobi_form_elements import IPAddressInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .null_boolean.fobi_form_elements import NullBooleanSelectPlugin
from fobi.contrib.plugins.form_elements.fields \
         .select.fobi_form_elements import SelectInputPlugin
from fobi.contrib.plugins.form_elements.fields.select_model_object \
         .fobi_form_elements import SelectModelObjectInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .select_multiple.fobi_form_elements import SelectMultipleInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .select_multiple_with_max.fobi_form_elements \
    import SelectMultipleWithMaxInputPlugin
from fobi.contrib.plugins.form_elements.fields.slug \
         .fobi_form_elements import SlugInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .text.fobi_form_elements import TextInputPlugin
from fobi.contrib.plugins.form_elements.fields \
         .textarea.fobi_form_elements import TextareaPlugin
from fobi.contrib.plugins.form_elements.fields \
         .url.fobi_form_elements import URLInputPlugin

from fobi.contrib.plugins.form_handlers \
         .db_store.fobi_form_handlers import DBStoreHandlerPlugin
from fobi.contrib.plugins.form_handlers \
         .mail.fobi_form_handlers import MailHandlerPlugin
from fobi.contrib.plugins.form_handlers \
         .http_repost.fobi_form_handlers import HTTPRepostHandlerPlugin

__title__ = 'fobi.tests.data'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TEST_DYNAMIC_FORMS_DEFINITION_DATA',
    'TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF',
    # 'TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF_NEGATIVE',
    'TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE',
    'TEST_DYNAMIC_FORMS_PUT_DATA',
    'TEST_DYNAMIC_FORMS_PUT_DATA_ALL',
    'TEST_FORM_ELEMENT_PLUGIN_DATA',
    'TEST_FORM_FIELD_DATA',
    'TEST_FORM_HANDLER_PLUGIN_DATA',
    'TEST_MAILCHIMP_IMPORTER_FORM_DATA',
)

TEST_FORM_ELEMENT_PLUGIN_DATA = {
    # Add a "Boolean (checkbox)" plugin.
    force_text(BooleanSelectPlugin.name): {
        'label': "Test boolean",
        'help_text': "Lorem ipsum boolean",
        'required': False,
    },

    # Add a "Select multiple" (select multiple input) form elelement
    # force_text(CheckboxSelectMultipleInputPlugin.name): {
    #     'label': "Test checkbox select multiple input",
    #     'help_text': "Lorem ipsum select multiple input",
    #     'required': False,
    # },

    # Add a "Date" input form element
    force_text(DateInputPlugin.name): {
        'label': "Test date input",
        'help_text': "Lorem ipsum select multiple input",
        'required': False,
    },

    # Add a "DateTime" input form element
    force_text(DateTimeInputPlugin.name): {
        'label': "Test datetime input",
        'help_text': "Lorem ipsum select multiple input",
        'required': False,
    },

    # Add an decimal input plugin
    force_text(DecimalInputPlugin.name): {
        'label': "Test decimal input",
        'help_text': "Lorem ipsum email",
        'required': True,
    },

    # Add an email input plugin
    force_text(EmailInputPlugin.name): {
        'label': "Test email input",
        'help_text': "Lorem ipsum email",
        'required': True,
    },

    # Add a "File" (file) form element
    force_text(FileInputPlugin.name): {
        'label': "Test file input",
        # 'name': "test_file_input",
        'help_text': "Lorem ipsum file",
        'required': False,
        },

    # Add an float input plugin
    force_text(FloatInputPlugin.name): {
        'label': "Test float input",
        'help_text': "Lorem ipsum email",
        'required': True,
    },

    # TODO: Find out why selenium fails here!
    # Add a "Hidden" (boolean) form element
    # force_text(HiddenInputPlugin.name): {
    #     'label': "Test hidden input",
    #     #'name': "test_hidden_input",
    #     'help_text': "Lorem ipsum hidden",
    #     'required': True,
    #     },

    # Add a "Integer" (text input) form element
    force_text(IntegerInputPlugin.name): {
        'label': "Test integer",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },

    # Add a "IP address" (text input) form element
    force_text(IPAddressInputPlugin.name): {
        'label': "Test IP address",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },

    # Add a "null boolean" form element
    force_text(NullBooleanSelectPlugin.name): {
        'label': "Test null boolean",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },

    # Add a "Select Input" (select input) form element
    force_text(SelectInputPlugin.name): {
        'label': "Test select",
        'help_text': "Lorem ipsum text input",
        'required': False,
        'choices': "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },

    # Add a "Select model object" (select input) form element
    force_text(SelectModelObjectInputPlugin.name): {
        'label': "Test select model object",
        'help_text': "Lorem ipsum select model object input",
        'required': False,
    },

    # Add a "Select multiple" (select multiple input) form element
    force_text(SelectMultipleInputPlugin.name): {
        'label': "Test select multiple input",
        'help_text': "Lorem ipsum select multiple input",
        'required': False,
        'choices': "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },

    # Add a "Select multiple with max" (select multiple with max input) form
    # element
    force_text(SelectMultipleWithMaxInputPlugin.name): {
        'label': "Test select multiple with max input",
        'help_text': "Lorem ipsum select multiple with max input",
        'required': False,
        'choices': "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },

    # Add a "Checkbox select multiple" (checkbox select multiple input) form
    # element
    force_text(CheckboxSelectMultipleInputPlugin.name): {
        'label': "Test checkbox select multiple input",
        'help_text': "Lorem ipsum checkbox select multiple input",
        'required': False,
        'choices': "1{s}2{s}alpha, Alpha{s}beta".format(s=os.linesep),
    },

    # Add a "Slug" (slug input) form element
    force_text(SlugInputPlugin.name): {
        'label': "Test slug input",
        'help_text': "Lorem ipsum select multiple input",
        'required': False,
    },

    # Add a "Text" (text input) form element
    force_text(TextInputPlugin.name): {
        'label': "Test text",
        'help_text': "Lorem ipsum text input",
        'required': True,
    },

    # Add a "Textarea" (text area) form element
    force_text(TextareaPlugin.name): {
        'label': "Test text area",
        'help_text': "Lorem ipsum text area",
        'required': True,
    },

    # Add a "URL input" form element
    force_text(URLInputPlugin.name): {
        'label': "Test URL input",
        'help_text': "Lorem ipsum text area",
        'required': True,
    },

    # Add a "Text" (text input) form element
    # force_text(TextInputPlugin.name): {
    #     'label': u"Անուն",
    #     'help_text': u"Անուն",
    #     'required': True,
    # },
}

TEST_FORM_FIELD_DATA = {
    'test_boolean': True,
    # 'test_checkbox_select_multiple_input': '',
    'test_date_input': datetime.date.today().strftime("%Y-%m-%d"),
    'test_datetime_input': datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    'test_decimal_input': '10.01',  # Decimal(10.01),
    'test_email_input': 'john@doe.net',
    'test_file_input': os.path.join(
        settings.MEDIA_ROOT,
        'testing',
        'delusional_insanity_-_karima_van_der_voort.jpg'
    ),
    'test_float_input': '10.01',
    # 'test_hidden_input': '',
    'test_integer': '2014',
    'test_null_boolean': False,
    'test_ip_address': '127.0.0.1',
    'test_select': '',
    'test_select_model_object': '',
    'test_select_multiple_input': '',
    'test_slug_input': 'lorem-ipsum',
    'test_text': 'Lorem ipsum',
    'test_text_area': 'Dolor sit amet',
    'test_url_input': 'http://dev.example.com',
    # 'test_unicode_text': u'Անուն',
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


TEST_MAILCHIMP_IMPORTER_FORM_DATA = [
    {
        u'default': u'',
        u'field_type': u'email',
        u'helptext': u'',
        u'id': 0,
        u'name': u'Email Address',
        u'order': u'1',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'EMAIL'
    },
    {
        u'default': u'',
        u'field_type': u'text',
        u'helptext': u'',
        u'id': 1,
        u'name': u'First Name',
        u'order': u'2',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'FNAME'
    },
    {
        u'default': u'',
        u'field_type': u'text',
        u'helptext': u'',
        u'id': 2,
        u'name': u'Last Name',
        u'order': u'3',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'LNAME'
    },
    {
        u'default': u'',
        u'field_type': u'text',
        u'helptext': u'',
        u'id': 3,
        u'name': u'Organisation',
        u'order': u'4',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'ORG'
    },
    {
        u'default': u'Type Text Default Value',
        u'field_type': u'text',
        u'helptext': u'Type Text Help Text',
        u'id': 4,
        u'name': u'type_text',
        u'order': u'5',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_TEXT'
    },
    {
        u'default': u'1',
        u'field_type': u'number',
        u'helptext': u'Type Number Help Text',
        u'id': 5,
        u'name': u'type_number',
        u'order': u'6',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_NUMBE'
    },
    {
        u'choices': [u'First Choice', u'Second Choice', u'Third Choice'],
        u'default': u'Second Choice',
        u'field_type': u'radio',
        u'helptext': u'Type Radio Buttons Help Text',
        u'id': 6,
        u'name': u'type_radio_buttons',
        u'order': u'7',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_RADIO'
    },
    {
        u'choices': [u'First Choice', u'Second Choice', u'Third Choice'],
        u'default': u'Third Choice',
        u'field_type': u'dropdown',
        u'helptext': u'Drop Down Help Text',
        u'id': 7,
        u'name': u'type_drop_down',
        u'order': u'9',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_DROPD'
    },
    {
        u'dateformat': u'MM/DD/YYYY',
        u'default': u'',
        u'field_type': u'date',
        u'helptext': u'Type Date Help Text',
        u'id': 8,
        u'name': u'type_date',
        u'order': u'10',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_DATE'
    },
    {
        u'dateformat': u'MM/DD',
        u'default': u'',
        u'field_type': u'birthday',
        u'helptext': u'Type Birthday Help Text',
        u'id': 9,
        u'name': u'type_birthday',
        u'order': u'11',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_BIRTH'
    },
    {
        u'default': u'',
        u'defaultcountry': u'109',
        u'defaultcountry_cc': u'NL',
        u'defaultcountry_name': u'Netherlands',
        u'field_type': u'address',
        u'helptext': u'Type Address Help Text',
        u'id': 10,
        u'name': u'type_address',
        u'order': u'12',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_ADDRE'
    },
    {
        u'default': u'',
        u'field_type': u'zip',
        u'helptext': u'Type Zip Code Help Text',
        u'id': 11,
        u'name': u'type_zip_code',
        u'order': u'13',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_ZIP_C'
    },
    {
        u'default': u'',
        u'field_type': u'phone',
        u'helptext': u'Type Phone Help Text',
        u'id': 12,
        u'name': u'type_phone',
        u'order': u'14',
        u'phoneformat': u'none',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_PHONE'
    },
    {
        u'default': u'',
        u'field_type': u'url',
        u'helptext': u'Type Website Help Text',
        u'id': 13,
        u'name': u'type_website',
        u'order': u'15',
        u'public': True,
        u'req': True,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_WEBSI'
    },
    {
        u'default': u'',
        u'field_type': u'imageurl',
        u'helptext': u'Type Image Help Text',
        u'id': 14,
        u'name': u'type_image',
        u'order': u'16',
        u'public': True,
        u'req': False,
        u'show': True,
        u'size': u'25',
        u'tag': u'TYPE_IMAGE'
    }
]

TEST_DYNAMIC_FORMS_DEFINITION_DATA = OrderedDict([
    (
        'username',
        (
            TextInputPlugin.uid,
            '{'
            '"name": "username", '
            '"required": true, '
            '"max_length": 200, '
            '"label": "Username", '
            '"placeholder": "delusionalinsanity"'
            '}'
        )
    ),
    (
        'email',
        (
            EmailInputPlugin.uid,
            '{'
            '"name": "email", '
            '"required": true, '
            '"label": "E-mail"'
            '}'
        )
    ),
    (
        'age',
        (
            IntegerInputPlugin.uid,
            '{'
            '"name": "age", '
            '"required": true, '
            '"max_value": 200, '
            '"label": "Age"'
            '}'
        )
    ),
    (
        'drivers_license',
        (
            BooleanSelectPlugin.uid,
            '{'
            '"name": "drivers_license", '
            '"required": false, '
            '"label": "Drivers license?"'
            '}'
        )
    ),
    (
        'special_fields',
        (
            HiddenInputPlugin.uid,
            '{'
            '"name": "special_fields", '
            '"required": false, '
            '"label": "Special fields"'
            '}'
        )
    ),
    (
        'ignore_01',
        (
            ContentImagePlugin.uid, '{'
            '"fit_method": "center", '
            '"file": "fobi_plugins/content_plugin_images/'
            '04.jpg", '
            '"alt": "Cute girl"'
            '}'
        )
    ),
    (
        'number_of_children',
        (
            IntegerInputPlugin.uid,
            '{'
            '"name": "number_of_children", '
            '"required": false, '
            '"label": "Number of children"'
            '}'
        )
    ),
    (
        'bio',
        (
            TextareaPlugin.uid,
            '{'
            '"name": "bio", '
            '"required": true, '
            # '"max_length": null',
            '"label": "Biography"'
            '}'
        )
    ),
    (
        'ignore_02',
        (
            ContentTextPlugin.uid,
            '{'
            '"text": "Suspendisse potenti. Etiam in nunc '
            'sodales, congue lectus ut, suscipit massa. In '
            'commodo fringilla orci, in varius eros gravida '
            'a! Aliquam erat volutpat. Donec sodales orci nec '
            'massa aliquam bibendum. Aenean sed condimentum '
            'velit. Mauris luctus bibendum nulla vel tempus. '
            'Integer tempor condimentum ligula sed feugiat. '
            'Aenean scelerisque ultricies vulputate. Donec '
            'semper lorem rhoncus sem cras amet."'
            '}'
        )
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
])

TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF = copy.copy(
    TEST_DYNAMIC_FORMS_DEFINITION_DATA
)
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop('ignore_01')
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop('ignore_02')
TEST_DYNAMIC_FORMS_DEFINITION_DATA_DRF.pop('special_fields')

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
    'username': FAKER.user_name(),
    'email': FAKER.email(),
    'age': FAKER.random_int(min=0, max=200),
    'drivers_license': FAKER.pybool(),
    'special_fields': FAKER.pystr(),
    'number_of_children': FAKER.pyint(),
    'bio': FAKER.text(),
    # 'unicode_name': u'Անուն',
}

TEST_DYNAMIC_FORMS_PUT_DATA = copy.copy(TEST_DYNAMIC_FORMS_PUT_DATA_ALL)
TEST_DYNAMIC_FORMS_PUT_DATA.pop('special_fields')

TEST_DYNAMIC_FORMS_OPTIONS_RESPONSE = OrderedDict([
    (u'username', OrderedDict([(u'type', u'string'),
                               (u'required', True),
                               (u'read_only', False),
                               (u'label', u'Username'),
                               (u'max_length', 200),
                               (u'placeholder', 'delusionalinsanity')])),
    (u'email', OrderedDict([(u'type', u'email'),
                            (u'required', True),
                            (u'read_only', False),
                            (u'label', u'E-mail'),
                            (u'max_length', 255)])),
    (u'age', OrderedDict([(u'type', u'integer'),
                          (u'required', True),
                          (u'read_only', False),
                          (u'label', u'Age'),
                          ('max_value', 200)])),
    (u'drivers_license', OrderedDict([(u'type', u'boolean'),
                                      (u'required', False),
                                      (u'read_only', False),
                                      (u'label', u'Drivers license?')])),
    # (u'special_fields', OrderedDict([(u'type', u'field'),
    #                                  (u'required', False),
    #                                  (u'read_only', False),
    #                                  (u'label', u'Special fields')])),
    (u'number_of_children', OrderedDict([(u'type', u'integer'),
                                         (u'required', False),
                                         (u'read_only', False),
                                         (u'label', u'Number of children')])),
    (u'bio', OrderedDict([(u'type', u'string'),
                          (u'required', True),
                          # (u'max_length', None),
                          (u'read_only', False),
                          (u'label', u'Biography')])),
    # (u'unicode_name', OrderedDict([(u'type', u'string'),
    #                                (u'required', True),
    #                                (u'read_only', False),
    #                                (u'label', u'Անուն'),
    #                                (u'max_length', 200),
    #                                (u'placeholder', u'Անուն')])),
])
