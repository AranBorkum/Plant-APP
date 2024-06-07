from django.test import Client
from pytest import fixture

from fixtures.integration import (
    _constants,
    _models,
    _patches,
    _payloads,
    _responses,
    _sendgrid_clients,
)
from fixtures.integration._constants import *
from fixtures.integration._models import *
from fixtures.integration._patches import *
from fixtures.integration._payloads import *
from fixtures.integration._responses import *
from fixtures.integration._sendgrid_clients import *


@fixture
def client() -> Client:
    client: Client = Client()
    return client


__all__ = (
    ["client"]
    + _constants.__all__
    + _models.__all__
    + _patches.__all__
    + _payloads.__all__
    + _responses.__all__
    + _sendgrid_clients.__all__
)
