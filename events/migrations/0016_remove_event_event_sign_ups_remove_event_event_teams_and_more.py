# Generated by Django 4.2.7 on 2023-12-01 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_remove_team_team_events'),
        ('events', '0015_event_event_consoles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_sign_ups',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_teams',
        ),
        migrations.CreateModel(
            name='EventSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_signups', to='events.event')),
                ('players', models.ManyToManyField(blank=True, related_name='event_team_players', to='teams.team')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_teams', to='teams.team')),
            ],
        ),
    ]
