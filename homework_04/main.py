import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import init_db, get_session, User, Post


async def save_users_batch(session: AsyncSession, users_data: List[dict]) -> None:
    users = [
        User(
            name=user["name"],
            username=user["username"],
            email=user["email"]
        )
        for user in users_data
    ]
    session.add_all(users)
    await session.commit()
    print(f"Сохранено {len(users)} пользователей")

async def save_posts_batch(session: AsyncSession, posts_data: List[dict]) -> None:
    posts = [
        Post(
            user_id=post["userId"],
            title=post["title"],
            body=post["body"]
        )
        for post in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    print(f"Сохранено {len(posts)} постов")

async def async_main() -> None:
    await init_db()

    async for session in get_session():
        # Конкурентная загрузка данных
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )

        # Пакетное сохранение
        await save_users_batch(session, users_data)
        await save_posts_batch(session, posts_data)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
