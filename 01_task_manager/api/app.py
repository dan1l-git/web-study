from fastapi import FastAPI
from api.database import engine, Base
from api.routers.task import router as tasks_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tasks_router)

@app.get("/ping")
def ping():
    return {"status": "ok"}