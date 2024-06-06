from typing import Any, Type
from uuid import UUID

from django.db.models import Model, QuerySet

from project.dataclasses import DataclassBase


class RepositoryBase:
    service_model: Type[Model]

    def get_model(self, **kwargs: Any) -> Model:
        model = self.service_model.objects.get(**kwargs)
        return model

    def filter_models(self, **kwargs: Any) -> QuerySet:
        models = self.service_model.objects.filter(**kwargs)
        return models

    def create_model(self, **kwargs: Any) -> Model:
        model = self.service_model.objects.create(**kwargs)
        return model

    def update_model(self, id_: UUID, obj: DataclassBase) -> Model:
        model = self.get_model(id=id_)
        for key, value in obj.as_dict().items():
            if key != "id":
                setattr(model, key, value)

        model.save()
        return model
