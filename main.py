from fastapi import FastAPI
from routes.base import app as base_app

app = FastAPI()

app.include_router(base_app)