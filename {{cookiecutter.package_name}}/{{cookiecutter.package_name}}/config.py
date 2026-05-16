from starlette.config import Config

# Load configuration from environment variable AND .env file:
config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
