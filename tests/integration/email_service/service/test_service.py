from typing import Type

from pytest import mark
from sendgrid import SendGridAPIClient

from authentication_service.models import UserModel
from email_service.dataclasses import EmailLog
from email_service.enums import Email, EmailSendStatus
from email_service.interfaces import IMailGenerator
from email_service.models import EmailLogModel
from email_service.service import email_service
from fixtures.integration import (  # noqa
    mail_generator,
    sendgrid_client,
    sendgrid_client_unhandled,
    sendgrid_client_unsuccessful,
    user_model,
)


class TestCaseEmailService:
    @mark.django_db
    def test_log_persisted_on_email_sent(
        self,
        mail_generator: Type[IMailGenerator],
        sendgrid_client: SendGridAPIClient,
        user_model: UserModel,
    ) -> None:
        assert EmailLogModel.objects.count() == 0
        generator = mail_generator(Email.CONFIRM_SIGN_UP, "test@test.com")
        email_service.send(generator, sendgrid_client)
        assert EmailLogModel.objects.count() == 1
        email_log = EmailLog.create(EmailLogModel.objects.last())
        assert email_log.send_status == EmailSendStatus.SENT

    @mark.django_db
    def test_log_persisted_on_email_sent_unsuccessful(
        self,
        mail_generator: Type[IMailGenerator],
        sendgrid_client_unsuccessful: SendGridAPIClient,
        user_model: UserModel,
    ) -> None:
        assert EmailLogModel.objects.count() == 0
        generator = mail_generator(Email.CONFIRM_SIGN_UP, "test@test.com")
        email_service.send(generator, sendgrid_client_unsuccessful)
        assert EmailLogModel.objects.count() == 1
        email_log = EmailLog.create(EmailLogModel.objects.last())
        assert email_log.send_status == EmailSendStatus.FAILED_TO_SEND

    @mark.django_db
    def test_log_persisted_on_email_sent_unhandled(
        self,
        mail_generator: Type[IMailGenerator],
        sendgrid_client_unhandled: SendGridAPIClient,
        user_model: UserModel,
    ) -> None:
        assert EmailLogModel.objects.count() == 0
        generator = mail_generator(Email.CONFIRM_SIGN_UP, "test@test.com")
        email_service.send(generator, sendgrid_client_unhandled)
        assert EmailLogModel.objects.count() == 1
        email_log = EmailLog.create(EmailLogModel.objects.last())
        assert email_log.send_status == EmailSendStatus.UNDEFINED
