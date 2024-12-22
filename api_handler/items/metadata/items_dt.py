from pydantic import BaseModel

class Item(BaseModel):
    
    id: int
    name: str
    
    def dictionarify(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }
    