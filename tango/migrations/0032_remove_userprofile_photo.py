# Generated by Django 5.0.1 on 2024-02-13 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0031_course_language_course_requirement_to_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
    ]
