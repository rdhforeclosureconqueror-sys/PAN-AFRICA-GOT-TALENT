from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PAN-AFRICAN GOT TALENT API"
    env: str = "dev"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/pagt"
    redis_url: str = "redis://localhost:6379/0"
    s3_bucket: str = "pagt-assets"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
