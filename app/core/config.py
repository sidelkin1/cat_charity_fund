from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Название приложения'
    app_description: str = 'Описание приложения'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
