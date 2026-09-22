from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env: str = "local"
    model_name: str = "rule-based-v1"
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_prefix="WAFI_", extra="forbid")
