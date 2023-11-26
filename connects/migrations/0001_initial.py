# Generated by Django 4.2.7 on 2023-11-21 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Connect",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "connect_name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PSN", "PSN"),
                            ("Xbox Live", "Xbox Live"),
                            ("Twitter", "Twitter"),
                            ("Discord", "Discord"),
                            ("Twitch", "Twitch"),
                        ],
                        max_length=255,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "game_tag",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_connects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]