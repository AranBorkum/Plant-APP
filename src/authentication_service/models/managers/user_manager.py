from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, password, first_name, last_name, telephone, user_id=None
    ):
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

    def create_superuser(self, email, username=None, password=None):
        email = self.normalize_email(email)
        user = self.create_user(email, password)
        user.staff = True
        user.admin = True
        user.save()
        return user
