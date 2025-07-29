# FastAPI REST API Starter Code
# Complete the TODOs to build your book library API

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Book Library API",
    description="A simple REST API for managing a book library",
    version="1.0.0"
)

# TODO: Define your Book model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    genre: str
    available: bool = True

# TODO: Define your User model
class User(BaseModel):
    # Add user fields here
    pass

# Sample data - replace with your own books
books_db = [
    {
        "id": 1,
        "title": "The Python Programming Language",
        "author": "Guido van Rossum",
        "publication_year": 1991,
        "genre": "Programming",
        "available": True
    },
    # TODO: Add 9 more sample books
]

users_db = []

# TODO: Implement GET /books - Get all books
@app.get("/books")
async def get_books():
    # Your code here
    pass

# TODO: Implement GET /books/{book_id} - Get specific book
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    # Your code here
    pass

# TODO: Implement POST /books - Add new book
@app.post("/books", status_code=201)
async def create_book(book: Book):
    # Your code here
    pass

# TODO: Implement PUT /books/{book_id} - Update book
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    # Your code here
    pass

# TODO: Implement DELETE /books/{book_id} - Delete book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    # Your code here
    pass

# TODO: Add filtering endpoint with query parameters
@app.get("/books/search")
async def search_books(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    author: Optional[str] = Query(None, description="Filter by author"),
    available: Optional[bool] = Query(None, description="Filter by availability")
):
    # Your code here
    pass

# TODO: Implement user endpoints
@app.post("/users", status_code=201)
async def create_user(user: User):
    # Your code here
    pass

# TODO: Implement book borrowing system
@app.post("/books/{book_id}/borrow")
async def borrow_book(book_id: int, user_id: int):
    # Your code here
    pass

@app.post("/books/{book_id}/return")
async def return_book(book_id: int, user_id: int):
    # Your code here
    pass

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Book Library API! Visit /docs for API documentation."}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
