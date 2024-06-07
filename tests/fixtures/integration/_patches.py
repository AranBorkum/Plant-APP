from typing import Generator
from unittest.mock import MagicMock, patch

from pytest import fixture

from email_service.enums import EmailSendStatus
from email_service.service import EmailService


@fixture
def patch_send_mail() -> Generator | MagicMock:
    send_mail = patch.object(
        EmailService, "_send", return_value=EmailSendStatus.SENT
    ).start()
    yield send_mail
    send_mail.stop()


@fixture
def patch_send_mail_raise_exception() -> Generator | MagicMock:
    send_mail = patch.object(
        EmailService, "_send", return_value=EmailSendStatus.FAILED_TO_SEND
    ).start()
    yield send_mail
    send_mail.stop()


__all__ = ["patch_send_mail", "patch_send_mail_raise_exception"]
