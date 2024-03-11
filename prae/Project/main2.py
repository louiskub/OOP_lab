from typing import Optional
from fastapi import FastAPI
import uvicorn


app = FastAPI()
@app.get("/test")
def read_root(request:str, reply:str):
    return {"Request" : request, "Reply": reply}

@app.get("/item/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id" : item_id, "q": q}

