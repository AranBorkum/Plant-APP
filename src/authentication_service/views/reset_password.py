from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication_service.service import authentication_service


class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request: Request) -> Response:
        return authentication_service.reset_password(request)
