import logging
import logging.config

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api_router

app = FastAPI()
app.add_middleware(CORSMiddleware)
app.include_router(api_router, prefix="/api/v1/my_service")

# https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}},
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        }
    },
    "loggers": {
        "": {"handlers": ["console"], "propagate": False},  # root logger
        "uvicorn": {"handlers": ["console"], "propagate": False},
    },
}
logging.config.dictConfig(logging_config)
