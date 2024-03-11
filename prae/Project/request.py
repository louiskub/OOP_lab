import requests
import json


act = {"id" : 4,"activity" : "Do homework"}
r = requests.post("http://127.0.0.1:8000/todo",data=json.dumps(act))
print(r.json())

act = {"id" : 3,"activity" : "Play games"}
r = requests.put("http://127.0.0.1:8000/todo/3",data=json.dumps(3, act))
print(r.json())

# r = requests.delete("http://127.0.0.1:8000/todo/3")
# print(r)
# print(r.json())

# r = requests.delete("http://127.0.0.1:8000/todo/4")
# print(r)
# print(r.json())

r = requests.get("http://127.0.0.1:8000/todo")
print(r.json())
