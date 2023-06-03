import uuid
from typing import Union

from core.domains import User as UserModel
from core.interfaces.user_repository import IUserRepository


class UserService:
    def __init__(self, user_rep: IUserRepository):
        self._user_rep = user_rep

    async def create_user(self, user: UserModel) -> UserModel:
        user = await self._user_rep.add(user)
        return user

    async def get_user_by_email(self, email: str) -> Union[UserModel, None]:
        result = await self._user_rep.get({'email': email})
        return result

    async def get_user_by_id(self, user_id: Union[str, uuid.UUID]) -> Union[UserModel, None]:
        result = await self._user_rep.get({'id': str(user_id)})
        return result
