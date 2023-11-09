from django.urls import path

from accounts.api.views import register_user

app_name = 'accounts'

urlpatterns = [
    path('register-user/', register_user, name="register_user"),


]
