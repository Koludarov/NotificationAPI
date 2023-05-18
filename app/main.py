from fastapi import FastAPI
from app.database import database
from app.tasks.celery import celery_app
from api.routes import mailings, messages


app = FastAPI()


app.include_router(mailings.router)
app.include_router(messages.router)
@app.on_event("startup")
async def startup():
    await database.connect()
    celery_app.conf.update(app=app)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
