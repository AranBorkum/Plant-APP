from uuid import uuid4

from django.db.models import (
    CASCADE,
    DateTimeField,
    ForeignKey,
    IntegerField,
    Model,
    TextField,
    UUIDField,
)


class EmailLogModel(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    template = TextField(null=False)
    recipient = ForeignKey(
        "authentication_service.UserModel",
        on_delete=CASCADE,
    )
    send_status = IntegerField()
    created_timestamp = DateTimeField(auto_now_add=True)
