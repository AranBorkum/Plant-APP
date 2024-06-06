from rest_framework.request import Request
from rest_framework.response import Response

from authentication_service.serializers import (
    LoginUserSerializer,
    RegisterUserSerializer,
)
from authentication_service.service._api_methods import AuthenticationServiceAPIMethods


class AuthenticationService:
    def __init__(self) -> None:
        self.api_methods = AuthenticationServiceAPIMethods()

    def register_user(self, request: Request) -> Response:
        response: Response = self.api_methods.register_user(request)
        return response

    def login_user(self, request: Request) -> Response:
        response: Response = self.api_methods.login_user(request)
        return response

    def logout_user(self, request: Request) -> Response:
        response: Response = self.api_methods.logout_user(request)
        return response

    def reset_password(self, request: Request) -> Response:
        response: Response = self.api_methods.reset_password(request)
        return response


authentication_service = AuthenticationService()
