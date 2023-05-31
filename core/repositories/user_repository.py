from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.domains.models.user_and_role import User as UserModel
from core.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, session_factory: AsyncSession):
        self._session = session_factory

    async def add(self, user: UserModel) -> UserModel:
        self._session.add(user)
        await self._session.commit()
        await self._session.refresh(user)
        await self._session.close()
        return UserModel(**user.to_dict())

    async def get(self, expr) -> Union[UserModel, None]:
        result = await self._session.execute(select(UserModel).filter_by(**expr))
        user_record = result.scalars().first()
        return UserModel(**user_record.to_dict()) if user_record else None

    async def update(self, *args, **kwargs) -> UserModel:
        pass

    async def delete(self, *args, **kwargs) -> UserModel:
        pass
