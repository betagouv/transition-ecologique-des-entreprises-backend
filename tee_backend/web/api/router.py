from fastapi.routing import APIRouter

from tee_backend.web.api import brevo, docs, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
# api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(brevo.router, prefix="/brevo", tags=["brevo"])
api_router.include_router(brevo.router, prefix="/insee", tags=["insee"])
