from django.urls import path

from accounts.api.views import register_user, verify_user_email, connects_endpoint, UserLogin, set_position_view
from events.api.views import get_all_events
from teams.api.views import get_team_data

app_name = 'teams'

urlpatterns = [
    path('', get_team_data, name="get_team_data"),


]
