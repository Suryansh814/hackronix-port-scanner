from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HACKRONIX Port Scanner",
    description="Professional Network Port Scanner API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "project": "HACKRONIX Port Scanner",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }