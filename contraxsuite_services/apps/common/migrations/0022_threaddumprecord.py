# Generated by Django 2.2.4 on 2019-11-01 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20191017_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadDumpRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, db_index=True)),
                ('node', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('command_line', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('cpu_usage', models.FloatField(blank=True, null=True)),
                ('memory_usage', models.IntegerField(blank=True, null=True)),
                ('dump', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
