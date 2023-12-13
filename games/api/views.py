from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.serializers import serialize
from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from connects.api.serializers import ConnectSerializers
from connects.models import Connect
from events.api.serializers import EventSerializers, LeagueSerializers, AllLeagueSerializers, AllEventSerializers, \
    LeagueEventSerializers
from events.models import Event, League
from games.models import Game, Round
from teams.models import Team
from user_profile.models import UserProfile

User = get_user_model()


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_all_games_data(request):

    payload = {}
    data = {}
    errors = {}

    game_schedule = []
    recent_games = []
    current_tournaments = []

    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)

        if not user_id:
            errors["user_id"] = ['User ID is required']


        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']


        if errors:
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)


        data['game_schedule'] = game_schedule
        data['recent_games'] = recent_games
        data['current_tournaments'] = current_tournaments


        payload['message'] = "Successful"


        payload['data'] = data

    return Response(payload)



@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def games_brackets_view(request):
    payload = {}
    data = {}
    errors = {}

    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        event_id = request.query_params.get('event_id', None)

        if not user_id:
            errors["user_id"] = ['User ID is required']

        if not event_id:
            errors["event_id"] = ['Event ID is required']

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            errors["event_id"] = ['Event does not exist.']

        if not errors:
            # Fetch tournament brackets based on event_id
            tournament_data = {'tournament': {'rounds': []}}
            all_rounds = Round.objects.filter(event=event).prefetch_related('games__home_team', 'games__away_team').all()

            for round_obj in all_rounds:
                round_data = {
                    'round_id': round_obj.round_id,
                    'round_number': round_obj.number,
                    'round_name': round_obj.name,
                    'matches': []
                }

                for game in round_obj.games.all():
                    match_data = {
                        'team1': game.home_team.team_name,
                        'team2': game.away_team.team_name
                    }
                    round_data['matches'].append(match_data)

                tournament_data['tournament']['rounds'].append(round_data)

            data['brackets'] = tournament_data

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)

    payload['message'] = "Successful"
    payload['data'] = data

    return Response(payload)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def add_rounds_to_event(request):
    payload = {}
    data = {}
    errors = {}

    if request.method == 'POST':
        user_id = request.data.get('user_id')
        event_id = request.data.get('event_id')
        round_data = request.data.get('rounds')

        if not user_id:
            errors["user_id"] = ['User ID is required']

        if not event_id:
            errors["event_id"] = ['Event ID is required']

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            errors["event_id"] = ['Event does not exist.']

        if not errors:
            round_number = round_data['round_number']
            round_name = round_data['round_name']
            start_date_str = round_data['start_date']
            end_date_str = round_data['end_date']

            # Convert string dates to datetime objects
            #start_date = make_aware(datetime.fromisoformat(start_date_str))
            #end_date = make_aware(datetime.fromisoformat(end_date_str))

            # Create the round and associate it with the event
            round_obj = Round.objects.create(
                event=event,
                name=round_name,
                number=round_number,
                start_date=start_date_str,
                end_date=end_date_str,
                # Set other attributes accordingly
            )
            round_obj.save()

            data['message'] = 'Round added successfully'

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)

    payload['message'] = "Successful"
    payload['data'] = data
    return Response(payload)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def add_matches_to_round(request):
    payload = {}
    data = {}
    errors = {}

    if request.method == 'POST':
        user_id = request.data.get('user_id')
        round_id = request.data.get('round_id')
        matches_data = request.data.get('matches')

        if not user_id:
            errors["user_id"] = ['User ID is required']

        if not round_id:
            errors["round_id"] = ['Round ID is required']

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']

        try:
            round_obj = Round.objects.get(round_id=round_id)
        except Round.DoesNotExist:
            errors["round_id"] = ['Round does not exist.']

        if not errors:
            for match_data in matches_data:
                team_1_id = match_data['team_1_id']
                team_2_id = match_data['team_2_id']

                # Fetch Team objects based on team names
                team1 = Team.objects.get(team_id=team_1_id)
                team2 = Team.objects.get(team_id=team_2_id)

                # Create the match and associate it with the round
                match = Game.objects.create(
                    round=round_obj,
                    home_team=team1,
                    away_team=team2,
                    # Set other attributes accordingly
                )
                match.save()

            data['message'] = 'Matches added to the round successfully'

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)

    payload['message'] = "Successful"
    payload['data'] = data
    return Response(payload)
