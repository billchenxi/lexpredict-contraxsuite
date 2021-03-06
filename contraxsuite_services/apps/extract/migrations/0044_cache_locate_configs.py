# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-01 14:33
from __future__ import unicode_literals

from django.db import migrations

from apps.extract import dict_data_cache


def cache_geo_config(apps, schema_editor):
    dict_data_cache.cache_geo_config()


class Migration(migrations.Migration):
    dependencies = [
        ('extract', '0043_auto_20190227_1952'),
    ]

    operations = [
        migrations.RunPython(cache_geo_config),
    ]
