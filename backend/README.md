# Authentication API with FastAPI

## Overview

This project is an authentication API built with FastAPI. It includes features for user registration, login, and token validation. The API uses JWT for authentication and SQLite for storing user data.

## Prerequisites

- Python 3.8 or higher

## Installation

1. **Change Directory to backend:**

    ```bash
    cd /backend
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Database Path:**

   The database file will be automatically created for you if it does not already exist. 
   Ensure that the `DB_PATH` in `app/database.py` points to your SQLite database file. By default, it is set to:

    ```python
    DB_PATH = "/Users/m2air16-256/Developer/auth-app.db"
    ```

## Running the Application

1. **Start the server:**

    ```bash
    uvicorn app.main:app --reload
    ```

   This will start the FastAPI server with live reloading enabled.

2. **Access the API:**

   Open your browser and go to `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- **POST /login**: Authenticates a user and returns a JWT token.
- **GET /validate_token**: Validates a JWT token and returns user information.
- **POST /register**: Registers a new user.

## Example Requests

1. **Register a new user:**

    ```bash
    curl -X POST "http://127.0.0.1:8000/register" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
    ```

2. **Login with a user:**

    ```bash
    curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
    ```

3. **Validate a token:**

    ```bash
    curl -X 'GET' \
    'http://127.0.0.1:8000/validate_token?token=YOUR_JWT_TOKEN' \
    -H 'accept: application/json'
    ```

