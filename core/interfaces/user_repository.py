from abc import ABC, abstractmethod

from core.domains import User as UserModel


class IUserRepository(ABC):
    @abstractmethod
    async def add(self, *args, **kwargs) -> UserModel: pass

    @abstractmethod
    async def get(self, *args, **kwargs) -> UserModel: pass

    @abstractmethod
    async def update(self, *args, **kwargs) -> UserModel: pass

    @abstractmethod
    async def delete(self, *args, **kwargs) -> UserModel: pass
