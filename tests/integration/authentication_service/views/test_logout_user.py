from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from fixtures.integration import logout_user_response, register_user_payload  # noqa


class TestCaseRegisterUser:
    @mark.django_db
    def test_logout_user_returns_200(self, logout_user_response: Response) -> None:
        assert logout_user_response.status_code == status.HTTP_200_OK
