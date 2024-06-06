from dataclasses import dataclass

from django.db.models import Model


@dataclass
class DataclassBase:
    @classmethod
    def create(cls, model: Model) -> "DataclassBase":
        raise NotImplementedError()

    def as_dict(self) -> dict:
        raise NotImplementedError()
