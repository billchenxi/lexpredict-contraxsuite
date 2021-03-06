# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-06 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0110_remove_temporary_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTypeCachingConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caching_enabled', models.BooleanField(default=True)),
                ('document_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.DocumentType')),
            ],
        ),
    ]
