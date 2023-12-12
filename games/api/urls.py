from django.urls import path

from games.api.views import get_all_games_data, games_brackets_view, add_rounds_to_event

app_name = 'games'

urlpatterns = [
    path('', get_all_games_data, name="get_all_games_data"),
    path('brackets/', games_brackets_view, name="games_brackets_view"),
    path('add-rounds/', add_rounds_to_event, name="add_rounds_to_event"),

]
