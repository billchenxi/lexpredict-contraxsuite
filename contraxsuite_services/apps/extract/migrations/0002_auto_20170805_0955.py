# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='name',
            field=models.CharField(db_index=True, max_length=1024),
        ),
    ]
