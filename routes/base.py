from fastapi import FastAPI, APIRouter
from config.settings import settings

app = APIRouter(
    prefix="/api/v1",
    tags=["api-v1"]
)

# health check

@app.get("/health")
async def health_check():
    return {
        "message": "Welcome to the Customer Service RAG System",
        "version": settings.APP_VERSION,
        "name": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "author": settings.APP_AUTHOR,
        "license": settings.APP_LICENSE,
        "contact": settings.APP_CONTACT
    }