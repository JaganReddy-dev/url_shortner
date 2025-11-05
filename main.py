from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Item Management API",
    version="1.0.0",
    summary="A simple REST API for managing items.",
    description="""
### 🧾 Overview
This API allows you to **create**, **read**, **update**, and **delete** items stored in memory.

It demonstrates key FastAPI concepts like:
- Data validation with **Pydantic**
- Path and body parameters
- Automatic **OpenAPI/Swagger documentation**
- Type-safe responses with `response_model`

### ⚙️ Available Endpoints
- `GET /items` — Retrieve all items  
- `GET /items/{item_id}` — Fetch a single item by ID  
- `POST /items/add` — Add a new item  
- `PUT /items/{item_id}` — (future) Update an existing item  
- `DELETE /items/{item_id}` — (future) Delete an item  

### 💡 Notes
Currently, data is stored **in memory only** — it resets when the server restarts.
This API is great for testing, prototyping, or learning FastAPI basics.
""",
)


class Item(BaseModel):
    text: str


items: list[Item] = [Item(text="apple"), Item(text="banana")]


@app.get("/")
def root():
    return {"Hey": "You!"}


@app.get(
    "/items/{item_id}",
    response_model=Item,
    summary="Get specific item",
    description="Get an item with given itemId from the memory list.",
)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item Not Found!")


@app.post(
    "/items/add",
    response_model=list[Item],
    summary="Add new item",
    description="Create a new item and append it to the in-memory list.",
)
def create_item(item: Item):
    items.append(item)
    return items


@app.get(
    "/items",
    response_model=list[Item],
    summary="Get all items",
    description="Get all items from the in-memory list.",
)
def get_items():
    return items
