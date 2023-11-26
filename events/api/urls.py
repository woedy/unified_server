from django.urls import path

from accounts.api.views import register_user, verify_user_email, connects_endpoint, UserLogin, set_position_view
from events.api.views import get_all_events, get_leagues_data, get_league_details_data, get_event_details_data
from leaderboards.api.views import get_league_event_details_data

app_name = 'events'

urlpatterns = [
    path('', get_all_events, name="all_events"),
    path('event-details/', get_event_details_data, name="get_event_details_data"),

    path('leagues/', get_leagues_data, name="get_leagues_data"),
    path('league-details/', get_league_details_data, name="get_league_details_data"),
    path('league-event-details/', get_league_event_details_data, name="get_league_event_details_data"),


]
