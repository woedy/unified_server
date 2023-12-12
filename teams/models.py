import os
import random

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save

from unifiedpro_am_proj.utils import unique_team_id_generator

# Create your models here.

User = get_user_model()


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "teams/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

def upload_gallery_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "teams/gallery/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Team(models.Model):
    team_id = models.CharField(max_length=255, null=False, blank=True, unique=True)
    team_name = models.CharField(max_length=255, null=True, blank=True)
    team_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    team_about = models.TextField(null=True, blank=True)

    selected_consoles = models.CharField(null=True, blank=True, max_length=255)

    points_per_game = models.DecimalField(default=0.00, null=True, blank=True, max_digits=5, decimal_places=3)
    assists_per_game = models.DecimalField(default=0.00, null=True, blank=True, max_digits=5,decimal_places=3)
    rebounds_per_game = models.DecimalField(default=0.00, null=True, blank=True, max_digits=5,decimal_places=3)

    wins = models.IntegerField(default=0, null=True, blank=True)
    loss = models.IntegerField(default=0, null=True, blank=True)

    team_owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def pre_save_team_id_receiver(sender, instance, *args, **kwargs):
    if not instance.team_id:
        instance.team_id = unique_team_id_generator(instance)

pre_save.connect(pre_save_team_id_receiver, sender=Team)



class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_members")
    member = models.ForeignKey(User, models.CASCADE, related_name="team_member")



class TeamGallery(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_gallery")
    caption = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=upload_gallery_path, null=True, blank=True)


class TeamSchedule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_schedules")
    date_time = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)



class TeamLineUp(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_lineups")
    player = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


class TeamPlayerInvite(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_player_invite")
    player = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)