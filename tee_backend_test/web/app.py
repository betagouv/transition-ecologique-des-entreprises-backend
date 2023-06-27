# from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from tee_backend_test.web.api.router import api_router

app = FastAPI(
    title="tee_backend_test",
    # version=metadata.version("tee_backend_test"),
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    # FIXME not safe
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main router for the API.
app.include_router(router=api_router, prefix="/api")

