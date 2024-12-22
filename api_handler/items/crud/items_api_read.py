from fastapi import HTTPException
import logging
from api_handler.items.metadata.items_init import items_db_metadata, items_router
from api_handler.items.metadata.items_dt import Item


@items_router.get("/", response_model = list[Item])
async def get_items():
    try:
        items = await items_db_metadata.items_collection.find().to_list(length=None)
        if not items:
            raise HTTPException(status_code=404, detail="Items not found.")
        return items
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as unexpect_err:
        logging.basicConfig(level=logging.DEBUG)
        logging.error(str(unexpect_err))
        raise HTTPException(status_code=500, detail='Internal Server Error.')

@items_router.get("/{item_id}", response_model = Item)
async def get_item_by_id(item_id : int):
    try:
        item = await items_db_metadata.items_collection.find_one({"id": item_id})
        if not item:
            raise HTTPException(status_code=404, detail="Item not found.")
        return item
    
    except HTTPException as http_error:
        raise http_error
    
    except Exception as unexpect_err:
        logging.basicConfig(level=logging.DEBUG)
        logging.error(str(unexpect_err))
        raise HTTPException(status_code=500, detail='Internal Server Error.')
