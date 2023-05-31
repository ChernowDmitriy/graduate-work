import datetime
import logging
import uuid

import sqlalchemy as sa

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import declarative_base, sessionmaker

from infrastructures.config.base import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)

BaseModel = declarative_base()

engine = create_async_engine(settings.POSTGRES_URL)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)

_async_scoped_session = async_scoped_session(async_session, scopefunc=lambda: None)


class ORMBaseModel(BaseModel):
    __abstract__ = True

    id = sa.Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now())
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.now())

    def to_dict(self):
        res = {}
        for field in self.__dict__:
            if not field.startswith('_'):
                res[field] = self.__dict__[field]
        res['id'] = str(res['id'])
        return res
