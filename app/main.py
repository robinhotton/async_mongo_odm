from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.profile import Profile
from app.config import settings
from contextlib import asynccontextmanager
from app.routers import profile

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    database = client[settings.DATABASE_NAME]
    await init_beanie(database=database, document_models=[Profile])
    try:
        yield
    finally:
        # Shutdown logic
        client.close()

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(profile.router, prefix="/api/v1")
