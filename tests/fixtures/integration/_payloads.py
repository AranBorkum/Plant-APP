from pytest import fixture


@fixture
def register_user_payload() -> dict:
    return {
        "first_name": "Test",
        "last_name": "Test",
        "telephone": "01234567890",
        "email": "test@test.com",
        "password": "password",
    }


@fixture
def login_user_payload() -> dict:
    return {
        "email": "test@test.com",
        "password": "password",
    }


@fixture
def reset_password_payload() -> dict:
    return {
        "email": "test@test.com",
        "password": "password",
        "new_password": "sufficiently_different_password",
    }


@fixture
def reset_password_too_similar_payload() -> dict:
    return {
        "email": "test@test.com",
        "password": "password",
        "new_password": "new_password",
    }


__all__ = [
    "register_user_payload",
    "login_user_payload",
    "reset_password_payload",
    "reset_password_too_similar_payload",
]
