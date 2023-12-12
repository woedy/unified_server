from django.contrib.auth import get_user_model
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
from user_profile.models import UserProfile

User = get_user_model()


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_all_players(request):

    payload = {}
    data = {}
    errors = {}

    players = []

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


        data['players'] = players


        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)



