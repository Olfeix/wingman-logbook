# Generated by Django 4.1.7 on 2023-03-02 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('users', '0002_rename_user_registeredusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisteredUsers',
            new_name='User',
        ),
    ]