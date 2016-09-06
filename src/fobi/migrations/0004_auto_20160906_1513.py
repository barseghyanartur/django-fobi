# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0003_auto_20160517_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formelement',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'boolean', b'Boolean'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_image', b'Content image'), (b'content_text', b'Content text'), (b'content_video', b'Content video'), (b'date', b'Date'), (b'date_drop_down', b'Date drop down'), (b'datetime', b'DateTime'), (b'decimal', b'Decimal'), (b'dummy', b'Dummy'), (b'email', b'Email'), (b'file', b'File'), (b'float', b'Float'), (b'hidden', b'Hidden'), (b'honeypot', b'Honeypot'), (b'input', b'Input'), (b'integer', b'Integer'), (b'ip_address', b'IP address'), (b'null_boolean', b'Null boolean'), (b'password', b'Password'), (b'radio', b'Radio'), (b'regex', b'Regex'), (b'select', b'Select'), (b'select_model_object', b'Select model object'), (b'select_multiple', b'Select multiple'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple_with_max', b'Select multiple with max'), (b'slug', b'Slug'), (b'text', b'Text'), (b'textarea', b'Textarea'), (b'time', b'Time'), (b'url', b'URL')]),
        ),
        migrations.AlterField(
            model_name='formelemententry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'boolean', b'Boolean'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_image', b'Content image'), (b'content_text', b'Content text'), (b'content_video', b'Content video'), (b'date', b'Date'), (b'date_drop_down', b'Date drop down'), (b'datetime', b'DateTime'), (b'decimal', b'Decimal'), (b'dummy', b'Dummy'), (b'email', b'Email'), (b'file', b'File'), (b'float', b'Float'), (b'hidden', b'Hidden'), (b'honeypot', b'Honeypot'), (b'input', b'Input'), (b'integer', b'Integer'), (b'ip_address', b'IP address'), (b'null_boolean', b'Null boolean'), (b'password', b'Password'), (b'radio', b'Radio'), (b'regex', b'Regex'), (b'select', b'Select'), (b'select_model_object', b'Select model object'), (b'select_multiple', b'Select multiple'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple_with_max', b'Select multiple with max'), (b'slug', b'Slug'), (b'text', b'Text'), (b'textarea', b'Textarea'), (b'time', b'Time'), (b'url', b'URL')]),
        ),
        migrations.AlterField(
            model_name='formhandler',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'db_store', b'DB store'), (b'http_repost', b'HTTP Repost'), (b'mail', b'Mail')]),
        ),
        migrations.AlterField(
            model_name='formhandlerentry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'db_store', b'DB store'), (b'http_repost', b'HTTP Repost'), (b'mail', b'Mail')]),
        ),
    ]
