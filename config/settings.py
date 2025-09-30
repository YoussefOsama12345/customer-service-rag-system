import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")
    APP_DESCRIPTION: str = os.getenv("DESCRIPTION")
    APP_AUTHOR: str = os.getenv("AUTHOR")
    APP_LICENSE: str = os.getenv("LICENSE")
    APP_CONTACT: str = os.getenv("CONTACT")
    APP_DOCS_URL: str = os.getenv("APP_DOCS_URL")

settings = Settings()
    
    