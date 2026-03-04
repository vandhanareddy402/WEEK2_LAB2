# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will have created a simple API for managing resources, understood routing, request/response models, and basic error handling.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Set up a new Python project with FastAPI and Uvicorn. Create a basic FastAPI application that runs a simple "Hello, world!" endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main application file (e.g., `main.py`)
- Define a root endpoint (`/`) that returns a welcome message


### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Expand your FastAPI app to include CRUD (Create, Read, Update, Delete) endpoints for a resource (e.g., books, users, or tasks). Use Pydantic models for request and response validation.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource
- Implement endpoints for creating, reading (all and by ID), updating, and deleting resources
- Store resources in an in-memory list or dictionary
- Return appropriate HTTP status codes and error messages


### 🛠️ Task 3: API Documentation and Testing

#### Description
Explore FastAPI's automatic API documentation and test your endpoints using the built-in Swagger UI.

#### Requirements
Completed program should:

- Access the interactive API docs at `/docs`
- Test all endpoints using the Swagger UI
- Add docstrings and descriptions to endpoints for better documentation
