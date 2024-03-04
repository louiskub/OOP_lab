from fastapi import FastAPI

app = FastAPI()

class MyObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

@app.get("/member/{id}/{name}")
async def create_object(id: int, name: str = None, memberId: str = None):
    return [id+10, name+" hello ", "KUYYYYY" + memberId]


