import sentry_sdk
from config import SentryConst, AppDataSourceConst
import requests

sentry_sdk.init(
    dsn=SentryConst.SENTRY_DNS,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)


data = requests.get("https://data.cityofchicago.org/resource/f7f2-ggz5.json").json()
print(data)
