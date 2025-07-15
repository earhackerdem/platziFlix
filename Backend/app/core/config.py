"""Application configuration using Pydantic Settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

try:
    from app import __version__
except ImportError:
    # When running from within app directory
    from __init__ import __version__


class Settings(BaseSettings):
    """Application settings configuration."""
    
    # Project information
    PROJECT_NAME: str = "Platziflix"
    VERSION: str = __version__
    DESCRIPTION: str = "Plataforma de cursos online - Backend API"
    
    # Database configuration
    DATABASE_URL: str = Field(
        ...,
        description="PostgreSQL database URL",
        examples=["postgresql://user:password@localhost:5432/platziflix"]
    )
    
    # Application configuration
    DEBUG: bool = Field(
        default=False,
        description="Enable debug mode"
    )
    API_PREFIX: str = Field(
        default="/api/v1",
        description="API route prefix"
    )
    
    # Server configuration
    HOST: str = Field(
        default="0.0.0.0",
        description="Server host"
    )
    PORT: int = Field(
        default=8000,
        description="Server port"
    )
    
    # CORS configuration
    ALLOWED_ORIGINS: str = Field(
        default="*",
        description="Allowed CORS origins (comma-separated)"
    )
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    @property
    def allowed_origins_list(self) -> list[str]:
        """Convert ALLOWED_ORIGINS string to list."""
        if self.ALLOWED_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]


# Global settings instance
settings = Settings() 