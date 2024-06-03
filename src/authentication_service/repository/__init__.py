from authentication_service.models import UserModel
from project.repositories.repository import RepositoryBase


class UserRepository(RepositoryBase):
    service_model = UserModel


user_repository = UserRepository()
