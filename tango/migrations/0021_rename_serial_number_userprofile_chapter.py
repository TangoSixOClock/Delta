# Generated by Django 5.0.1 on 2024-02-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0020_userprofile_serial_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='serial_number',
            new_name='chapter',
        ),
    ]
