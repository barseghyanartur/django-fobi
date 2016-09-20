# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0002_auto_20150912_1744'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedFormDataEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID',
                                        serialize=False, primary_key=True)),
                ('form_data_headers', models.TextField(
                    verbose_name='Form data headers', blank=True, null=True)),
                ('saved_data', models.TextField(verbose_name='Plugin data',
                                                blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='Date created',
                                                 auto_now_add=True)),
                ('form_entry', models.ForeignKey(verbose_name='Form',
                                                 blank=True,
                                                 to='fobi.FormEntry',
                                                 null=True)),
                ('user', models.ForeignKey(verbose_name='User', blank=True,
                                           to=settings.AUTH_USER_MODEL,
                                           null=True)),
            ],
            options={
                'verbose_name': 'Saved form data entry',
                'abstract': False,
                'verbose_name_plural': 'Saved form data entries',
                'db_table': 'db_store_savedformdataentry',
            },
        ),
    ]
