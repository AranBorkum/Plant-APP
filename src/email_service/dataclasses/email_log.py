from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from django.utils import timezone

from email_service.enums import Email, EmailSendStatus
from email_service.models import EmailLogModel


@dataclass
class EmailLog:
    template: Email
    recipient: str
    send_status: EmailSendStatus
    created_timestamp: datetime = field(default_factory=timezone.now)
    id: UUID = field(default_factory=uuid4)

    @classmethod
    def create(cls, model: EmailLogModel) -> "EmailLog":
        return EmailLog(
            id=model.id,
            template=Email[model.template],
            recipient=model.recipient.email,
            send_status=EmailSendStatus(model.send_status),
            created_timestamp=model.created_timestamp,
        )

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "template": self.template.name,
            "recipient": self.recipient,
            "send_status": self.send_status.value,
            "created_timestamp": self.created_timestamp,
        }
