# Generated by Django 5.0.1 on 2024-02-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tango', '0022_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='profile.jpg', upload_to='files/profile/'),
        ),
    ]
