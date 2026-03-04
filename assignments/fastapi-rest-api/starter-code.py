# starter-code.py
"""
Starter code for FastAPI REST API assignment
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint returns a welcome message."""
    return {"message": "Welcome to your FastAPI REST API!"}

# Add your CRUD endpoints and models below
