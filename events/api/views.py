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
from events.api.serializers import EventSerializers, LeagueSerializers, AllLeagueSerializers, AllEventSerializers
from events.models import Event, League, EventSignUp
from payments.models import Payment
from teams.models import Team
from user_profile.models import UserProfile

User = get_user_model()


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def join_events(request):
    payload = {}
    errors = {}
    data = {}

    if request.method == 'POST':
        user_id = request.data.get('user_id', None)
        event_id = request.data.get('event_id', None)
        team_id = request.data.get('team_id', None)
        players = request.data.get('players', None)
        payment_info = request.data.get('payment_info', None)

        if not all([user_id, event_id, team_id, players, payment_info]):
            errors["required_fields"] = ['All required fields must be provided']
        else:
            holder_name = payment_info.get('holder_name')
            card_number = payment_info.get('card_number')
            expiry_month = payment_info.get('expiry_month')
            expiry_year = payment_info.get('expiry_year')
            cvc = payment_info.get('cvc')
            payment_type = payment_info.get('payment_type')

            if not all([holder_name, card_number, expiry_month, expiry_year, cvc, payment_type]):
                errors["payment_info"] = ['All payment information fields are required']

            # Check existence of user, event, and team
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                errors["user_id"] = ['User does not exist.']

            try:
                event = Event.objects.get(event_id=event_id)
            except Event.DoesNotExist:
                errors["event_id"] = ['Event does not exist.']

            try:
                team = Team.objects.get(team_id=team_id)
            except Team.DoesNotExist:
                errors["team_id"] = ['Team does not exist.']

            if not errors:
                # Event Signups
                new_event_signup = EventSignUp.objects.create(event=event, team=team)
                for player in players:
                    try:
                        p_user = User.objects.get(user_id=player)
                        new_event_signup.players.add(p_user)
                        new_event_signup.save()
                    except User.DoesNotExist:
                        errors["players"] = [f'Player with ID {player} does not exist.']

                # Add Payment
                new_payment = Payment.objects.create(
                    event=event,
                    team=team,
                    holder_name=holder_name,
                    card_number=card_number,
                    expiry_month=expiry_month,
                    expiry_year=expiry_year,
                    payment_type=payment_type,
                    cvc=cvc,
                    user=user
                )

                payload['message'] = "Successful"
                payload['data'] = data
                return Response(payload, status=status.HTTP_201_CREATED)

    if errors:
        payload['message'] = "Errors"
        payload['errors'] = errors
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_all_events(request):
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

        all_events = Event.objects.all().order_by("-created_at")

        if search_query:
            all_events = all_events.filter(
                Q(event_title__icontains=search_query) |
                Q(event_description__icontains=search_query)
            )

        paginator = CustomPagination()
        paginated_result = paginator.paginate_queryset(all_events, request)
        all_events_serializer = AllEventSerializers(paginated_result, many=True)

        data["all_events"] = all_events_serializer.data
        data["total_pages"] = paginator.page.paginator.num_pages  # Get total number of pages
        data["current_page"] = paginator.page.number  # Get current page number

        payload['message'] = "Successful"
        payload['data'] = data

    return paginator.get_paginated_response(data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_event_details_data(request):

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

        event_detail = Event.objects.get(event_id=event_id)
        event_detail_serializer = EventSerializers(event_detail, many=False)
        if event_detail_serializer:
            event_detail_serializer = event_detail_serializer.data

        data["event_details"] = event_detail_serializer

        if errors:
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)


        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)



@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_leagues_data(request):

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

        all_leagues = League.objects.all()
        all_leagues_serializer = AllLeagueSerializers(all_leagues, many=True)
        if all_leagues_serializer:
            all_leagues_serializer = all_leagues_serializer.data

        data["all_leagues"] = all_leagues_serializer

        if errors:
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)




        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)



@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def get_league_details_data(request):

    payload = {}
    data = {}
    errors = {}

    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        league_id = request.query_params.get('league_id', None)

        if not user_id:
            errors["user_id"] = ['User ID is required']

        if not league_id:
            errors["league_id"] = ['League ID is required']

        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            errors["user_id"] = ['User does not exist.']

        league_detail = League.objects.get(league_id=league_id)
        league_detail_serializer = LeagueSerializers(league_detail, many=False)
        if league_detail_serializer:
            league_detail_serializer = league_detail_serializer.data

        data["league_detail"] = league_detail_serializer

        if errors:
            payload['message'] = "Errors"
            payload['errors'] = errors
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)




        payload['message'] = "Successful"
        payload['data'] = data

    return Response(payload)