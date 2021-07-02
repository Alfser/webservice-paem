import requests
import json
from requests.auth import HTTPBasicAuth

def login(cpf):
    url = 'http://localhost:5000/api.paem/auth.bot'
    headers = {"Authentication": f"CPF {cpf}"}
    response = requests.post(url, headers=headers)
    token = json.loads(response.content).get('token')
    if token is None:
         res = False
    else:
         res = True
    return res
