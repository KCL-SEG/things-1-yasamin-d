# Generated by Django 4.1.3 on 2022-12-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things',
            new_name='Thing',
        ),
    ]
