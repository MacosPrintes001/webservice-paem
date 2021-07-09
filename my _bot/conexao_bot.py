import re
import requests
import json
from requests.auth import HTTPBasicAuth

token = ' '
rota_base = 'http://localhost:5000/api.paem'

#/ pergar o nome e id do discente atraves cpf
#/ saber de qual campus a pessoa é

def login(cpf):
     global token
     try:
          #conexão para pegar o token (funcionado)
          headers = {"Authentication": f"CPF {cpf}"}
          response = requests.post(url=f"{rota_base}/auth.bot", headers=headers)
          token = json.loads(response.content).get('token')

          if token is None:
               pass
               #return False
          else: #se retornar um token, acesso a rota usuarios
               search_dados(token, cpf)
     except EOFError:#problea de conexão
          pass
          #return "erro"

def search_dados(token, cpf):
     res = True
     bearer_token = f"Bearer {token}"
     payload = {"Authorization":bearer_token}
     res = requests.get(
     url=f"{rota_base}/usuarios",
     headers=payload
     )

     print(res.json())

     if cpf in res.json():
          print("achei")
     else:
          print("não achei")

"""
def search_campus(campus):
     pass


def envia_dados():
     pass"""

my_cpf = 11111111111
login(my_cpf)