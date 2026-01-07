# URL Shortener API

A simple URL shortener application built with FastAPI and MongoDB. Create users, generate API keys, and generate short URL paths for long URLs with Base62 encoding.

## Project Details

- **Author:** [Jagan](https://github.com/JaganReddy-dev)
- **Version:** 0.1.0

## Features

- **Create Users:** Register new users with unique usernames
- **Generate API Keys:** Create API keys (28 characters) for user authentication
- **Generate Short URLs:** Convert long URLs to short URL paths using Base62 encoding
- **API Key Authentication:** Validate API keys for URL shortening requests
- **Duplicate URL Prevention:** Prevent duplicate short URLs for the same user

## Tech Stack

- **Framework:** FastAPI 0.121.0+
- **Database:** MongoDB 4.15.5+
- **Server:** Uvicorn 0.38.0+
- **Validation:** Pydantic 2.12.3+, Pydantic Settings 2.12.0+
- **Utilities:** python-dotenv 1.2.1+, PyMongo 4.15.5+

## Installation

### Prerequisites

- Python 3.14+
- MongoDB instance

### Clone the Repository

```bash
git clone https://github.com/JaganReddy-dev/url-shortener.git
cd url-shortener
```

### Install Dependencies

```bash
pip install -e .
```

### Environment Setup

Create a `.env` file in the root directory:

```plaintext
ENV=development
BASE_URI=http://localhost:8000
DB_URI=mongodb+srv://username:password@cluster.mongodb.net/
BASE62=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

## Running the Application

```bash
uvicorn shortener_app.main:app --reload
```

The API will be available at `http://localhost:8000`

- **API Documentation:** `http://localhost:8000/docs`

## API Endpoints

### Create User

- **Endpoint:** `POST /users/`
- **Request:** `{"name": "username"}`
- **Response:** `{"id": "...", "user_name": "...", "is_active": true, "created_at": "...", "updated_at": "..."}`
- **Status:** 201 Created

### Create API Key

- **Endpoint:** `POST /api_key/`
- **Request:** `{"user_uuid": "user_id", "api_key_name": "key_name"}`
- **Response:** `{"id": "...", "name": "...", "api_key": "...", "created_at": "...", "expires_at": "...", "user_id": "...", "is_active": true}`
- **Status:** 201 Created

### Generate Short URL

- **Endpoint:** `POST /short_url/new`
- **Request:** `{"long_url": "https://example.com/very/long/url", "api_key": "YOUR_API_KEY"}`
- **Response:** `{"id": "...", "long_url": "...", "short_url_path": "...", "created_at": "...", "expires_at": "...", "user_id": "...", "is_active": true}`
- **Status:** 200 OK

## Project Structure

```
shortener_app/
├── main.py                 # FastAPI app setup
├── config.py              # Configuration
├── Routes/                # API route handlers
├── Services/              # Business logic
├── Models/v1/             # Request/response models
├── Schemas/               # Database schemas
├── Data/DB/               # Database client
└── Utils/                 # Utility functions
```

## How It Works

### User Creation

Users are created with a unique lowercase username and stored in MongoDB.

### API Key Generation

- 28-character alphanumeric keys (uppercase letters and digits)
- Keys are hashed before storage
- 30-day expiration from creation date
- Plaintext key returned only once during creation

### Short URL Generation

1. User submits a long URL with a valid API key
2. API key is validated (must be active and not expired)
3. Short URL path is generated using Base62 encoding
4. URL mapping is stored with user association
5. Duplicate URLs for the same user are rejected

## Error Responses

- `400 Bad Request` - Missing or invalid parameters
- `401 Unauthorized` - Invalid or expired API key
- `409 Conflict` - Duplicate username, API key name, or URL
- `500 Internal Server Error` - Short URL generation collision (rare)
