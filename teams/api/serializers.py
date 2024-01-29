from django.contrib.auth import get_user_model
from rest_framework import serializers

from connects.models import Connect
from events.models import Event
from teams.models import Team, TeamMember
from user_profile.models import UserProfile, GamerTag

User = get_user_model()


class TeamOwnerProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['photo',]


class TeamOwnerGamerTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = GamerTag
        fields = ['tag_name','console_type']


class TeamOwnerSerializers(serializers.ModelSerializer):
    personal_info = TeamOwnerProfileSerializers(many=False)
    user_gamer_tag = TeamOwnerGamerTagSerializers(many=True)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'personal_info', 'user_gamer_tag']



class TeamMemberSerializers(serializers.ModelSerializer):
    member = TeamOwnerSerializers(many=False)

    class Meta:
        model = TeamMember
        fields = ['id', 'member', 'is_invited']



class AllTeamsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'team_logo',
            'team_about',

            'selected_consoles',



            'wins',
            'loss',
        ]




class TeamSerializers(serializers.ModelSerializer):
    team_owner = TeamOwnerSerializers(many=False)
    team_members = TeamMemberSerializers(many=True)

    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'team_logo',
            'team_about',

            'selected_consoles',

            'points_per_game',
            'assists_per_game',
            'rebounds_per_game',

            'wins',
            'loss',

            'team_owner',

            'team_members',
            'team_gallery',
            'team_schedules',
            'team_lineups',


            'created_at',
        ]




