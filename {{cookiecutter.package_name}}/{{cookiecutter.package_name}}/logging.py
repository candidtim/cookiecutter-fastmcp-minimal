import logging.config

from .config import DEBUG


def init_logging():
    msg_fmt = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": msg_fmt,
                }
            },
            "handlers": {
                "stdout": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                }
            },
            "root": {
                "level": "DEBUG" if DEBUG else "INFO",
                "handlers": ["stdout"],
            },
            "loggers": {
                "": {
                    "level": "DEBUG" if DEBUG else "INFO",
                    "handlers": ["stdout"],
                },
                "{{cookiecutter.package_name}}": {
                    "level": "DEBUG" if DEBUG else "INFO",
                    "handlers": ["stdout"],
                },
                "fastmcp": {
                    "level": "DEBUG" if DEBUG else "INFO",
                    "handlers": ["stdout"],
                    "propagate": False,
                },
                "starlette": {
                    "handlers": ["stdout"],
                    "level": "INFO",
                    "propagate": False,
                },
                "uvicorn": {
                    "handlers": ["stdout"],
                    "level": "INFO",
                    "propagate": False,
                },
            },
            "disable_existing_loggers": False,
        }
    )
