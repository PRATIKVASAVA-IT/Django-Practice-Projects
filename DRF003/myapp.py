import requests
import json

URL="http://127.0.0.1:8000/searchapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    parsed_data=json.dumps(data)
    r=requests.get(url=URL,data=parsed_data)
    data=r.json()
    print(data)


get_data(5)

def post_data():
    data={'name':'rinkesh','roll':908,'city':'bhuj'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data) 

#post_data()
    


def update_data():
    data={'id':6,'city':'vadodara'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
#update_data()

def delete_data():
  data={'id':6}
  json_data=json.dumps(data)
  r=requests.delete(url=URL,data=json_data)
  data=r.json()
  print(data)  

#delete_data()  


