from django.urls import path

from authentication_service.views import (
    LoginUserView,
    LogoutUserView,
    RegisterUserView,
    ResetPasswordView,
    SessionAuthTestView,
)

urlpatterns: list = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("test/", SessionAuthTestView.as_view(), name="test"),
]
