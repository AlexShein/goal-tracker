from typing import AsyncGenerator, Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta

from goal_tracker.settings import DB_ADDR, DB_PASS, DB_USER

SQLALCHEMY_DATABASE_URL = "postgresql{extra}://" f"{DB_USER}:{DB_PASS}@{DB_ADDR}"


Base = declarative_base()

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL.format(extra="+asyncpg"), pool_pre_ping=True, max_overflow=100
)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db() -> AsyncGenerator[DeclarativeMeta, None]:
    db_session = async_session()
    try:
        yield db_session
    finally:
        await db_session.close()


sync_engine = create_engine(SQLALCHEMY_DATABASE_URL.format(extra=""), pool_pre_ping=True, max_overflow=100)

sync_session = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)


def get_sync_db() -> Generator[DeclarativeMeta, None, None]:
    db_session = sync_session()
    try:
        yield db_session
    finally:
        db_session.close()
