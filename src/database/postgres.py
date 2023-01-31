from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

url = 'postgresql+asyncpg://postgres:postgres@postgres:5432/bbmp'

async_engine = create_async_engine(
    url,
    poolclass=NullPool,
    future=True
)

# noinspection PyTypeChecker
local_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
