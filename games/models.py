from django.db import models
from django.db.models.signals import pre_save

from events.models import Event
from teams.models import Team
from unifiedpro_am_proj.utils import unique_game_id_generator, unique_round_id_generator


#class Game(models.Model):
#    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_games')
#    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_team_1')
#    team_1_avg_score = models.IntegerField(default=0, null=True, blank=True)
#    team_1_1st_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_1_2nd_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_1_3rd_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_1_4th_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_1_overtime = models.IntegerField(default=0, null=True, blank=True)
#
#    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_team_2')
#    team_2_avg_score = models.IntegerField(default=0, null=True, blank=True)
#    team_2_1st_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_2_2nd_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_2_3rd_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_2_4th_quart = models.IntegerField(default=0, null=True, blank=True)
#    team_2_overtime = models.IntegerField(default=0, null=True, blank=True)



class Round(models.Model):
    round_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_rounds')
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.event} - {self.name}"


def pre_save_round_id_receiver(sender, instance, *args, **kwargs):
    if not instance.round_id:
        instance.round_id = unique_round_id_generator(instance)

pre_save.connect(pre_save_round_id_receiver, sender=Round)


class Game(models.Model):
    game_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_games')
    round = models.ForeignKey(Round, related_name='games', on_delete=models.CASCADE)
    home_team = models.ForeignKey( Team, default=1,related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, default=2,  related_name='away_games', on_delete=models.CASCADE)
    home_team_score = models.PositiveIntegerField(blank=True, null=True)
    away_team_score = models.PositiveIntegerField(blank=True, null=True)
    # Other fields: date, location, etc.

    def __str__(self):
        return f"Game: {self.home_team} vs {self.away_team}"




def pre_save_game_id_receiver(sender, instance, *args, **kwargs):
    if not instance.game_id:
        instance.game_id = unique_game_id_generator(instance)

pre_save.connect(pre_save_game_id_receiver, sender=Game)
