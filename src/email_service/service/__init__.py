import logging

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from email_service.dataclasses import EmailLog
from email_service.enums import Email, EmailSendStatus
from email_service.repositories import email_repository

logger = logging.getLogger(__name__)


class EmailService:
    repository = email_repository

    def send(self, email: Email, recipient_list: list[str]) -> None:
        for recipient in recipient_list:
            send_status = self._send(email, recipient)
            self._persist_email_log(email, recipient, send_status)

    @staticmethod
    def _send(email: Email, recipient: str) -> EmailSendStatus:
        html_message = render_to_string(email.value.template, {"context": "values"})
        try:
            send_mail(
                subject=email.value.subject,
                html_message=html_message,
                message=strip_tags(html_message),
                from_email=email.value.sender,
                recipient_list=[recipient],
                fail_silently=False,
            )
            return EmailSendStatus.SENT
        except Exception as exception:
            logger.warning(f"Encountered exception {exception.__class__.__name__}")
            return EmailSendStatus.FAILED_TO_SEND

    def _persist_email_log(
        self, email: Email, recipient: str, send_status: EmailSendStatus
    ) -> None:
        email_log = EmailLog(
            template=email,
            recipient=recipient,
            send_status=send_status,
        )
        self.repository.create_model(email_log)


email_service = EmailService()
