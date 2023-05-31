import logging

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.interfaces.user_repository import IUserRepository
from core.repositories.user_repository import UserRepository
from core.services.auth_service import AuthService
from core.services.user_service import UserService
from infrastructures.database import _async_scoped_session

# TODO: Временно решение, т.к будет добавлен сервис для обработки логов ELK stash и нужно будет привести все логи к
#  единому виду
logger = logging.getLogger(__name__)


async def get_session() -> AsyncSession:
    async with _async_scoped_session() as session:
        try:
            yield session
        except Exception as error:
            logger.exception(error)
            await session.rollback()
        finally:
            await session.close()


async def get_user_repository(
        session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)


async def get_user_service(
        user_rep: IUserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_rep)


async def get_auth_service(
        user_service: UserService = Depends(get_user_service)
) -> AuthService:
    return AuthService(user_service)
