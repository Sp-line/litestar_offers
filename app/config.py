from pydantic import Field, PostgresDsn, AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = Field(default=True)
    DATABASE_URL: PostgresDsn = Field(
        default="postgresql+asyncpg://postgres:postgres@postgres:5432/litestar_offers"
    )

    APP_HOST: str = Field(default="127.0.0.1")
    APP_PORT: int = Field(default=5000)

    CORS_ORIGINS: list[AnyHttpUrl] | list[str] = Field(
        default_factory=lambda: ["http://127.0.0.1:8000"]
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
