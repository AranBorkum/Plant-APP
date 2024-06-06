from uuid import UUID

from pytest import fixture

from authentication_service.models import UserModel


@fixture
def registered_user_model(user_id: UUID) -> UserModel:
    user: UserModel = UserModel.objects.create_user(
        user_id=user_id,
        email="test@test.com",
        password="password",
        first_name="Test",
        last_name="Test",
        telephone="01234567890",
    )
    return user


__all__ = ["registered_user_model"]
