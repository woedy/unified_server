from django.db import models

from events.models import Event
from teams.models import Team


class Game(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_games')
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_team_1')
    team_1_avg_score = models.IntegerField(default=0, null=True, blank=True)
    team_1_1st_quart = models.IntegerField(default=0, null=True, blank=True)
    team_1_2nd_quart = models.IntegerField(default=0, null=True, blank=True)
    team_1_3rd_quart = models.IntegerField(default=0, null=True, blank=True)
    team_1_4th_quart = models.IntegerField(default=0, null=True, blank=True)
    team_1_overtime = models.IntegerField(default=0, null=True, blank=True)

    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_team_2')
    team_2_avg_score = models.IntegerField(default=0, null=True, blank=True)
    team_2_1st_quart = models.IntegerField(default=0, null=True, blank=True)
    team_2_2nd_quart = models.IntegerField(default=0, null=True, blank=True)
    team_2_3rd_quart = models.IntegerField(default=0, null=True, blank=True)
    team_2_4th_quart = models.IntegerField(default=0, null=True, blank=True)
    team_2_overtime = models.IntegerField(default=0, null=True, blank=True)