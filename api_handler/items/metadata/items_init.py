from fastapi import APIRouter
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Generator
import os
from dotenv import load_dotenv

from db_handler.db_handler_mongo import db_handler_mongo
# CFG #

items_db_envkey : str = 'MONGODB_ITEM_DB_NAME'
items_collection_envkey : str = 'MONGODB_ITEM_COLLECTION_NAME'
items_env_path : str = 'api_handler/items/metadata/.env'

# --- #

class ItemsDBMetadata():

    items_db : Database
    items_collection : Collection

    def __init__(self, items_db, items_collection):
        self.items_db = items_db
        self.items_collection = items_collection
    

items_db_metadata : ItemsDBMetadata = ItemsDBMetadata(items_db = None, items_collection = None)

def items_router_startup(app : APIRouter) -> None:
    global items_db_metadata
    load_dotenv(dotenv_path=items_env_path)
    items_db_name : str = os.getenv(items_db_envkey)
    items_collection_name : str = os.getenv(items_collection_envkey)
    if not items_db_name or not items_collection_name:
        raise ValueError(f'could not load \'items_db_name\' and \'items_collection_name\' ')
    items_db_metadata.items_db = db_handler_mongo.client[items_db_name]
    items_db_metadata.items_collection = items_db_metadata.items_db[items_collection_name]

def items_router_shutdown(app : APIRouter) -> None:
    pass

def items_router_lifespan(app : APIRouter) -> Generator[None, None, None]:
    items_router_startup(app)
    yield
    items_router_shutdown(app)

items_router : APIRouter = APIRouter(lifespan = items_router_lifespan)

