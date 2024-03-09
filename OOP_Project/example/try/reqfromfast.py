import requests
import json



def get_todo():
    r = requests.get('http://127.0.0.1:3838/todo')
    print(r)
    print(r.json())

def post_todo(id, activity):
    act = {"id": str(id), "Activity": activity}
    r = requests.post('http://127.0.0.1:3838/todo', data=json.dumps(act))
    print(r)
    print(r.json())

def put_todo(id, activity):
    act = {"id": str(id), "Activity": activity}
    r = requests.put(f'http://127.0.0.1:3838/todo/{str(id)}', data=json.dumps(act))
    print(r)
    print(r.json())

def delete_todo(id):
    r = requests.delete(f'http://127.0.0.1:3838/todo/{str(id)}')

post_todo(3, "Play football")
# put_todo(3, "Sell Shop")
# delete_todo(1)
#get_todo()