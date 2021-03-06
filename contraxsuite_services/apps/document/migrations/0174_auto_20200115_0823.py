# Generated by Django 2.2.4 on 2020-01-15 08:23

import apps.document.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0173_auto_20191223_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldAnnotationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('code', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('is_confirm', models.BooleanField(db_index=True, default=False)),
                ('is_deny', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'verbose_name_plural': 'Field Annotation Statuses',
                'ordering': ['order', 'name', 'code'],
            },
        ),
        migrations.AddField(
            model_name='fieldannotation',
            name='assign_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fieldannotation',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field_annotations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalfieldannotation',
            name='assign_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalfieldannotation',
            name='assignee',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fieldannotation',
            name='status',
            field=models.ForeignKey(blank=True, default=apps.document.models.FieldAnnotationStatus.initial_status, null=True, on_delete=django.db.models.deletion.SET_NULL, to='document.FieldAnnotationStatus'),
        ),
        migrations.AddField(
            model_name='historicalfieldannotation',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='document.FieldAnnotationStatus'),
        ),
    ]
