from django.urls import path

from accounts.api.views import register_user, verify_user_email, connects_endpoint, UserLogin, set_position_view

app_name = 'accounts'

urlpatterns = [
    path('register-user/', register_user, name="register_user"),
    path('verify-user-email/', verify_user_email, name="verify_user_email"),
    path('login-user/', UserLogin.as_view(), name="login_user"),
    path('connect-service/', connects_endpoint, name="connects_endpoint"),
    path('set-position/', set_position_view, name="set_position_view"),




]
