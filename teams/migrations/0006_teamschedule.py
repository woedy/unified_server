# Generated by Django 4.2.7 on 2023-11-26 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0005_teamgallery"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamSchedule",
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
                ("date_time", models.DateTimeField(blank=True, null=True)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_schedules",
                        to="teams.team",
                    ),
                ),
            ],
        ),
    ]
