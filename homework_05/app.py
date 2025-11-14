from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers.api_router import router, books_list


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(router, prefix="/api")

@app.get("/", response_class=HTMLResponse, name="index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "books": books_list})

@app.get("/books/", response_class=HTMLResponse, name="books")
async def books(request: Request):
    return templates.TemplateResponse("books.html", {"request": request, "books": books_list})

@app.get("/books/{book_id}", response_class=HTMLResponse, name="book_detail")
async def book_detail(request: Request, book_id: int):
    book = next((book for book in books_list if book.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return templates.TemplateResponse("book_detail.html", {"request": request, "book": book})

@app.get("/about/", response_class=HTMLResponse, name="about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})