from fastapi import FastAPI
from app.database import database
from app.tasks.celery import celery_app
from app.api.routes import router


app = FastAPI()


app.include_router(router)
@app.on_event("startup")
async def startup():
    await database.connect()
    celery_app.conf.update(app=app)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
