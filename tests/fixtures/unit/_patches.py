from typing import Generator
from unittest.mock import MagicMock, patch

from pytest import fixture

from email_service.service import email_service


@fixture
def patch_email_repository_create_model() -> Generator | MagicMock:
    create_model = patch.object(email_service, "_persist_email_log").start()
    yield create_model
    create_model.stop()


@fixture
def patch_email_service_send_message() -> Generator | MagicMock:
    send_message = patch.object(email_service, "_send_message").start()
    yield send_message
    send_message.stop()


__all__ = ["patch_email_repository_create_model", "patch_email_service_send_message"]
