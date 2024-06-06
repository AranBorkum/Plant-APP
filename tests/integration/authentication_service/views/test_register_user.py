from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from authentication_service.models import UserModel
from fixtures.integration import register_user_payload, register_user_response  # noqa


class TestCaseRegisterUser:
    @mark.django_db
    def test_register_user_returns_201(self, register_user_response: Response) -> None:
        assert register_user_response.status_code == status.HTTP_201_CREATED

    @mark.django_db
    def test_user_persisted_in_db(self, register_user_response: Response) -> None:
        assert UserModel.objects.filter(first_name="Test").count() == 1
