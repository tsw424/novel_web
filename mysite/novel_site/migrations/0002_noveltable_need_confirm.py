# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noveltable',
            name='need_confirm',
            field=models.BooleanField(default=0),
        ),
    ]
