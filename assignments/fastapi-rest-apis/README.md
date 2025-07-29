# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete REST API using the FastAPI framework to manage a simple book library system, learning modern web development practices and API design principles.

## 📝 Tasks

### 🛠️ Basic API Setup and Book Management

#### Description
Create a FastAPI application with endpoints to manage a collection of books. You'll implement CRUD (Create, Read, Update, Delete) operations and learn about HTTP methods, status codes, and JSON responses.

#### Requirements
Completed program should:

- Set up a FastAPI application with proper project structure
- Create a Book model with fields: id, title, author, publication_year, genre, and available
- Implement GET /books endpoint to retrieve all books
- Implement GET /books/{book_id} endpoint to retrieve a specific book
- Implement POST /books endpoint to add a new book
- Include proper HTTP status codes (200, 201, 404, etc.)
- Use Pydantic models for request/response validation
- Include basic error handling for invalid requests

### 🛠️ Advanced API Features

#### Description
Enhance your API with additional features including filtering, updating records, user management, and API documentation. This task focuses on more advanced REST API concepts and best practices.

#### Requirements
Completed program should:

- Implement PUT /books/{book_id} endpoint to update book information
- Implement DELETE /books/{book_id} endpoint to remove books
- Add query parameters for filtering books (by genre, author, availability)
- Create User model and endpoints for user registration and management
- Implement book borrowing system (users can borrow/return books)
- Include automatic API documentation using FastAPI's built-in Swagger UI
- Add input validation and meaningful error messages
- Use dependency injection for common operations
- Include at least 10 sample books in your initial data
