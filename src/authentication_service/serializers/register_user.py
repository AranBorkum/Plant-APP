from typing import Any

from rest_framework.serializers import ModelSerializer

from authentication_service.models import UserModel


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, clean_data: dict) -> Any:
        user_obj = UserModel.objects.create_user(
            first_name=clean_data["first_name"],
            last_name=clean_data["last_name"],
            telephone=clean_data["telephone"],
            email=clean_data["email"],
            password=clean_data["password"],
        )
        user_obj.username = clean_data["email"]
        user_obj.save()
        return user_obj
