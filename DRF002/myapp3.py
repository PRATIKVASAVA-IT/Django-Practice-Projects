import requests 
import json

URL='http://127.0.0.1:8000/updated/' 

data={'id':5,'name':'Janki'}
json_data=json.dumps(data)
r=requests.put(url=URL,data=json_data)

v=r.json()
print(v)

