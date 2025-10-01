from src.controllers.BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_in_mb = self.settings.file_max_size * 1024 * 1024
        
    
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.settings.file_allowed_extensions:
            raise False
        if file.size > self.size_in_mb:
           return False
        return True