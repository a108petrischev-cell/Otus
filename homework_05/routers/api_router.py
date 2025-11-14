import uvicorn
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

class Book(BaseModel):
    id: int
    title: str
    author: str = Field(..., min_length=3)
    description: str | None = None

books_list = [
    Book(id=1, title="Изучаем Python, 5-е издание", author="Марк Лутц", description="Полное, подробное и авторитетное руководство по языку Python."),
    Book(id=2, title="Грокаем алгоритмы 2е издание", author="Адитья Бхаргава", description="Иллюстрированное пособие для программистов, любителей головоломок и других любознательных людей."),
    Book(id=3, title="Теоретический минимум по Сomputer Science", author="Владстон Феррейра Фило", description="Все, что нужно знать программисту и разработчику."),
 ]

@router.get("/books")
async def list_books():
    return books_list

@router.get("/books/{book_id}")
async def get_book(book_id: int):
    book = next((book for book in books_list if book.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/books")
async def create_book(book: Book):
    books_list.append(book)
    return book

if __name__ == "__main__":
    uvicorn.run("routers.api_router:router", host="127.0.0.1", port=8000, reload=True)