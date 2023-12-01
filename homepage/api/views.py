from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()
@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_home_page_data(request):
    payload = {}
    data = {}
    errors = {}


    schedules = []
    games_played = []
    global_leaderboard = []
    global_player_leaderboard = []
    upcoming_events = []

    user_id = request.query_params.get('user_id', None)

    if not user_id:
        errors["user_id"] = ['User ID is required']

    try:
        qs = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        errors["user_id"] = ['User does not exist.']

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)



    data["schedules"] = schedules
    data["games_played"] = games_played
    data["global_leaderboard"] = global_leaderboard
    data["global_player_leaderboard"] = global_player_leaderboard
    data["upcoming_events"] = upcoming_events


    payload['message'] = "Successful"
    payload['data'] = data

    return Response(payload, status=status.HTTP_200_OK)

