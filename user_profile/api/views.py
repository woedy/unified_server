from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from connects.api.serializers import ConnectSerializers
from connects.models import Connect
from user_profile.models import UserProfile

User = get_user_model()

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_user_profile(request):

    payload = {}
    data = {}
    errors = {}

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

        user_profile = UserProfile.objects.get(user=user)
        user_connects = Connect.objects.filter(user=user)

        connects_serializer = ConnectSerializers(user_connects, many=True)
        if connects_serializer:
            connects_serializer = connects_serializer.data



        data['user_id'] = user.user_id
        data['email'] = user.email
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['is_online'] = user.is_online

        data['country'] = user_profile.country
        data['followers'] = user_profile.followers.count()
        data['following'] = user_profile.following.count()

        data['position'] = user_profile.position

        data['points_per_game'] = user_profile.points_per_game
        data['assists_per_game'] = user_profile.assists_per_game
        data['rebounds_per_game'] = user_profile.rebounds_per_game

        data['games_played'] = user_profile.games_played
        data['games_won'] = user_profile.games_won
        data['games_lost'] = user_profile.games_lost

        data['connects'] = connects_serializer





        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)