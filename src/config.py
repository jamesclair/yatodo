from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOSTNAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_PORT: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def DB_URL(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
