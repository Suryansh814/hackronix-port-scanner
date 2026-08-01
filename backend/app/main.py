from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.utils.validator import is_valid_target
from app.api.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def home():
    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.get("/validate/{target}")
def validate_target(target: str):
    return {
        "target": target,
        "valid": is_valid_target(target)
    }
