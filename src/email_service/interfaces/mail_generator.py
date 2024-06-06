import re
from abc import ABC, abstractmethod

from sendgrid.helpers.mail import Mail

from email_service.enums import Email

_email_pattern = (
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}"
    r"[a-zA-Z0-9])?(?:\.[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)


class IMailGenerator(ABC):
    def __init__(self, email_information: Email, recipient: str) -> None:
        self._email_information: Email = email_information
        self._recipient: str = recipient
        assert recipient, "A valid string is required to send an email"
        assert re.search(_email_pattern, self._recipient)

    @property
    def template(self) -> Email:
        return self._email_information

    @property
    def recipient(self) -> str:
        return self._recipient

    @abstractmethod
    def build(self) -> Mail: ...
