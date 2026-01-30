from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

_db: Dict[int, Item] = {}

@app.post("/items/")
def create_item(item: Item):
    if item.id in _db:
        raise HTTPException(status_code=400, detail="exists")
    _db[item.id] = item
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = _db.get(item_id)
    if not item:
        raise HTTPException(status_code=404)
    return item
