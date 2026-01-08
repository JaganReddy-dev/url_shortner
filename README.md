# URL Shortener API

A simple URL shortener application built with FastAPI and MongoDB. Create users, generate API keys, and generate short URL paths for long URLs with Base62 encoding and obfuscation.

## Project Details

- **Author:** [Jagan](https://github.com/JaganReddy-dev)
- **Version:** 0.1.0

## Features

- **Create Users:** Register new users with unique lowercase usernames
- **Generate API Keys:** Create 28-character API keys with at least 4 digits
- **Generate Short URLs:** Convert long URLs to short URL paths using Base62 encoding
- **Retrieve User URLs:** Get all URL mappings created by a specific user
- **API Key Authentication:** Validate API keys for URL shortening requests
- **Duplicate URL Prevention:** Prevent duplicate short URLs for the same user

## Tech Stack

- **Framework:** FastAPI 0.121.0+
- **Database:** MongoDB (AsyncMongoClient)
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
API Documentation (Swagger UI): `http://localhost:8000/docs`

## API Endpoints

### Create User

- **Endpoint:** `POST /users/new`
- **Request:** `{"name": "username"}`
- **Response:** User object with id, user_name, is_active, created_at, updated_at
- **Status:** 201 Created

### Get User URLs

- **Endpoint:** `GET /users/{user_uuid}/urls`
- **Response:** List of URL mappings with long_url and short_url_path
- **Status:** 200 OK

### Create API Key

- **Endpoint:** `POST /api_key/new`
- **Request:** `{"user_uuid": "user_id", "api_key_name": "key_name"}`
- **Response:** API key object with id, name, api_key (plaintext), created_at, expires_at, user_id, is_active
- **Status:** 201 Created

### Generate Short URL

- **Endpoint:** `POST /short_url/new`
- **Request:** `{"long_url": "https://example.com/long/url", "api_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"}`
- **Response:** URL mapping object with id, short_url_path, long_url, created_at, expires_at, user_id, is_active
- **Status:** 200 OK

## How It Works

### User Creation

Users are created with unique lowercase usernames and stored in MongoDB.

### API Key Generation

- 28-character alphanumeric keys (uppercase letters A-Z and digits 0-9)
- Ensures at least 4 digits for randomness
- Keys are hashed with SHA256 before storage
- Plaintext key returned only at creation time
- 30-day expiration from creation date

### Short URL Generation

1. User submits long_url and api_key
2. API key is validated (hashed and checked in database)
3. Counter value is incremented and obfuscated using polynomial hash
4. Short URL path is generated using Base62 encoding
5. URL mapping stored with user association and 30-day expiration
6. Duplicate URLs for same user are rejected with 409 Conflict

### URL Retrieval

Users can retrieve all their URL mappings (long_url, short_url_path pairs).

## Error Responses

- `400 Bad Request` - Missing or invalid parameters (long_url or api_key)
- `401 Unauthorized` - Invalid or inactive API key
- `409 Conflict` - Duplicate username, API key name, or URL for user
- `500 Internal Server Error` - Short URL path collision (extremely rare)

## Database Collections

- **users** - User documents with user_name, is_active, created_at, updated_at
- **api_keys** - API key hashes with expiration and user association
- **url_map** - URL mappings with long_url, short_url_path, user_id, expiration
- **counter** - URL counter for generating unique IDs
