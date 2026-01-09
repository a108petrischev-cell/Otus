from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import aiosqlite

DATABASE_URL = "sqlite+aiosqlite:///homework_04.db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")


async def get_session() -> AsyncSession:
    """Создает новую асинхронную сессию"""
    async with AsyncSession(engine) as session:
        yield session


async def init_db():
    """Создает таблицы"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
