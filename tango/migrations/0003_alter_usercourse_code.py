# Generated by Django 5.0.1 on 2024-01-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0002_usercourse_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
