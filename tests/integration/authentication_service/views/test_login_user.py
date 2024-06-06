from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from authentication_service.models import UserModel
from fixtures.integration import (  # noqa
    login_user_payload,
    login_user_response,
    registered_user_model,
    user_id,
)


class TestCaseLoginUser:
    @mark.django_db
    def test_login_valid_user_returns_200(
        self,
        registered_user_model: UserModel,
        login_user_response: Response,
    ) -> None:
        assert login_user_response.status_code == status.HTTP_200_OK

    @mark.django_db
    def test_login_valid_user_sets_session(
        self,
        registered_user_model: UserModel,
        login_user_response: Response,
    ) -> None:
        assert login_user_response.cookies.get("sessionid")

    @mark.django_db
    def test_login_invalid_user_returns_400(
        self,
        login_user_response: Response,
    ) -> None:
        assert login_user_response.status_code == status.HTTP_400_BAD_REQUEST
