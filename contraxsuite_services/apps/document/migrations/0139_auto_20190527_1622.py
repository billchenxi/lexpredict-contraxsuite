# Generated by Django 2.2 on 2019-05-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0138_auto_20190527_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentfield',
            name='python_coded_field',
            field=models.CharField(blank=True, choices=[('employment.employee_name', 'Employment: Employee Name'), ('employment.employer_name', 'Employment: Employer Name'), ('employment.salary', 'Employment: Salary'), ('generic.EarliestDate', 'Earliest Date'), ('generic.LatestDate', 'Latest Date'), ('generic.MaxCurrency', 'Max Currency'), ('generic.Parties', 'Parties'), ('similarity.SimilarDocuments', 'Similar Documents')], db_index=True, max_length=100, null=True),
        ),
    ]
