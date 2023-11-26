# Generated by Django 4.2.7 on 2023-11-26 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="event_cancelled_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="event_end",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="event_rescheduled_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="event_start",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.CharField(
                blank=True, default="0000", max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Created", "Created"),
                    ("Pending", "Pending"),
                    ("Rescheduled", "Rescheduled"),
                    ("Started", "Started"),
                    ("Ongoing", "Ongoing"),
                    ("Completed", "Completed"),
                    ("Canceled", "Canceled"),
                ],
                default="Pending",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
