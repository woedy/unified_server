from django.contrib.auth import get_user_model
from rest_framework import serializers

from connects.models import Connect
from events.models import Event, League
from user_profile.models import UserProfile

User = get_user_model()


class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'event_id',
            'event_title',
            'league',
            'event_description',
            'event_cover',
            'status',
            'event_type',
            'price',
            'event_start',
            'event_end',
            'event_rescheduled_at',
            'event_cancelled_at',
            'event_creator',
            'event_sign_ups',
            'event_consoles',
            'event_teams',
            'created_at',
        ]

class LeagueEventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'event_id',
            'event_title',
            'league',
            'event_description',
            'event_cover',
            'status',
            'event_type',
            'price',
            'event_start',
            'event_end',
            'event_rescheduled_at',
            'event_cancelled_at',
            'event_creator',
            'event_sign_ups',
            'event_consoles',
            'event_teams',

            'event_standings',
            'event_leaderboards',
            'event_awards',

            'created_at',
        ]


class AllEventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'event_id',
            'event_title',
            'event_type',
            'event_start',
            'event_cover',
            'event_consoles',

        ]


class LeagueManagerProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['photo',]


class LeagueManagerSerializers(serializers.ModelSerializer):
    personal_info = LeagueManagerProfileSerializers(many=False)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'personal_info']



class LeagueSerializers(serializers.ModelSerializer):
    league_manager = LeagueManagerSerializers(many=False)
    league_events = AllEventSerializers(many=True)
    class Meta:
        model = League
        fields = [
            'league_id',
            'league_name',
            'league_type',
            'league_logo',
            'league_about',
            'league_manager',
            'is_active',

            'league_events',

            'seasons',
            'tournaments',
            'draft_leagues',

            'created_at',
        ]



class AllLeagueSerializers(serializers.ModelSerializer):
    league_manager = LeagueManagerSerializers(many=False)

    class Meta:
        model = League
        fields = [
            'league_id',
            'league_name',
            'league_type',
            'league_logo',
            'league_manager',
        ]



