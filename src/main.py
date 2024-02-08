from fastapi import FastAPI
from .config import settings

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/")
async def read_tasks():
    return {"Hello": "World"}


@app.get("/info")
async def info():
    return {
        "db_name": settings.DB_NAME,
        "db_password": settings.DB_PASSWORD,
        "db_username": settings.DB_USERNAME,
    }
