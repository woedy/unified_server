# Generated by Django 4.2.7 on 2023-11-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0012_league_league_cover"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="draft_leagues",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="league",
            name="seasons",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="league",
            name="tournaments",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]