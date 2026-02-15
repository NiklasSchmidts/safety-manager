from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "safety_db"
    DB_PORT: int = 5432
    ENVIRONMENT: str = "development"

    @computed_field
    @property
    def CONNECTION_STRING(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @computed_field
    @property
    def is_local(self) -> bool:
        return self.ENVIRONMENT == "development"


settings = Settings()
