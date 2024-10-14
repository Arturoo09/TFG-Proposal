from dotenv import load_dotenv
import os

load_dotenv()


class SentryConst: 
    SENTRY_DNS = os.getenv("SENTRY_DNS")


class AppDataSourceConst:
    APIKEY_SECRET = os.getenv("APIKEY_SECRET")
    APP_TOKEN = os.getenv("APP_TOKEN")
    APP_SECRET_TOKEN = os.getenv("APP_SECRET_TOKEN")