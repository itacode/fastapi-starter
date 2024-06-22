from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    UPLOAD_FOLDER: str
    MY_SERVICE_DB_USER: str
    MY_SERVICE_DB_PASSWORD: str
    MY_SERVICE_DB_HOST: str
    MY_SERVICE_DB_PORT: str
    MY_SERVICE_DB_NAME: str

    def get_db_url(self):
        return (
            f"mysql+pymysql://{self.MY_SERVICE_DB_USER}"
            + f":{self.MY_SERVICE_DB_PASSWORD}"
            + f"@{self.MY_SERVICE_DB_HOST}"
            + f":{self.MY_SERVICE_DB_PORT}"
            + f"/{self.MY_SERVICE_DB_NAME}"
        )


settings = Settings()


# https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "uvicorn_formatter": {
            "format": "%(asctime)s - uvicorn - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "uvicorn_handler": {
            "level": "INFO",
            "formatter": "uvicorn_formatter",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "propagate": False,
        },  # root logger
        "uvicorn": {
            "handlers": ["uvicorn_handler"],
            "propagate": False,
        },
    },
}
