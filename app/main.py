from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config import settings
from contextlib import asynccontextmanager

# import routers
from app.routers import classe_routes, eleve_routes, matiere_routes, note_routes, professeur_routes, trimestre_routes, user_routes, protected_routes

# import models
from app.models.classe import Classe
from app.models.eleve import Eleve
from app.models.matiere import Matiere
from app.models.note import Notes
from app.models.professeur import Professeur
from app.models.trimestre import Trimestre
from app.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    database = client[settings.DATABASE_NAME]
    await init_beanie(database=database, document_models=[Classe, Eleve, Matiere, Notes, Professeur, Trimestre, User])
    try:
        yield
    finally:
        # Shutdown logic
        client.close()

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(classe_routes.router)
app.include_router(eleve_routes.router)
app.include_router(matiere_routes.router)
app.include_router(note_routes.router)
app.include_router(professeur_routes.router)
app.include_router(trimestre_routes.router)
app.include_router(user_routes.router)
app.include_router(protected_routes.router)