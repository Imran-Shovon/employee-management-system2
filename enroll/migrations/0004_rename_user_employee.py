# Generated by Django 4.0.2 on 2023-05-29 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_rename_name_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Employee',
        ),
    ]
