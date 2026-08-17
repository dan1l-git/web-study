from fastapi import FastAPI
from api.database import engine, Base
from api.routers.auth import router as auth_router
from api.routers.users import router as users_router

app = FastAPI(title="Auth Service")
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(users_router)