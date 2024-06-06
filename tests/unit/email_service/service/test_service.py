from typing import Type
from unittest.mock import MagicMock

from pytest import raises
from sendgrid import SendGridAPIClient

from email_service.enums import Email
from email_service.interfaces import IMailGenerator
from email_service.service import email_service
from fixtures.unit import (  # noqa
    mail_generator,
    patch_email_repository_create_model,
    patch_email_service_send_message,
    sendgrid_client,
)


class TestCaseEmailClient:
    def test_valid_email_happy_response(
        self,
        mail_generator: Type[IMailGenerator],
        sendgrid_client: SendGridAPIClient,
        patch_email_repository_create_model: MagicMock,
    ) -> None:
        generator = mail_generator(Email.CONFIRM_SIGN_UP, "test@test.com")
        email_service.send(generator, sendgrid_client)

    def test_invalid_email_unhappy_response(
        self,
        mail_generator: Type[IMailGenerator],
        sendgrid_client: SendGridAPIClient,
        patch_email_service_send_message: MagicMock,
    ) -> None:
        with raises(Exception):
            generator = mail_generator(Email.CONFIRM_SIGN_UP, "test@ test.com")
            email_service.send(generator, sendgrid_client)

        patch_email_service_send_message.assert_not_called()
