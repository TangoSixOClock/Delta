# Generated by Django 5.0.1 on 2024-02-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0030_alter_userprofile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='requirement_to_complete',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
