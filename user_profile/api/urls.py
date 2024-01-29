from django.urls import path

from accounts.api.views import register_user
from user_profile.api.views import get_user_profile, add_gamer_tag

app_name = 'user_profile'

urlpatterns = [
    path('', get_user_profile, name="get_user_profile"),
    path('add-gamer-tag/', add_gamer_tag, name="add_gamer_tag"),


]
