from django.contrib.auth import get_user_model
from django.db import models

from events.models import Event
from teams.models import Team

User = get_user_model()
class Standing(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_standings')
    position = models.IntegerField(default=0, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='team_standings')

    wins = models.IntegerField(default=0, null=True, blank=True)
    loss = models.IntegerField(default=0, null=True, blank=True)

    pct = models.IntegerField(default=0, null=True, blank=True)
    gb = models.IntegerField(default=0, null=True, blank=True)


class LeaderBoard(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_leaderboards')
    pos = models.IntegerField(default=0, blank=True, null=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='leaderboard_players')



class Award(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_awards')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='award_winner')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
