# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0003_auto_20160517_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formelement',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'select_model_object', b'Select model object'), (b'text', b'Text'), (b'float', b'Float'), (b'datetime', b'DateTime'), (b'boolean', b'Boolean'), (b'radio', b'Radio'), (b'file', b'File'), (b'select', b'Select'), (b'content_image', b'Content image'), (b'null_boolean', b'Null boolean'), (b'input', b'Input'), (b'hidden', b'Hidden'), (b'email', b'Email'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_text', b'Content text'), (b'date', b'Date'), (b'integer', b'Integer'), (b'password', b'Password'), (b'ip_address', b'IP address'), (b'slug', b'Slug'), (b'dummy', b'Dummy'), (b'textarea', b'Textarea'), (b'url', b'URL'), (b'decimal', b'Decimal'), (b'content_video', b'Content video'), (b'time', b'Time'), (b'date_drop_down', b'Date drop down')]),
        ),
        migrations.AlterField(
            model_name='formelemententry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'select_model_object', b'Select model object'), (b'text', b'Text'), (b'float', b'Float'), (b'datetime', b'DateTime'), (b'boolean', b'Boolean'), (b'radio', b'Radio'), (b'file', b'File'), (b'select', b'Select'), (b'content_image', b'Content image'), (b'null_boolean', b'Null boolean'), (b'input', b'Input'), (b'hidden', b'Hidden'), (b'email', b'Email'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_text', b'Content text'), (b'date', b'Date'), (b'integer', b'Integer'), (b'password', b'Password'), (b'ip_address', b'IP address'), (b'slug', b'Slug'), (b'dummy', b'Dummy'), (b'textarea', b'Textarea'), (b'url', b'URL'), (b'decimal', b'Decimal'), (b'content_video', b'Content video'), (b'time', b'Time'), (b'date_drop_down', b'Date drop down')]),
        ),
        migrations.AlterField(
            model_name='formhandler',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'db_store', b'DB store'), (b'mail', b'Mail'), (b'http_repost', b'HTTP Repost')]),
        ),
        migrations.AlterField(
            model_name='formhandlerentry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'db_store', b'DB store'), (b'mail', b'Mail'), (b'http_repost', b'HTTP Repost')]),
        ),
    ]
