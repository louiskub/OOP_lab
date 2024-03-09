import requests
from datetime import date, datetime
url = "http://127.0.0.1:8000/root"

req = requests.get(url)
input_date = datetime.strptime(req.json(), '%Y-%m-%d').date()
print(type(req.json()), req.json(), type(input_date))

from datetime import date
r = [{
    "money": 700,
    "detail": "2030-06-20"
},{
    "money": 600,
    "detail": "2030-05-15"}
# },{
#     "money": 500,
#     "detail": date(2024, 1, 5)
# },{
#     "money": 400,
#     "detail": date(2024, 3, 8)
# },{
#     "money": 300,
#     "detail": date(2024, 9, 12)
# },{
#     "money": 200,
#     "detail": date(2024, 12, 22)
# },{
#     "money": 100,
#     "detail": date(2025, 7, 21)
# }
]
r.sort(key = lambda e: e['detail'])
print(r)