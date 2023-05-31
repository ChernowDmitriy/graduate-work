from typing import Union

from passlib.context import CryptContext

from core.domains.DTO.user import AuthUserSchemaInput, CreateUserSchemaInput
from core.domains.models.user_and_role import User as UserModel
from core.exceptions import UserEmailAlreadyExistsException
from core.services.user_service import UserService

from infrastructures.config.base import get_settings


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self._user_service = user_service
        self._password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self._settings = get_settings()

    def hash_password(self, password: str) -> str:
        return self._password_context.hash(password)

    # TODO: Need store refresh_token in table
    async def authenticate_user(self, data: AuthUserSchemaInput) -> Union[UserModel, None]:
        user = await self._user_service.get_user_by_email(data.email)
        if user and self.verify_password(data.password, user.password):
            return user
        return None

    async def sign_up(self, data: CreateUserSchemaInput) -> UserModel:
        existing_user = await self._user_service.get_user_by_email(data.email)
        if existing_user:
            raise UserEmailAlreadyExistsException

        hashed_password = self.hash_password(data.password)
        data.password = hashed_password
        insert_data = UserModel(**data.dict())
        created_user = await self._user_service.create_user(insert_data)
        return created_user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._password_context.verify(plain_password, hashed_password)
