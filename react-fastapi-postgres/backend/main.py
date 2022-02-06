"""implement main

author: kyeongmin woo
email: wgm0601@gmail.com
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item1(BaseModel):
    name: str
    desc: str

class Item2(BaseModel):
    name: str
    desc: str


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/")
async def add_root():
    return {"message": "Hello World"}

@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/item/{item_id}")
async def add_item(item_id: int, item1: Item1):
    return {"item_id": item_id, "name" : item1.name}

@app.post("/double_item/{item_id}")
async def add_double_item(item_id: int, item1: Item1, item2: Item2):
    return {"item_id": item_id, "name1" : item1.name, "name2":item2.name}
