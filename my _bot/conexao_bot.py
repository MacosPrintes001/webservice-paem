import re
import requests
import json
from requests.auth import HTTPBasicAuth

token = ' '

#/ pergar o nome e id do discente atraves cpf
#/ saber de qual campus a pessoa é

def login(cpf):
     global token
     try:
          #conexão para pegar o token (funcionado)
          rota_base = 'http://localhost:5000/api.paem'
          headers = {"Authentication": f"CPF {cpf}"}
          response = requests.post(url=f"{rota_base}/auth.bot", headers=headers)
          #print(response.json())
          token = json.loads(response.content).get('token')

          if token is None:
               return False
          else: #se retornar um token, acesso a rota usuarios
               res = True
               bearer_token = f"Bearer {token}"
               payload = {"Authorization":bearer_token}
               res = requests.get(
               url=f"{rota_base}/usuarios",
               headers=payload
               )
               print(res.json())
               return res
               #/pegar id e nome do usuario
     except EOFError:#problea de conexão
          return "erro"

def search_campus(campus):
     pass
#login(11111111111)