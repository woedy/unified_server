from django.urls import path


from teams.api.views import get_team_data, create_team, get_team_details_data, invite_player_view, \
    invite_player_email_view

app_name = 'teams'

urlpatterns = [
    path('', get_team_data, name="get_team_data"),
    path('team-details', get_team_details_data, name="get_team_details_data"),
    path('create-team', create_team, name="create_team"),
    path('invite-player', invite_player_view, name="invite_player_view"),
    path('invite-player-email', invite_player_email_view, name="invite_player_email_view"),

]
