# Generated by Django 4.2 on 2023-06-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0011_alter_report_description_alter_report_fault_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='shift',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1, null=True),
        ),
    ]