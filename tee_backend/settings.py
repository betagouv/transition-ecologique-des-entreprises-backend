import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic import BaseSettings

# TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    # host: str = "0.0.0.0"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    token_api_brevo: str = ""
    token_api_siren: str = ""

    # This variable is used to define
    # multiproc_dir. It's required for [uvi|guni]corn projects.
    # prometheus_dir: Path = TEMP_DIR / "prom"

    api_brevo: str = "https://api.brevo.com/v3"
    api_siren: str = "https://api.insee.fr/entreprises/sirene/V3"

    class Config:
        env_file = ".env"
        env_prefix = "TEE_BACKEND_"
        env_file_encoding = "utf-8"


settings = Settings()
