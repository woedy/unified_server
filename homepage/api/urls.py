from django.urls import path

from accounts.api.views import register_user, verify_user_email, connects_endpoint, UserLogin, set_position_view
from homepage.api.views import get_home_page_data

app_name = 'homepage'

urlpatterns = [
    path('', get_home_page_data, name="get_home_page_data"),

]
