"""
FastAPI Application Entry Point.
This is the main server file that configures and runs the application.
"""
from fastapi import FastAPI
from app.core.config import get_settings
from app.routes import health

# Load settings
settings = get_settings()

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="A simple Order Management System API for learning backend fundamentals",
    version="1.0.0",
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc",    # ReDoc
)

# Include routers
app.include_router(health.router)


@app.get("/")
def root():
    """Root endpoint - API information."""
    return {
        "message": "Welcome to the Order Management System API",
        "docs": "/docs",
        "health": "/health"
    }
