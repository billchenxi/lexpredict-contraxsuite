# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0011_auto_20180213_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.DocumentType'),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='document.DocumentType'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='search_fields',
            field=models.ManyToManyField(blank=True, related_name='search_field_document_type', to='document.DocumentField'),
        ),
    ]
