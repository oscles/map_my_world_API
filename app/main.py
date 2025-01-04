from typing import Annotated

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
from app.utils.database import Session, get_session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }
