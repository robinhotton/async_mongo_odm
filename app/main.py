from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config import settings
from contextlib import asynccontextmanager

from .routers import router
from .models import all

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    database = client[settings.DATABASE_NAME]
    await init_beanie(database=database, document_models=all)
    try:
        yield
    finally:
        client.close()

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(router)