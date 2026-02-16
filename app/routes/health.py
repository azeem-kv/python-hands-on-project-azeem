"""
Health check endpoint for service monitoring.
Used by Docker, load balancers, and monitoring tools.
"""
from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    """
    Health check endpoint.
    Returns 200 OK if the service is running.
    """
    return {
        "status": "healthy",
        "service": "Order Management System"
    }
