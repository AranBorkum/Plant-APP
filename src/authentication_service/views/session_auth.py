from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class SessionAuthTestView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request: Request):
        return Response(status=status.HTTP_200_OK)
