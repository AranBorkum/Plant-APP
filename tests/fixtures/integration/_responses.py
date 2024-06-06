from typing import Any

from django.test import Client
from pytest import fixture
from rest_framework.response import Response


@fixture
def register_user_response(
    client: Client,
    register_user_payload: dict,
) -> Response | Any:
    return client.post("/auth/register/", register_user_payload)


@fixture
def login_user_response(
    client: Client,
    login_user_payload: dict,
) -> Response | Any:
    return client.post("/auth/login/", login_user_payload)


@fixture
def logout_user_response(
    client: Client,
) -> Response | Any:
    return client.post("/auth/logout/", {})


@fixture
def reset_password_response(
    client: Client,
    reset_password_payload: dict,
) -> Response | Any:
    return client.post("/auth/reset-password/", reset_password_payload)


@fixture
def reset_password_too_similar_response(
    client: Client,
    reset_password_too_similar_payload: dict,
) -> Response | Any:
    return client.post("/auth/reset-password/", reset_password_too_similar_payload)


__all__ = [
    "register_user_response",
    "login_user_response",
    "logout_user_response",
    "reset_password_response",
    "reset_password_too_similar_response",
]
