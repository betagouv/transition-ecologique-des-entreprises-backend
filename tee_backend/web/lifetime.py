from typing import Awaitable, Callable

from fastapi import FastAPI
# from prometheus_fastapi_instrumentator.instrumentation import (
#     PrometheusFastApiInstrumentator,
# )


# def setup_prometheus(app: FastAPI) -> None:  # pragma: no cover
#     """
#     Enables prometheus integration.

#     :param app: current application.
#     """
#     PrometheusFastApiInstrumentator(should_group_status_codes=False).instrument(
#         app,
#     ).expose(app, should_gzip=True, name="prometheus_metrics")


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        # setup_prometheus(app)
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        pass  # noqa: WPS420

    return _shutdown
