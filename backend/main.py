from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/", tags=["Blog"])
def hello():
    """Basic route to test the server."""
    return {"msg": "Hello FastAPI! 🚀"}