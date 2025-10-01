from fastapi import FastAPI, APIRouter, Depends
from src.config.settings import get_settings, Settings
from typing import Dict, Any

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api-v1"]
)

@base_router.get("/health")
async def health_check(settings: Settings = Depends(get_settings)) -> Dict[str, Any]:
    return {
        "message": "Welcome to the Customer Service RAG System",
        "version": settings.app_version,
        "name": settings.app_name,
        "description": settings.description,
        "author": settings.author,
        "license": settings.license,
        "contact": settings.contact
    }