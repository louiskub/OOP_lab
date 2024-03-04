import requests as req
import json
r = req.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
data = r.json()
print(data)
print(f"ผู้ป่วย: {data[0]['total_case']}")
# print(dir(r))
