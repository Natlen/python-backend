from fastapi import HTTPException
import logging
from api_handler.items.metadata.items_init import items_db_metadata, items_router
from api_handler.items.metadata.items_dt import Item


@items_router.post("/", response_model = Item)
async def post_item(item : Item):
    try:
        found = await items_db_metadata.items_collection.find_one({"id": item.id})
        if found:
            raise HTTPException(status_code=409, detail="Already exists.")
        
        await items_db_metadata.items_collection.insert_one(item.dictionarify())
        return item
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as unexpect_err:
        logging.basicConfig(level=logging.DEBUG)
        logging.error(str(unexpect_err))
        raise HTTPException(status_code=500, detail='Internal Server Error.')