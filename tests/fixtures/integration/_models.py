from pytest import fixture

from authentication_service.models import UserModel


@fixture
def user_model() -> None:
    UserModel.objects.create(
        first_name="test",
        last_name="test",
        telephone="0123456789",
        email="test@test.com",
    )


__all__ = ["user_model"]
