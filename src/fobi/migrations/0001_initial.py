# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings
from nine.versions import DJANGO_GTE_1_8


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    if DJANGO_GTE_1_8:
        dependencies += [('auth', '0006_require_contenttypes_0002'),]

    operations = [
        migrations.CreateModel(
            name='FormElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_uid', models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'select_model_object', b'Select model object'), (b'text', b'Text'), (b'float', b'Float'), (b'datetime', b'DateTime'), (b'boolean', b'Boolean'), (b'radio', b'Radio'), (b'file', b'File'), (b'select', b'Select'), (b'regex', b'Regex'), (b'content_image', b'Content image'), (b'null_boolean', b'Null boolean'), (b'input', b'Input'), (b'hidden', b'Hidden'), (b'email', b'Email'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_text', b'Content text'), (b'date', b'Date'), (b'integer', b'Integer'), (b'password', b'Password'), (b'ip_address', b'IP address'), (b'slug', b'Slug'), (b'dummy', b'Dummy'), (b'textarea', b'Textarea'), (b'url', b'URL'), (b'decimal', b'Decimal'), (b'content_video', b'Content video'), (b'time', b'Time'), (b'date_drop_down', b'Date drop down'), (b'honeypot', b'Honeypot')])),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='Group', blank=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='User', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Form element plugin',
                'verbose_name_plural': 'Form element plugins',
            },
        ),
        migrations.CreateModel(
            name='FormElementEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_data', models.TextField(null=True, verbose_name='Plugin data', blank=True)),
                ('plugin_uid', models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'select_model_object', b'Select model object'), (b'text', b'Text'), (b'float', b'Float'), (b'datetime', b'DateTime'), (b'boolean', b'Boolean'), (b'radio', b'Radio'), (b'file', b'File'), (b'select', b'Select'), (b'regex', b'Regex'), (b'content_image', b'Content image'), (b'null_boolean', b'Null boolean'), (b'input', b'Input'), (b'hidden', b'Hidden'), (b'email', b'Email'), (b'select_multiple_model_objects', b'Select multiple model objects'), (b'select_multiple', b'Select multiple'), (b'checkbox_select_multiple', b'Checkbox select multiple'), (b'content_text', b'Content text'), (b'date', b'Date'), (b'integer', b'Integer'), (b'password', b'Password'), (b'ip_address', b'IP address'), (b'slug', b'Slug'), (b'dummy', b'Dummy'), (b'textarea', b'Textarea'), (b'url', b'URL'), (b'decimal', b'Decimal'), (b'content_video', b'Content video'), (b'time', b'Time'), (b'date_drop_down', b'Date drop down'), (b'honeypot', b'Honeypot')])),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Position', blank=True)),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
                'verbose_name': 'Form element entry',
                'verbose_name_plural': 'Form element entries',
            },
        ),
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(verbose_name='Slug', unique=True, editable=False)),
                ('is_public', models.BooleanField(default=False, help_text='Makes your form visible to the public.', verbose_name='Public?')),
                ('is_cloneable', models.BooleanField(default=False, help_text='Makes your form cloneable by other users.', verbose_name='Cloneable?')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Position', blank=True)),
                ('success_page_title', models.CharField(help_text='Custom message title to display after valid form is submitted', max_length=255, null=True, verbose_name='Success page title', blank=True)),
                ('success_page_message', models.TextField(help_text='Custom message text to display after valid form is submitted', null=True, verbose_name='Success page body', blank=True)),
                ('action', models.CharField(help_text="Custom form action; don't fill this field, unless really necessary.", max_length=255, null=True, verbose_name='Action', blank=True)),
            ],
            options={
                'verbose_name': 'Form entry',
                'verbose_name_plural': 'Form entries',
            },
        ),
        migrations.CreateModel(
            name='FormFieldsetEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('is_repeatable', models.BooleanField(default=False, help_text='Makes your form fieldset repeatable.', verbose_name='Is repeatable?')),
                ('form_entry', models.ForeignKey(verbose_name='Form', blank=True, to='fobi.FormEntry', null=True)),
            ],
            options={
                'verbose_name': 'Form fieldset entry',
                'verbose_name_plural': 'Form fieldset entries',
            },
        ),
        migrations.CreateModel(
            name='FormHandler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_uid', models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'db_store', b'DB store'), (b'mail', b'Mail'), (b'http_repost', b'HTTP Repost')])),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='Group', blank=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='User', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Form handler plugin',
                'verbose_name_plural': 'Form handler plugins',
            },
        ),
        migrations.CreateModel(
            name='FormHandlerEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_data', models.TextField(null=True, verbose_name='Plugin data', blank=True)),
                ('plugin_uid', models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'db_store', b'DB store'), (b'mail', b'Mail'), (b'http_repost', b'HTTP Repost')])),
                ('form_entry', models.ForeignKey(verbose_name='Form', to='fobi.FormEntry')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Form handler entry',
                'verbose_name_plural': 'Form handler entries',
            },
        ),
        migrations.CreateModel(
            name='FormWizardEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(verbose_name='Slug', unique=True, editable=False)),
                ('is_public', models.BooleanField(default=False, help_text='Makes your form wizard visible to the public.', verbose_name='Is public?')),
                ('is_cloneable', models.BooleanField(default=False, help_text='Makes your form wizard cloneable by other users.', verbose_name='Is cloneable?')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Form wizard entry',
                'verbose_name_plural': 'Form wizard entries',
            },
        ),
        migrations.AddField(
            model_name='formentry',
            name='form_wizard_entry',
            field=models.ForeignKey(verbose_name='Form wizard', blank=True, to='fobi.FormWizardEntry', null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='formelemententry',
            name='form_entry',
            field=models.ForeignKey(verbose_name='Form', to='fobi.FormEntry'),
        ),
        migrations.AddField(
            model_name='formelemententry',
            name='form_fieldset_entry',
            field=models.ForeignKey(verbose_name='Form fieldset', blank=True, to='fobi.FormFieldsetEntry', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='formwizardentry',
            unique_together=set([('user', 'slug'), ('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='formfieldsetentry',
            unique_together=set([('form_entry', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='formentry',
            unique_together=set([('user', 'slug'), ('user', 'name')]),
        ),
    ]
