# Generated by Django 4.1.3 on 2022-11-09 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_social_care'),
    ]

    operations = [
        migrations.RenameField(
            model_name='care',
            old_name='type',
            new_name='name',
        ),
    ]
