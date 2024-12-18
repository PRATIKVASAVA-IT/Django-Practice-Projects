import requests
import json


URL="http://127.0.0.1:8000/get_all/" 

r=requests.get(url=URL)

a=r.json()

print(a)

