from fastapi.routing import APIRouter

from tee_backend_test.web.api import docs, monitoring, brevo, insee

api_router = APIRouter()
api_router.include_router(docs.router)
api_router.include_router(monitoring.router)
api_router.include_router(brevo.router, prefix="/brevo", tags=["brevo"])
api_router.include_router(insee.router, prefix="/insee", tags=["insee"])
