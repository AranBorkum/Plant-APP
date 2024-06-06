from authentication_service.models import UserModel
from email_service.dataclasses import EmailLog
from email_service.models import EmailLogModel


class EmailRepository:
    model = EmailLogModel

    def create_model(self, email_log: EmailLog) -> EmailLogModel:
        email_log_model: EmailLogModel = self.model.objects.create(
            id=email_log.id,
            template=email_log.template.name,
            recipient=UserModel.objects.get(email=email_log.recipient),
            send_status=email_log.send_status.value,
            created_timestamp=email_log.created_timestamp,
        )
        return email_log_model


email_repository = EmailRepository()
