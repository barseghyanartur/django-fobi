# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created', null=True),
        ),
        migrations.AddField(
            model_name='formentry',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated', null=True),
        ),
    ]
