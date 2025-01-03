from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }
