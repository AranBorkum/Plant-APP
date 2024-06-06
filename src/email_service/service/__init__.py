from requests import Response
from sendgrid import SendGridAPIClient

from email_service.dataclasses import EmailLog
from email_service.enums import EmailSendStatus
from email_service.exceptions import FailedToSendEmailException
from email_service.interfaces import IMailGenerator
from email_service.repositories import email_repository
from email_service.service._mail_generator import MailGenerator


class EmailService:
    repository = email_repository

    def send(
        self,
        mail_generator: IMailGenerator,
        sendgrid_client: SendGridAPIClient,
    ) -> None:
        self._send_message(mail_generator, sendgrid_client)

    def _send_message(
        self,
        mail_generator: IMailGenerator,
        sendgrid_client: SendGridAPIClient,
    ) -> None:
        try:
            response: Response = sendgrid_client.send(mail_generator.build())
        except Exception as exception:
            raise FailedToSendEmailException from exception

        self._persist_email_log(mail_generator, response)

    def _persist_email_log(
        self, mail_generator: IMailGenerator, response: Response
    ) -> None:
        response_status_to_send_status = {
            200: EmailSendStatus.SENT,
            400: EmailSendStatus.FAILED_TO_SEND,
        }

        email_log = EmailLog(
            template=mail_generator.template,
            recipient=mail_generator.recipient,
            send_status=response_status_to_send_status.get(
                response.status_code,
                EmailSendStatus.UNDEFINED,
            ),
        )
        self.repository.create_model(email_log)


email_service = EmailService()
