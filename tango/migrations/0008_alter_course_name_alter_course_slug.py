# Generated by Django 5.0.1 on 2024-02-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0007_alter_course_discount_alter_course_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
