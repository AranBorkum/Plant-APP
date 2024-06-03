from rest_framework.serializers import CharField, EmailField

from authentication_service.serializers._user_base import UserSerializerBase


class LoginUserSerializer(UserSerializerBase):
    email = EmailField()
    password = CharField()
