from django.contrib.auth import authenticate
from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer


class UserSerializerBase(Serializer):
    @staticmethod
    def check_user(clean_data: dict) -> AbstractBaseUser:
        user = authenticate(
            username=clean_data["email"],
            password=clean_data["password"],
        )
        if not user:
            raise ValidationError("User not found")
        return user
