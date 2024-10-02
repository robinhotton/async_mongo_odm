from fastapi import FastAPI
from .utils import lifespan
from .routers import router

app = FastAPI(lifespan=lifespan)
app.include_router(router)