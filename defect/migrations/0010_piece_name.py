# Generated by Django 4.2 on 2023-06-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect', '0009_alter_report_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=False,
        ),
    ]