# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:48
from __future__ import unicode_literals

import ckeditor.fields
import django.contrib.postgres.fields.jsonb
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=1024, null=True)),
                ('document_type', models.CharField(db_index=True, max_length=128)),
                ('description', models.TextField(null=True)),
                ('source', models.CharField(db_index=True, max_length=1024, null=True)),
                ('source_type', models.CharField(db_index=True, max_length=100, null=True)),
                ('source_path', models.CharField(db_index=True, max_length=1024, null=True)),
                ('paragraphs', models.PositiveIntegerField(default=0)),
                ('sentences', models.PositiveIntegerField(default=0)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DocumentNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('note', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ('document__name', 'timestamp'),
            },
        ),
        migrations.CreateModel(
            name='DocumentProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=1024)),
                ('value', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ('document__name', 'key', 'value'),
                'verbose_name_plural': 'Document Properties',
            },
        ),
        migrations.CreateModel(
            name='DocumentRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=1024)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('document', 'tag', 'timestamp'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalDocumentNote',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('note', ckeditor.fields.RichTextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical document note',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTextUnitNote',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('note', ckeditor.fields.RichTextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical text unit note',
            },
        ),
        migrations.CreateModel(
            name='TextUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_type', models.CharField(db_index=True, max_length=128)),
                ('language', models.CharField(db_index=True, max_length=3)),
                ('text', models.TextField(max_length=16384)),
                ('text_hash', models.CharField(db_index=True, max_length=1024, null=True)),
            ],
            options={
                'ordering': ('document__name', 'unit_type'),
            },
        ),
        migrations.CreateModel(
            name='TextUnitNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('note', ckeditor.fields.RichTextField()),
            ],
            options={
                'ordering': ('text_unit', 'timestamp'),
            },
        ),
        migrations.CreateModel(
            name='TextUnitProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=1024)),
                ('value', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ('text_unit__document__name', 'key', 'value'),
                'verbose_name_plural': 'Text Unit Properties',
            },
        ),
        migrations.CreateModel(
            name='TextUnitRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TextUnitTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=1024)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('text_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.TextUnit')),
            ],
            options={
                'ordering': ('text_unit', 'tag', 'timestamp'),
            },
        ),
    ]
