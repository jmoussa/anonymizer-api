from fastapi import FastAPI, WebSocket

# from websockets.exceptions import ConnectionClosedError
# from starlette.websockets import WebSocketDisconnect
from mongodb import close_mongo_connection, connect_to_mongo, get_nosql_db
from starlette.middleware.cors import CORSMiddleware
from config import MONGODB_DB_NAME
from api import router as api_router

import pymongo
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        db.create_collection("user_info")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
        pass
    try:
        db.create_collection("de-anon")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
        pass
    try:
        user_collection = db.users
        de_anon_collection = db["de-anon"]
        user_collection.create_index("username", name="username", unique=True)
        de_anon_collection.create_index("connector_id", name="connector_id", unique=True)
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
        pass


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


app.include_router(api_router, prefix="/api")
