import os
import random

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save

from teams.models import Team
from unifiedpro_am_proj.utils import unique_event_id_generator, unique_league_id_generator

User = get_user_model()



def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "league/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


def upload_event_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "events/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


LEAGUE_TYPE_CHOICE = (

    ('Premier Leagues', 'Premier Leagues'),
    ('Amateur Leagues', 'Amateur Leagues'),
)
class League(models.Model):
    league_id = models.CharField(max_length=255, null=False, blank=True, unique=True)
    league_name = models.CharField(max_length=255, null=True, blank=True)
    league_type = models.CharField(choices=LEAGUE_TYPE_CHOICE, max_length=255, null=True, blank=True)
    league_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    league_cover = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    league_about = models.TextField(null=True, blank=True)

    seasons = models.IntegerField(default=0, null=True, blank=True)
    tournaments = models.IntegerField(default=0, null=True, blank=True)
    draft_leagues = models.IntegerField(default=0, null=True, blank=True)

    league_manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='league_manager')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def pre_save_league_id_receiver(sender, instance, *args, **kwargs):
    if not instance.league_id:
        instance.league_id = unique_league_id_generator(instance)

pre_save.connect(pre_save_league_id_receiver, sender=League)




EVENT_TYPE_CHOICE = (

    ('Season', 'Season'),
    ('Tournament', 'Tournament'),
)

STATUS_CHOICE = (

    ('Created', 'Created'),
    ('Pending', 'Pending'),
    ('Rescheduled', 'Rescheduled'),
    ('Started', 'Started'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
    ('Canceled', 'Canceled'),
)

class Event(models.Model):
    event_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True,  blank=True, related_name='league_events')

    event_title = models.CharField(max_length=255, blank=True, null=True)
    event_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, default="Pending", null=True, blank=True, choices=STATUS_CHOICE)
    event_type = models.CharField(max_length=255, null=True, blank=True, choices=EVENT_TYPE_CHOICE)
    price = models.CharField(max_length=255, default="0000", null=True, blank=True)
    sign_up_fee = models.CharField(max_length=255, default="0000", null=True, blank=True)
    event_cover = models.ImageField(upload_to=upload_event_image_path, null=True, blank=True)

    event_consoles = models.CharField(max_length=1000, blank=True, null=True)

    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)

    event_rescheduled_at = models.DateTimeField(null=True, blank=True)
    event_cancelled_at = models.DateTimeField(null=True, blank=True)

    event_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  blank=True,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def pre_save_event_id_receiver(sender, instance, *args, **kwargs):
    if not instance.event_id:
        instance.event_id = unique_event_id_generator(instance)

pre_save.connect(pre_save_event_id_receiver, sender=Event)


class EventSignUp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_signups')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,  blank=True, related_name='event_teams')
    players = models.ManyToManyField(User,  blank=True, related_name='event_team_players')
