from fastapi import FastAPI
from datetime import datetime
import os
from api import router
from modules.sentry_module import Sentry

sentry_module = Sentry()

app = FastAPI(
    title="TFG",
    version="0.0.1",
)

@app.get("/status")
def get_status():
    return {
        "message" : "API works",
        "date" : f"{datetime.now()}",
    }

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

