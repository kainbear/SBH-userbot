from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from database.config import settings
from typing import Annotated


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)


async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String[256]
    }