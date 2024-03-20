import os

import uvicorn
from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine
from loguru import logger
import sys

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")

logger.add(sys.stdout, level="INFO")

port = os.getenv("PORT")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=int(port))
