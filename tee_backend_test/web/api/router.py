from fastapi.routing import APIRouter

from tee_backend_test.web.api import monitoring, brevo, insee

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(brevo.router)
api_router.include_router(insee.router)
