from typing import AsyncIterator
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase
from app.config import settings


class Base(DeclarativeBase):
    pass


engine: AsyncEngine | None = None
SessionFactory: async_sessionmaker | None = None


async def init_db() -> None:
    global engine, SessionFactory
    engine = create_async_engine(str(settings.DATABASE_URL), echo=settings.DEBUG)
    SessionFactory = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionFactory() as session:
        yield session
