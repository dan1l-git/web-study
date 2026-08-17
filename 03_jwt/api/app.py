from fastapi import FastAPI
from api.database import engine, Base
from api.routers.auth import router as auth_router

app = FastAPI(title="Auth Service")
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)