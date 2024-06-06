from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from authentication_service.models import UserModel
from authentication_service.repository import user_repository
from fixtures.integration import (  # noqa
    registered_user_model,
    reset_password_payload,
    reset_password_response,
    reset_password_too_similar_payload,
    reset_password_too_similar_response,
    user_id,
)


class TestCaseResetPassword:
    @mark.django_db
    def test_reset_password_returns_200(
        self, registered_user_model: UserModel, reset_password_response: Response
    ) -> None:
        assert reset_password_response.status_code == status.HTTP_200_OK

    @mark.django_db
    def test_reset_password_changes_password(
        self, registered_user_model: UserModel, reset_password_response: Response
    ) -> None:
        user: UserModel = user_repository.get_model(
            user_id=registered_user_model.user_id
        )
        assert user.check_password("sufficiently_different_password")

    @mark.django_db
    def test_reset_password_too_similar_fails(
        self,
        registered_user_model: UserModel,
        reset_password_too_similar_response: Response,
    ) -> None:
        assert (
            reset_password_too_similar_response.status_code == status.HTTP_404_NOT_FOUND
        )
