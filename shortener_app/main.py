from fastapi import FastAPI
from shortener_app.Routes.create_short_url import router as urls_router
from shortener_app.Routes.create_user import router as users_router
from shortener_app.Routes.create_api_key import router as api_keys_router

app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    description="A simple URL shortener with API-key-based users",
)

app.include_router(users_router)
app.include_router(urls_router)
app.include_router(api_keys_router)
