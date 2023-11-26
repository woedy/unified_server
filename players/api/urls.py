from django.urls import path

from accounts.api.views import register_user, verify_user_email, connects_endpoint, UserLogin, set_position_view
from games.api.views import get_all_games_data
from homepage.api.views import get_home_page_data
from players.api.views import get_all_players

app_name = 'players'

urlpatterns = [
    path('', get_all_players, name="get_all_players"),

]
