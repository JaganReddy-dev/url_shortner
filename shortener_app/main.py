from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="URL shortner API",
    version="1.0.0",
    summary="A simple REST API for implementing short URL's.",
    description="""
### 🧾 Overview
This API allows you to **create**, **read**, **update**, and **delete** urls and store it in sqlite3.

### ⚙️ Available Endpoints
- `GET /urls` — Retrieve all urls  
- `GET /urls/{url_id}` — Fetch a single url by ID  
- `POST /urls/add` — Add a new url when url to shorten is provided
- `PUT /url/{url_id}` — Update an existing url  
- `DELETE /url/{url_id}` — Delete an url  

### 💡 Notes
Currently, data is stored **in memory only** — it resets when the server restarts.
This API is great for testing, prototyping, or learning FastAPI basics.
""",
)


class URL(BaseModel):
    text: str


urls: list[URL] = [URL(text="www.google.com"), URL(text="www.maps.google.com")]


@app.get("/")
def root():
    return {"message": "You hit the root of the URL shortner API!"}


@app.get(
    "/urls/{url_id}",
    response_model=URL,
    summary="Get specific url",
    description="Get an url with given urlId from the memory list.",
)
def get_item(url_id: str):
    if url_id in urls:
        return urls[url_id]
    raise HTTPException(status_code=404, detail="URL Not Found!")


@app.post(
    "/urls/add",
    response_model=list[URL],
    summary="Add new url when provided url to shorten",
    description="Create a new url and append it to the in-memory list when provided url to shorten.",
)
def create_item(url: URL):
    urls.append(url)
    return urls


@app.get(
    "/urls",
    response_model=list[URL],
    summary="Get all urls",
    description="Get all urls from the in-memory list.",
)
def get_items():
    return urls
