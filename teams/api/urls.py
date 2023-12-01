from django.urls import path


from teams.api.views import get_team_data, create_team, get_team_details_data

app_name = 'teams'

urlpatterns = [
    path('', get_team_data, name="get_team_data"),
    path('team-details', get_team_details_data, name="get_team_details_data"),
    path('create-team', create_team, name="create_team"),


]
