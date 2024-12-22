from fastapi import HTTPException
import logging
from api_handler.items.metadata.items_init import items_db_metadata, items_router
from api_handler.items.metadata.items_dt import Item


@items_router.delete("/{item_id}", response_model = Item)
async def delete_item_by_id(item_id : int):
    try:
        found = await items_db_metadata.items_collection.find_one({"id": item_id})
        if not found:
            raise HTTPException(status_code=404, detail="Item not found.")
        
        deleted = await items_db_metadata.items_collection.delete_one(filter={"id": item_id})
        if deleted.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Item cloud not be deleted.")
        
        return found
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as unexpect_err:
        logging.basicConfig(level=logging.DEBUG)
        logging.error(str(unexpect_err))
        raise HTTPException(status_code=500, detail='Internal Server Error.')