from fastapi import FastAPI
from shortener_app.Routes.short_url import router as urls_router
from shortener_app.Routes.api_key import router as api_keys_router
from shortener_app.Routes.signup import router as signup_router
from shortener_app.Routes.login import router as login_router
from shortener_app.Routes.user import router as user_router

app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    description="A simple URL shortener with API-key-based users",
)

app.include_router(login_router)
app.include_router(urls_router)
app.include_router(api_keys_router)
app.include_router(signup_router)
app.include_router(user_router)
