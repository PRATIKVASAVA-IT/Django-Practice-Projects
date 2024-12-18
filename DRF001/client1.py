import requests
url='http://127.0.0.1:8000/check/'

r=requests.get(url=url)

a=r.json()

print(a)