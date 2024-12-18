import requests
import json

URL='http://127.0.0.1:8000/details/'

data={'name':'jay','roll':106,'city':'Bharuch'}

jsondata=json.dumps(data)

r= requests.post(url= URL, data = jsondata)

data=r.json()


print(data)