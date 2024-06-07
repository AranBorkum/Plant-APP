from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from authentication_service.models import UserModel
from email_service.models import EmailLogModel
from fixtures.integration import (  # noqa
    patch_send_mail,
    patch_send_mail_raise_exception,
    register_user_email_failure_response,
    register_user_payload,
    register_user_response,
)


class TestCaseRegisterUser:
    @mark.django_db
    def test_register_user_returns_201(self, register_user_response: Response) -> None:
        assert register_user_response.status_code == status.HTTP_201_CREATED

    @mark.django_db
    def test_user_persisted_in_db(self, register_user_response: Response) -> None:
        assert UserModel.objects.filter(first_name="Test").count() == 1

    @mark.django_db
    def test_email_persisted_on_happy_path(
        self, register_user_response: Response
    ) -> None:
        emails = EmailLogModel.objects.filter()
        assert emails.count() == 1
        assert emails.last().send_status == 1


class TestCaseRegisterUserUnhappyPath:
    @mark.django_db
    def test_message_persisted_if_email_sending_fails(
        self, register_user_email_failure_response: Response
    ) -> None:
        assert UserModel.objects.filter(first_name="Test").count() == 1

    @mark.django_db
    def test_email_persisted_on_unhappy_path(
        self, register_user_email_failure_response: Response
    ) -> None:
        emails = EmailLogModel.objects.filter()
        assert emails.count() == 1
        assert emails.last().send_status == 2
