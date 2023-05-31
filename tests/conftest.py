import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

from infrastructures.config.test.settings import get_settings

settings = get_settings()


@pytest.fixture(scope="session")
async def session() -> AsyncSession:
    async_engine = create_async_engine(settings.POSTGRES_URL)
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
    )

    _async_scoped_session = async_scoped_session(async_session, scopefunc=lambda: None)

    async with _async_scoped_session() as session:
        try:
            yield session
        except Exception as error:
            print(error)
            await session.rollback()
        finally:
            await session.close()
