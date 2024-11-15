from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: PostgresDsn

    # Application settings
    APP_NAME: str = "zODC Backend"
    DEBUG: bool = False

    # API settings
    API_V1_STR: str = "/api/v1"

    # JWT settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()