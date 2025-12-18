from fastapi import FastAPI
from shortener_app.routes.urls import router as urls_router
from shortener_app.routes.users import router as users_router

app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    description="A simple URL shortener with API-key-based users",
)

app.include_router(users_router)
app.include_router(urls_router)
