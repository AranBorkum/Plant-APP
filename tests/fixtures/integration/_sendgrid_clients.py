from unittest.mock import MagicMock, Mock

from pytest import fixture
from sendgrid import SendGridAPIClient


@fixture
def sendgrid_client() -> SendGridAPIClient:
    return Mock(
        spec=SendGridAPIClient,
        send=MagicMock(return_value=Mock(status_code=200, body={}, headers={})),
    )


@fixture
def sendgrid_client_unsuccessful() -> SendGridAPIClient:
    return Mock(
        spec=SendGridAPIClient,
        send=MagicMock(return_value=Mock(status_code=400, body={}, headers={})),
    )


@fixture
def sendgrid_client_unhandled() -> SendGridAPIClient:
    return Mock(
        spec=SendGridAPIClient,
        send=MagicMock(return_value=Mock(status_code=418, body={}, headers={})),
    )


__all__ = [
    "sendgrid_client",
    "sendgrid_client_unsuccessful",
    "sendgrid_client_unhandled",
]
