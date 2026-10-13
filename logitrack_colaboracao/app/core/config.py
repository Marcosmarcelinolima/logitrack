"""Configurações carregadas do ambiente."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://logitrack:logitrack@localhost:5432/logitrack"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
