# import os
# import shutil
import json
from loguru import logger

from tee_backend.logging import configure_logging

import uvicorn

from tee_backend.settings import settings


# def set_multiproc_dir() -> None:
#     """
#     Sets mutiproc_dir env variable.

#     This function cleans up the multiprocess directory
#     and recreates it. This actions are required by prometheus-client
#     to share metrics between processes.

#     After cleanup, it sets two variables.
#     Uppercase and lowercase because different
#     versions of the prometheus-client library
#     depend on different environment variables,
#     so I've decided to export all needed variables,
#     to avoid undefined behaviour.
#     """
#     shutil.rmtree(settings.prometheus_dir, ignore_errors=True)
#     os.makedirs(settings.prometheus_dir, exist_ok=True)
#     os.environ["prometheus_multiproc_dir"] = str(
#         settings.prometheus_dir.expanduser().absolute(),
#     )
#     os.environ["PROMETHEUS_MULTIPROC_DIR"] = str(
#         settings.prometheus_dir.expanduser().absolute(),
#     )

def serve() -> None:
    """Entrypoint of the application."""
    configure_logging()

    # set_multiproc_dir()
    # print(f'settings', settings)
    settings_json = json.dumps(settings.dict(), indent=4)
    logger.debug(f'settings : {settings_json}')

    uvicorn.run(
        "tee_backend.web.app:app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=False,
    )


if __name__ == "__main__":
    serve()
