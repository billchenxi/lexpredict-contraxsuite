# Generated by Django 2.2.4 on 2019-12-06 06:39

from django.db import migrations, connection


def do_migrate(apps, schema_editor):

    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO document_textunittext (text_unit_id, text) SELECT id as text_unit_id, text FROM document_textunit')


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0170_textunittext'),
    ]

    operations = [
        migrations.RunPython(do_migrate, reverse_code=migrations.RunPython.noop),
    ]