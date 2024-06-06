from typing import Any
from uuid import UUID

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str,
        first_name: str | None,
        last_name: str | None,
        telephone: int | None,
        user_id: UUID | None = None,
    ) -> Any:
        if not email:
            raise ValueError("An email address is required")
        if not password:
            raise ValueError("An password is required")

        email = self.normalize_email(email)
        user = (
            self.model(
                email=email,
                first_name=first_name,
                last_name=last_name,
                telephone=telephone,
            )
            if not user_id
            else self.model(
                user_id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                telephone=telephone,
            )
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        username: str | None = None,
    ) -> Any:
        email = self.normalize_email(email)
        user = self.create_user(email, password, None, None, None)
        user.staff = True
        user.admin = True
        user.save()
        return user
