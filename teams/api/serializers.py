from django.contrib.auth import get_user_model
from rest_framework import serializers

from connects.models import Connect
from events.models import Event
from teams.models import Team

User = get_user_model()


class TeamSerializers(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'team_logo',
            'team_about',

            'selected_console',

            'points_per_game',
            'assists_per_game',
            'rebounds_per_game',

            'wins',
            'loss',

            'team_owner',

            'team_members',
            'team_events',
            'team_gallery',
            'team_schedules',
            'team_lineups',


            'created_at',
        ]




