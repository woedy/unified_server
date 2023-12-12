from django.contrib.auth import get_user_model
from django.core.serializers import serialize
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
                    'round_number': round_obj.name,
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
        event_id = request.data.get('event_id')
        round_data = request.data.get('rounds')  # Assuming rounds data is provided in a suitable format

        if not event_id:
            errors["event_id"] = ['Event ID is required']

        try:
            event = Event.objects.get(event_id=event_id)
        except Event.DoesNotExist:
            errors["event_id"] = ['Event does not exist.']

        if not errors:
            for round_info in round_data:
                round_number = round_info.get('round_number')
                round_name = round_info.get('round_name')
                # Other round data retrieval from round_info

                # Create the round and associate it with the event
                round_obj = Round.objects.create(
                    event=event,
                    name=round_name,
                    number=round_number,
                    # Set other attributes accordingly
                )
                round_obj.save()

            data['message'] = 'Rounds added successfully'

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)

    payload['message'] = "Successful"
    payload['data'] = data
    return Response(payload)