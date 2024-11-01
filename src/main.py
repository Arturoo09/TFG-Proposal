import requests
from modules.config import AppDataSourceConst
from modules.sentry import Sentry

sentry = Sentry()


data = requests.get("https://data.cityofchicago.org/resource/f7f2-ggz5.json").json()
print(data)
