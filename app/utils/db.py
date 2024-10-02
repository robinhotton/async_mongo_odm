from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from .settings import Settings
from ..models import all_models


@asynccontextmanager
async def lifespan(app: FastAPI): # Obligatoire : inversion de dépendance
    client = AsyncIOMotorClient(Settings.MONGODB_URI)
    database = client[Settings.DATABASE_NAME]
    await init_beanie(database=database, document_models=all_models)
    try:
        yield
    finally:
        client.close()