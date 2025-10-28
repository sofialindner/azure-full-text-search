from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    search_endpoint: str
    index_name: str
    search_api_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()