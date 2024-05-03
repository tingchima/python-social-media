from ..domain.entities import User as UserEntity
from ..infrastructure.postgres.user_repository import UserRepository


class UserService:
    """Represents a service of user."""

    user_repo: UserRepository = UserRepository()

    def user_create(self, param: UserEntity) -> UserEntity:
        user = self.user_repo.save(param)
        return user

    def user_get_by_email(self, email: str) -> UserEntity:
        user = self.user_repo.user_get_by_email(email)
        return user
