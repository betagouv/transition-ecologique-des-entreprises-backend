import uvicorn

from tee_backend_test.settings import settings

def serve() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "tee_backend_test.web.app:app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        # reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=False,
    )


if __name__ == "__main__":
    serve()
