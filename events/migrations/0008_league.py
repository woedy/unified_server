# Generated by Django 4.2.7 on 2023-11-26 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0007_event_event_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="League",
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
                    "league_id",
                    models.CharField(blank=True, max_length=255, unique=True),
                ),
                (
                    "league_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "league_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Premier Leagues", "Premier Leagues"),
                            ("Amateur Leagues", "Amateur Leagues"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "league_logo",
                    models.ImageField(
                        blank=True, null=True, upload_to=events.models.upload_image_path
                    ),
                ),
                ("league_about", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "league_manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="league_manager",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]