# Generated by Django 4.0.6 on 2022-07-28 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary', '0002_rename_music_songs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]
