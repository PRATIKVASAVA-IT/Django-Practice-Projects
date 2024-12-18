import requests
import json

URL="http://127.0.0.1:8000/myapi/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)    
    header={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=header,data=json_data)
    data=r.json()
    print(data)

#get_data()


def post_data():
    data={
        'name':'Aarti',
        'roll':103,
        'city':'Mumbai'

    }

    json_data=json.dumps(data)
    header={'content-Type':'application/json'}
    r=requests.post(url=URL,headers=header,data=json_data)
    data=r.json()
    print(data)

post_data()    
