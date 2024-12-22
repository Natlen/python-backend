from fastapi    import FastAPI
from typing     import AsyncGenerator

from db_handler.db_handler_mongo    import db_handler_mongo

from api_handler.items.crud.items_api_create    import items_router as items_router_c
from api_handler.items.crud.items_api_read      import items_router as items_router_r
from api_handler.items.crud.items_api_update    import items_router as items_router_u
from api_handler.items.crud.items_api_delete    import items_router as items_router_d

async def app_startup(app : FastAPI) -> None:
    await db_handler_mongo.mongodb_cluter_connect()
    await db_handler_mongo.mongodb_cluster_check_connection()

async def app_shutdown(app : FastAPI) -> None:
    await db_handler_mongo.mongodb_cluter_disconnect()

async def app_lifespan(app : FastAPI) -> AsyncGenerator[any, any]:
    await app_startup(app)
    yield
    await app_shutdown(app)

app : FastAPI = FastAPI(lifespan = app_lifespan)

# Items API #

ITEMS_API_PREFIX : str = '/items'
ITEMS_API_TAGS : str = 'Items'

app.include_router(items_router_c, prefix=ITEMS_API_PREFIX, tags=ITEMS_API_TAGS)
app.include_router(items_router_r, prefix=ITEMS_API_PREFIX, tags=ITEMS_API_TAGS)
app.include_router(items_router_u, prefix=ITEMS_API_PREFIX, tags=ITEMS_API_TAGS)
app.include_router(items_router_d, prefix=ITEMS_API_PREFIX, tags=ITEMS_API_TAGS)

# --------- #

