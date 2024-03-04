from fastapi import FastAPI
from typing import Optional
import uvicorn

app = FastAPI()

todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours"
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book"
    }
]
@app.get('/', tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}

@app.get('/todo', tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": todos}

@app.post('/todo', tags=["Todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A Todo is Added",
    }

@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["Activity"] = body["Activity"]
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }

@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            print(todos)
            return {
                "data": f"Todo with id {id} has been deleted"
            }
    print("id not found")
    return {
        "data": f"This Todo with id {id} is not found!"
    }



# @app.get("/")
# def root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, cab_id: int,q: Optional[str] = None, r: str = None):
#     return {"item_id": item_id, "cab": cab_id, "q": q, "r": r}

# @app.get("/hello")
# def hello(name: str):
#     return {"Hello": name}


# if __name__ == '__main__':
#     uvicorn.run("fastapi_prac:app", host="127.0.0.1", port=3838, log_level="info", reload=True)\
