import requests
import json

reponse = requests.get('http://127.0.0.1:8000/api/get')

# print(reponse.json())
print(reponse.json()[0])
