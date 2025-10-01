from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os 
from src.config.settings import get_settings, Settings
from src.controllers.DataController import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["data","api-v1"]
)


@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,app_settings: Settings = Depends(get_settings)):
      is_valid = DataController().validate_file(file)
      return is_valid