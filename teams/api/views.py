from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from connects.api.serializers import ConnectSerializers
from connects.models import Connect
from events.api.serializers import EventSerializers
from events.models import Event
from teams.api.serializers import TeamSerializers, AllTeamsSerializers
from teams.models import Team
from user_profile.models import UserProfile

User = get_user_model()

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_team_data(request):
    class CustomPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

    payload = {}
    data = {}
    errors = {}

    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        page_number = request.query_params.get('page', 1)  # Default to page 1 if not provided
        search_query = request.query_params.get('q', None)

        if not user_id:
            errors["user_id"] = ['User ID is required']
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)

        all_teams = Team.objects.all().order_by("-created_at")

        if search_query:
            all_teams = all_teams.filter(
                Q(team_name__icontains=search_query) |
                Q(team_about__icontains=search_query)
            )

        paginator = CustomPagination()
        paginated_result = paginator.paginate_queryset(all_teams, request)
        all_teams_serializer = AllTeamsSerializers(paginated_result, many=True)

        data["all_teams"] = all_teams_serializer.data
        data["total_pages"] = paginator.page.paginator.num_pages  # Get total number of pages
        data["current_page"] = paginator.page.number  # Get current page number

        payload['message'] = "Successful"
        payload['data'] = data

    return paginator.get_paginated_response(data)




@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_team_details_data(request):

    payload = {}
    data = {}
    errors = {}

    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        team_id = request.query_params.get('team_id', None)

        if not user_id:
            errors["user_id"] = ['User ID is required']

        if not team_id:
            errors["team_id"] = ['Team ID is required']

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']

        team_detail = Team.objects.get(team_id=team_id)
        team_detail_serializer = TeamSerializers(team_detail, many=False)
        if team_detail_serializer:
            team_detail_serializer = team_detail_serializer.data

        data["team_details"] = team_detail_serializer

        if errors:
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)


        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_team(request):
    payload = {}
    errors = {}
    data = {}

    if request.method == 'POST':
        user_id = request.data.get('user_id')
        team_name = request.data.get('team_name')
        team_logo = request.data.get('team_logo')
        selected_consoles = request.data.get('selected_consoles')

        if not user_id:
            errors["user_id"] = ['User ID is required']
        if not team_name:
            errors["team_name"] = ['Team name is required']
        if not team_logo:
            errors["team_logo"] = ['Logo is required']
        if not selected_consoles:
            errors["selected_consoles"] = ['Select at least 1 console']

        if not errors:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                errors["user_id"] = ['User does not exist.']
            else:
                new_team = Team.objects.create(
                    team_name=team_name,
                    team_logo=team_logo,
                    selected_consoles=selected_consoles,
                    team_owner=user
                )
                data['team_id'] = new_team.team_id
                data['team_name'] = new_team.team_name
                payload['message'] = "Successful"
                payload['data'] = data
                return Response(payload, status=status.HTTP_201_CREATED)

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)