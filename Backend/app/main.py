"""FastAPI main application for Platziflix."""

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import settings


# Response models
class WelcomeResponse(BaseModel):
    """Response model for welcome endpoint."""
    message: str
    project: str
    version: str


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str
    service: str
    version: str
    timestamp: datetime


# FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/", response_model=WelcomeResponse)
async def root() -> WelcomeResponse:
    """Welcome endpoint with project information."""
    return WelcomeResponse(
        message=f"Bienvenido a {settings.PROJECT_NAME}",
        project=settings.PROJECT_NAME,
        version=settings.VERSION
    )


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="ok",
        service=settings.PROJECT_NAME,
        version=settings.VERSION,
        timestamp=datetime.now()
    ) 