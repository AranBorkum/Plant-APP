from typing import Type
from unittest.mock import Mock

from pytest import fixture
from sendgrid.helpers.mail import Mail

from email_service.interfaces import IMailGenerator


@fixture
def mail_generator() -> Type[IMailGenerator]:
    class MailGenerator(IMailGenerator):
        def build(self) -> Mail:
            return Mock(spec=Mail)

    return MailGenerator


__all__ = ["mail_generator"]
