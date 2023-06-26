from fastapi.routing import APIRouter

from tee_backend_test.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
