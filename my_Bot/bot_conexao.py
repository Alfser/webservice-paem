import requests
import json
from requests.auth import HTTPBasicAuth


# def login(cpf):
cpf = '22222222222'
url = 'http://localhost:5000/api.paem/auth.bot'
headers = {"Authentication": f"CPF {cpf}"}
response = requests.post(url, headers=headers)
print(response.text)
# token = json.loads(response.content).get('nome')
# if token is None:
#     res = False
# else:
#     res = True
# return token, res
