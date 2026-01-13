# URL Shortener API

A simple URL shortener application built with FastAPI and MongoDB. Create users, generate API keys, and generate short URL paths for long URLs with Base62 encoding and obfuscation.

## Project Details

- **Author:** [Jagan](https://github.com/JaganReddy-dev)
- **Version:** 0.1.0

## Features

- **User Authentication:** Sign up and login with username and password
- **Generate API Keys:** Create API keys for users
- **Generate Short URLs:** Convert long URLs to short URL paths using Base62 encoding
- **Retrieve User URLs:** Get all URL mappings created by a specific user

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

### Sign Up

- **Endpoint:** `POST /auth/signup`
- **Request:** `{"username": "username", "password": "password"}`
- **Response:** User object
- **Status:** 201 Created

### Login

- **Endpoint:** `POST /auth/login`
- **Request:** `{"username": "username", "password": "password"}`
- **Response:** Boolean (true if authentication successful)
- **Status:** 200 OK

### Create API Key

- **Endpoint:** `POST /api_key/new`
- **Request:** `{"user_uuid": "user_id", "api_key_name": "key_name"}`
- **Response:** API key object
- **Status:** 201 Created

### Generate Short URL

- **Endpoint:** `POST /short_url/new`
- **Request:** `{"long_url": "https://example.com/long/url", "api_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"}`
- **Response:** URL mapping object
- **Status:** 200 OK

### Get User URLs

- **Endpoint:** `GET /users/{user_uuid}/urls`
- **Response:** List of URL mappings with long_url and short_url_path
- **Status:** 200 OK

## How It Works

### User Authentication

Users register with a username, password, phone and email, then can log in to authenticate.

### API Key Generation

API keys can be created for authenticated users and can be used for URL shortening.

### Short URL Generation

1. User submits long_url and api_key
2. API key is validated
3. Short URL path is generated using Base62 encoding
4. URL mapping is stored with user association

## Error Responses

- `400 Bad Request` - Missing or invalid parameters
- `401 Unauthorized` - Invalid credentials or API key
- `500 Internal Server Error` - Server error

## Database Collections

- **users** - User documents with user_name, is_active, created_at, updated_at
- **api_keys** - API key hashes with expiration and user association
- **url_map** - URL mappings with long_url, short_url_path, user_id, expiration
- **counter** - URL counter for generating unique IDs
