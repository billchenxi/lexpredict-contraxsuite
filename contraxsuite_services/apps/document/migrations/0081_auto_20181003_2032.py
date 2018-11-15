# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-03 20:32
from __future__ import unicode_literals

from django.db import migrations, models


def update_read_only(apps, schema_editor):
    DocumentField = apps.get_model('document', 'DocumentField')
    for f in DocumentField.objects.all():  # type: DocumentField
        if f.formula:
            f.read_only = True
            f.save()


class Migration(migrations.Migration):
    dependencies = [
        ('document', '0080_auto_20181002_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfield',
            name='read_only',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(update_read_only)
    ]