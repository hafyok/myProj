from fastapi import FastAPI
from app.api.casts import casts
from app.api.db import metadata, database, engine
from app.api import models
from app.api.routes import router
from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_url="/openapi.json", docs_url="/")

app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(casts)
