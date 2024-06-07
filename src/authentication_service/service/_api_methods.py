from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from authentication_service.serializers import (
    LoginUserSerializer,
    RegisterUserSerializer,
)
from authentication_service.serializers.reset_password import ResetPasswordSerializer
from email_service.enums import Email
from email_service.service import email_service
from project.api_response import ServiceAPIDataclass


class AuthenticationServiceAPIMethods:
    @staticmethod
    def register_user(request: Request) -> Response:
        serializer: RegisterUserSerializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return ServiceAPIDataclass.default_404()

        user = serializer.create(request.data)
        if not user:
            return ServiceAPIDataclass.default_404()

        email_service.send(Email.CONFIRM_SIGN_UP, [request.data["email"]])
        return ServiceAPIDataclass(
            status=status.HTTP_201_CREATED, data=serializer.data
        ).generate_response()

    @staticmethod
    def login_user(request: Request) -> Response:
        serializer = LoginUserSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return ServiceAPIDataclass.default_404()

        user = serializer.check_user(request.data)
        login(request, user)
        return ServiceAPIDataclass(
            status=status.HTTP_200_OK, data=dict()
        ).generate_response()

    @staticmethod
    def logout_user(request: Request) -> Response:
        logout(request)
        return ServiceAPIDataclass(
            status=status.HTTP_200_OK, data=dict()
        ).generate_response()

    @staticmethod
    def reset_password(request: Request) -> Response:
        serializer = ResetPasswordSerializer(data=request.data)
        try:
            serializer.is_valid()
        except AssertionError:
            return ServiceAPIDataclass.default_404()

        user = serializer.check_user(request.data)
        user.set_password(request.data["new_password"])
        user.save()
        return ServiceAPIDataclass(
            status=status.HTTP_200_OK, data=dict()
        ).generate_response()
