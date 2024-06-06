from unittest.mock import MagicMock, Mock

from pytest import fixture
from sendgrid import SendGridAPIClient


@fixture
def sendgrid_client() -> SendGridAPIClient:
    return Mock(
        spec=SendGridAPIClient,
        send=MagicMock(return_value=Mock(status_code=200, body={}, headers={})),
    )


__all__ = ["sendgrid_client"]
