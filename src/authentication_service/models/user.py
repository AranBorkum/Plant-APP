from datetime import datetime
from uuid import UUID, uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import (
    BooleanField,
    CharField,
    DateField,
    EmailField,
    IntegerField,
    UUIDField,
)

from authentication_service.models.managers import CustomUserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    user_id: UUID | UUIDField = UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    first_name: str | CharField = CharField(max_length=100)
    last_name: str | CharField = CharField(max_length=100)
    telephone: int | IntegerField = IntegerField()
    email: str | EmailField = EmailField(max_length=100, unique=True)
    is_active: bool | BooleanField = BooleanField(default=True)
    is_staff: bool | BooleanField = BooleanField(default=False)
    date_joined: datetime | DateField = DateField(auto_now_add=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
