from uuid import UUID, uuid4

from pytest import fixture

_USER_ID = uuid4()


@fixture
def user_id() -> UUID:
    return _USER_ID


__all__ = ["user_id"]
