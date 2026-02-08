from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ZYRA API"
    version: str = "1.0.0"
    environment: str = "production"


settings = Settings()
