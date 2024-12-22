from fastapi import HTTPException
import logging
from api_handler.items.metadata.items_init import items_db_metadata, items_router
from api_handler.items.metadata.items_dt import Item


@items_router.put("/", response_model = Item)
async def put_item(item : Item):
    try:
        found = await items_db_metadata.items_collection.find_one({"id": item.id})
        if not found:
            raise HTTPException(status_code=404, detail="Item not found.")
        
        updated = await items_db_metadata.items_collection.update_one(
            filter={"id": item.id}, 
            update={"$set": {
                "name": item.name
            }})
        if updated.modified_count == 0:
            raise HTTPException(status_code=404, detail="Item cloud not be updated.")
        
        return item
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as unexpect_err:
        logging.basicConfig(level=logging.DEBUG)
        logging.error(str(unexpect_err))
        raise HTTPException(status_code=500, detail='Internal Server Error.')