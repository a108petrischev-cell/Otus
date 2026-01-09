"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from typing import List, Dict, Any
from dataclasses import dataclass

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

@dataclass
class ApiResponse:
    data: List[Dict[str, Any]]
    status: int

async def fetch_json(session: aiohttp.ClientSession, url: str) -> ApiResponse:
    """Базовая функция для GET запросов с ответом в JSON"""
    async with session.get(url) as response:
        return ApiResponse(
            data=await response.json(),
            status=response.status
        )

async def fetch_users_data() -> List[dict]:
    """Загружает данные пользователей"""
    async with aiohttp.ClientSession() as session:
        result = await fetch_json(session, USERS_DATA_URL)
        if result.status == 200:
            return result.data
        raise ValueError(f"Ошибка загрузки пользователей: {result.status}")

async def fetch_posts_data() -> List[dict]:
    """Загружает данные постов"""
    async with aiohttp.ClientSession() as session:
        result = await fetch_json(session, POSTS_DATA_URL)
        if result.status == 200:
            return result.data
        raise ValueError(f"Ошибка загрузки постов: {result.status}")
