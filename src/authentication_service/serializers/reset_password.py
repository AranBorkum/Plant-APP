from difflib import SequenceMatcher

from rest_framework.serializers import CharField, EmailField

from authentication_service.serializers._user_base import UserSerializerBase


class ResetPasswordSerializer(UserSerializerBase):
    email = EmailField()
    password = CharField()
    new_password = CharField()

    def validate(self, attrs: dict) -> dict:
        self._validate_password_similarity(
            attrs["password"],
            attrs["new_password"],
        )
        return attrs

    @staticmethod
    def _validate_password_similarity(password: str, new_password: str) -> None:
        assert SequenceMatcher(None, password, new_password).ratio() < 0.6
