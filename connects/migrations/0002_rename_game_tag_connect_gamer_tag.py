# Generated by Django 4.2.7 on 2023-11-21 06:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("connects", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="connect",
            old_name="game_tag",
            new_name="gamer_tag",
        ),
    ]
