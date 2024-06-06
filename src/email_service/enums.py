import os.path
from collections import namedtuple
from enum import Enum

from email_service.paths import __email_templates__

EmailInfo = namedtuple("EmailInfo", ["template", "subject", "sender"])
DEFAULT_SENDER = ""


class Email(Enum):
    CONFIRM_SIGN_UP = EmailInfo(
        os.path.join(__email_templates__, "confirm_sign_up.html"),
        "One last step before you're fully registered",
        DEFAULT_SENDER,
    )


class EmailSendStatus(Enum):
    UNDEFINED = 0
    SENT = 1
    FAILED_TO_SEND = 2
