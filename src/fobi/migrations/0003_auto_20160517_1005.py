# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0002_auto_20150912_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formelement',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'regex', b'Regex'), (b'boolean', b'Boolean'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'textarea', b'Textarea'), (b'select_model_object', b'Select model object'), (b'datetime', b'DateTime'), (b'text', b'Text'), (b'decimal', b'Decimal'), (b'float', b'Float'), (b'email', b'Email'), (b'date_drop_down', b'Date drop down'), (b'radio', b'Radio'), (b'null_boolean', b'Null boolean'), (b'time', b'Time'), (b'date', b'Date'), (b'integer', b'Integer'), (b'hidden', b'Hidden'), (b'password', b'Password'), (b'slug', b'Slug'), (b'select', b'Select')]),
        ),
        migrations.AlterField(
            model_name='formelemententry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'regex', b'Regex'), (b'boolean', b'Boolean'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'textarea', b'Textarea'), (b'select_model_object', b'Select model object'), (b'datetime', b'DateTime'), (b'text', b'Text'), (b'decimal', b'Decimal'), (b'float', b'Float'), (b'email', b'Email'), (b'date_drop_down', b'Date drop down'), (b'radio', b'Radio'), (b'null_boolean', b'Null boolean'), (b'time', b'Time'), (b'date', b'Date'), (b'integer', b'Integer'), (b'hidden', b'Hidden'), (b'password', b'Password'), (b'slug', b'Slug'), (b'select', b'Select')]),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='formhandler',
            name='plugin_uid',
            field=models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='formhandlerentry',
            name='plugin_uid',
            field=models.CharField(max_length=255, verbose_name='Plugin name'),
        ),
        migrations.AlterField(
            model_name='formwizardentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='Slug'),
        ),
    ]
