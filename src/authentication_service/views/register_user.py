from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication_service.service import authentication_service


class RegisterUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        return authentication_service.register_user(request)
