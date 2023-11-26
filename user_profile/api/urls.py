from django.urls import path

from accounts.api.views import register_user
from user_profile.api.views import get_user_profile

app_name = 'user_profile'

urlpatterns = [
    path('', get_user_profile, name="get_user_profile"),


]
