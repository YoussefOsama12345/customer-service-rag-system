from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str
    app_version: str 
    description: str 
    author: str
    license: str
    contact: str
    apps_docs_url: str
    

    file_allowed_extensions: List[str]
    file_max_size: int
    
    gemini_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def get_settings() -> Settings:
    return Settings()
